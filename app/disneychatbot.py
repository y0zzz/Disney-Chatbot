"""Core chatbot logic: routes a user message to the right answer source."""

from app.disneydata import COMPANY_FACTS, find_movie
from app.wiki import WikipediaHelper

FALLBACK_MESSAGE = (
    "I'm not sure how to answer that. Try asking about a Disney movie, "
    "or about the company's history, founder, or CEO."
)


class DisneyChatbot:
    def __init__(self, wiki_helper: WikipediaHelper | None = None):
        self.wiki_helper = wiki_helper or WikipediaHelper()

    def respond(self, user_input: str) -> str:
        if not user_input or not user_input.strip():
            return FALLBACK_MESSAGE

        text = user_input.lower()

        movie = find_movie(text)
        if movie:
            return f"{movie.title} was released on {movie.release_date}."

        for keyword, fact in COMPANY_FACTS.items():
            if keyword in text:
                return fact

        if "film" in text or "movie" in text:
            movie_name = self._extract_topic(text)
            if movie_name:
                return self.wiki_helper.get_summary(movie_name)

        if "company info" in text or "company history" in text or "history" in text:
            return self.wiki_helper.get_summary("The Walt Disney Company")

        return FALLBACK_MESSAGE

    @staticmethod
    def _extract_topic(text: str) -> str:
        for splitter in (" about ", " om "):
            if splitter in text:
                return text.split(splitter)[-1].strip()
        for word in ("film", "movie"):
            if word in text:
                return text.split(word)[-1].strip()
        return text.strip()
