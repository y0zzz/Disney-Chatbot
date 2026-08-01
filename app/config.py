"""Configuration for the Disney chatbot, read from environment variables."""

import os

# Base URL of your llm-api proxy, e.g. "https://llm-api.onrender.com"
# Leave unset to disable LLM fallback entirely (Wikipedia-only fallback).
LLM_API_BASE_URL: str | None = os.environ.get("LLM_API_BASE_URL")

# The X-API-Key value your llm-api proxy expects.
LLM_API_KEY: str | None = os.environ.get("LLM_API_KEY")

# Must match a key in llm-api's AVAILABLE_MODELS.
LLM_MODEL: str = os.environ.get("LLM_MODEL", "llama-3.1-8b")

# Seconds to wait before giving up on the LLM proxy and falling back.
LLM_TIMEOUT_SECONDS: float = float(os.environ.get("LLM_TIMEOUT_SECONDS", "15"))
