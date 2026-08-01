"""Core chatbot logic: routes a user message to the right answer source.

Order of precedence:
  1. Local knowledge base (instant, free, always correct)
  2. LLM proxy (llm-api) -- handles anything not explicitly hardcoded
  3. Wikipedia summary -- last-resort fallback if the LLM is unavailable
"""

from app.disneydata import COMPANY_FACTS, find_movie
from app.llm_client import LLMClient
from app.wiki import WikipediaHelper

FALLBACK_MESSAGE = (
    "I'm not sure how to answer that. Try asking about a Disney movie, "
    "or about the company's history, founder, or CEO."
)


class DisneyChatbot:
    def __init__(
        self,
        wiki_helper: WikipediaHelper | None = None,
        llm_client: LLMClient | None = None,
    ):
        self.wiki_helper = wiki_helper or WikipediaHelper()
        self.llm_client = llm_client or LLMClient()

    async def respond(self, user_input: str) -> str:
        if not user_input or not user_input.strip():
            return FALLBACK_MESSAGE

        text = user_input.lower()

        # 1. Known movie facts (fast, no network call)
        movie = find_movie(text)
        if movie:
            return f"{movie.title} was released on {movie.release_date}."

        # 2. Company facts
        for keyword, fact in COMPANY_FACTS.items():
            if keyword in text:
                return fact

        # 3. LLM fallback -- handles anything open-ended
        llm_answer = await self.llm_client.ask(user_input)
        if llm_answer:
            return llm_answer

        # 4. Wikipedia, only if the LLM is unavailable/unconfigured
        if "film" in text or "movie" in text:
            movie_name = self._extract_topic(text)
            if movie_name:
                return self.wiki_helper.get_summary(movie_name)

        if "company info" in text or "company history" in text or "history" in text:
            return self.wiki_helper.get_summary("The Walt Disney Company")

        return FALLBACK_MESSAGE

    @staticmethod
    def _extract_topic(text: str) -> str:
        """Pull the likely topic out of a phrase like 'tell me about the film X'."""
        for splitter in (" about ", " om "):
            if splitter in text:
                return text.split(splitter)[-1].strip()
        for word in ("film", "movie"):
            if word in text:
                return text.split(word)[-1].strip()
        return text.strip()
