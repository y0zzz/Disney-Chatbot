"""Wikipedia lookup helper, used as a fallback when nothing in the
local Disney knowledge base matches the question."""

import logging

import wikipediaapi

logger = logging.getLogger(__name__)

NOT_FOUND_MESSAGE = "I couldn't find any information about that on Wikipedia."


class WikipediaHelper:
    def __init__(self, user_agent: str = "DisneyChatbot/2.0 (https://github.com/y0zzz/Disney-Chatbot)"):
        self.wiki = wikipediaapi.Wikipedia(user_agent=user_agent, language="en")

    def get_summary(self, query: str, max_chars: int = 1000) -> str:
        query = query.strip()
        if not query:
            return NOT_FOUND_MESSAGE

        logger.debug("Looking up Wikipedia page for %r", query)
        page = self.wiki.page(query)

        if not page.exists():
            logger.debug("No Wikipedia page found for %r", query)
            return NOT_FOUND_MESSAGE

        logger.debug("Found Wikipedia page: %s", page.title)
        return page.summary[:max_chars]
