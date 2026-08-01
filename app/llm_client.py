"""Thin client for calling the llm-api proxy (github.com/y0zzz/llm-api).

Hits the /generate endpoint with the same request shape that proxy expects:
    POST {base_url}/generate
    Header: X-API-Key: <key>
    Body:   {"prompt": "...", "model": "...", "stream": false}
    Response: {"status": "success", "response": "...", "cached": bool}
"""

import logging

import httpx

from app.config import LLM_API_BASE_URL, LLM_API_KEY, LLM_MODEL, LLM_TIMEOUT_SECONDS

logger = logging.getLogger(__name__)

SYSTEM_PREAMBLE = (
    "You are a knowledgeable, concise assistant answering questions about "
    "Disney movies, characters, and The Walt Disney Company. Answer in 2-4 "
    "sentences unless more detail is clearly needed. If the question isn't "
    "about Disney, politely say you can only help with Disney topics."
)


class LLMClient:
    def __init__(
        self,
        base_url: str | None = LLM_API_BASE_URL,
        api_key: str | None = LLM_API_KEY,
        model: str = LLM_MODEL,
        timeout: float = LLM_TIMEOUT_SECONDS,
    ):
        self.base_url = base_url.rstrip("/") if base_url else None
        self.api_key = api_key
        self.model = model
        self.timeout = timeout

    @property
    def is_configured(self) -> bool:
        return bool(self.base_url and self.api_key)

    async def ask(self, question: str) -> str | None:
        """Returns the LLM's answer, or None if the call failed/isn't configured."""
        if not self.is_configured:
            return None

        prompt = f"{SYSTEM_PREAMBLE}\n\nQuestion: {question}"

        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.base_url}/generate",
                    headers={"X-API-Key": self.api_key},
                    json={"prompt": prompt, "model": self.model, "stream": False},
                )
                response.raise_for_status()
                data = response.json()
                return data.get("response")
        except httpx.HTTPStatusError as exc:
            logger.warning("llm-api returned %s: %s", exc.response.status_code, exc.response.text)
        except httpx.RequestError as exc:
            logger.warning("Could not reach llm-api: %s", exc)
        except (ValueError, KeyError) as exc:
            logger.warning("Unexpected response shape from llm-api: %s", exc)

        return None
