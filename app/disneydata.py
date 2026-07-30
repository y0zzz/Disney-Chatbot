"""
Static Disney knowledge base.

Adding a new fact is just adding a new dict entry -- no chatbot logic
needs to change.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class MovieFact:
    title: str
    release_date: str
    aliases: tuple[str, ...] = ()


MOVIES: list[MovieFact] = [
    MovieFact("The Lion King", "June 15, 1994", aliases=("lion king",)),
    MovieFact("Mulan", "June 5, 1998", aliases=("mulan",)),
    MovieFact("Mulan II", "December 28, 2004", aliases=("mulan 2", "mulan ii")),
    MovieFact("Aladdin", "November 25, 1992", aliases=("aladdin 1", "aladdin")),
    MovieFact(
        "The Return of Jafar",
        "May 20, 1994",
        aliases=("aladdin 2", "return of jafar"),
    ),
    MovieFact(
        "Aladdin and the King of Thieves",
        "August 13, 1996",
        aliases=("aladdin 3", "king of thieves"),
    ),
]

COMPANY_FACTS: dict[str, str] = {
    "founded": "The Walt Disney Company was founded on October 16, 1923.",
    "founder": "The Walt Disney Company was founded by Walt Disney and Roy O. Disney.",
    "ceo": "The current CEO of The Walt Disney Company is Bob Iger.",
}


def find_movie(user_input: str) -> MovieFact | None:
    """Find a movie fact whose alias appears in the user's message."""
    text = user_input.lower()
    for movie in sorted(MOVIES, key=lambda m: -max(len(a) for a in m.aliases)):
        for alias in movie.aliases:
            if alias in text:
                return movie
    return None
