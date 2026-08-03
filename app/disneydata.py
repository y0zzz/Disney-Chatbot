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
    # Golden Age (1937-1942)
    MovieFact("Snow White and the Seven Dwarfs", "December 21, 1937", aliases=("snow white",)),
    MovieFact("Pinocchio", "February 7, 1940", aliases=("pinocchio",)),
    MovieFact("Fantasia 2000", "January 1, 2000", aliases=("fantasia 2000",)),
    MovieFact("Fantasia", "November 13, 1940", aliases=("fantasia",)),
    MovieFact("Dumbo", "October 23, 1941", aliases=("dumbo",)),
    MovieFact("Bambi", "August 13, 1942", aliases=("bambi",)),
 
    # Silver Age (1950-1967)
    MovieFact("Cinderella", "February 15, 1950", aliases=("cinderella",)),
    MovieFact("Alice in Wonderland", "July 28, 1951", aliases=("alice in wonderland",)),
    MovieFact("Peter Pan", "February 5, 1953", aliases=("peter pan",)),
    MovieFact("Lady and the Tramp", "June 22, 1955", aliases=("lady and the tramp",)),
    MovieFact("Sleeping Beauty", "January 29, 1959", aliases=("sleeping beauty",)),
    MovieFact("101 Dalmatians", "January 25, 1961", aliases=("101 dalmatians", "one hundred and one dalmatians")),
    MovieFact("The Jungle Book", "October 18, 1967", aliases=("jungle book",)),
 
    # Disney Renaissance (1989-1999)
    MovieFact("The Little Mermaid", "November 17, 1989", aliases=("little mermaid",)),
    MovieFact("Beauty and the Beast", "November 22, 1991", aliases=("beauty and the beast",)),
    MovieFact("Aladdin", "November 25, 1992", aliases=("aladdin 1", "aladdin")),
    MovieFact("The Return of Jafar", "May 20, 1994", aliases=("aladdin 2", "return of jafar")),
    MovieFact("Aladdin and the King of Thieves", "August 13, 1996", aliases=("aladdin 3", "king of thieves")),
    MovieFact("The Lion King", "June 15, 1994", aliases=("lion king",)),
    MovieFact("Pocahontas", "June 23, 1995", aliases=("pocahontas",)),
    MovieFact("Toy Story 2", "November 24, 1999", aliases=("toy story 2",)),
    MovieFact("Toy Story", "November 22, 1995", aliases=("toy story",)),
    MovieFact("The Hunchback of Notre Dame", "June 21, 1996", aliases=("hunchback of notre dame",)),
    MovieFact("Hercules", "June 27, 1997", aliases=("hercules",)),
    MovieFact("Mulan II", "December 28, 2004", aliases=("mulan 2", "mulan ii")),
    MovieFact("Mulan", "June 5, 1998", aliases=("mulan",)),
    MovieFact("A Bug's Life", "November 25, 1998", aliases=("bug's life", "bugs life")),
 
    # 2000s
    MovieFact("Dinosaur", "May 19, 2000", aliases=("dinosaur",)),
    MovieFact("The Emperor's New Groove", "December 15, 2000", aliases=("emperor's new groove", "emperors new groove")),
    MovieFact("Atlantis: The Lost Empire", "June 15, 2001", aliases=("atlantis",)),
    MovieFact("Monsters, Inc.", "November 2, 2001", aliases=("monsters inc", "monsters, inc")),
    MovieFact("Lilo & Stitch", "June 21, 2002", aliases=("lilo & stitch", "lilo and stitch", "lilo")),
    MovieFact("Treasure Planet", "November 27, 2002", aliases=("treasure planet",)),
    MovieFact("Finding Nemo", "May 30, 2003", aliases=("finding nemo",)),
    MovieFact("Brother Bear", "November 1, 2003", aliases=("brother bear",)),
    MovieFact("Incredibles 2", "June 15, 2018", aliases=("incredibles 2",)),
    MovieFact("The Incredibles", "November 5, 2004", aliases=("incredibles",)),
    MovieFact("Cars 2", "June 24, 2011", aliases=("cars 2",)),
    MovieFact("Cars", "June 9, 2006", aliases=("cars",)),
    MovieFact("Ratatouille", "June 29, 2007", aliases=("ratatouille",)),
    MovieFact("WALL-E", "June 27, 2008", aliases=("wall-e", "walle")),
    MovieFact("Bolt", "November 21, 2008", aliases=("bolt",)),
 
    # 2010s
    MovieFact("The Princess and the Frog", "December 11, 2009", aliases=("princess and the frog",)),
    MovieFact("Toy Story 3", "June 18, 2010", aliases=("toy story 3",)),
    MovieFact("Tangled", "November 24, 2010", aliases=("tangled",)),
    MovieFact("Brave", "June 22, 2012", aliases=("brave",)),
    MovieFact("Wreck-It Ralph", "November 2, 2012", aliases=("wreck-it ralph", "wreck it ralph")),
    MovieFact("Monsters University", "June 21, 2013", aliases=("monsters university",)),
    MovieFact("Frozen II", "November 22, 2019", aliases=("frozen ii", "frozen 2")),
    MovieFact("Frozen", "November 27, 2013", aliases=("frozen",)),
    MovieFact("Big Hero 6", "November 7, 2014", aliases=("big hero 6", "big hero six")),
    MovieFact("Inside Out", "June 19, 2015", aliases=("inside out",)),
    MovieFact("Zootopia", "March 4, 2016", aliases=("zootopia",)),
    MovieFact("Finding Dory", "June 17, 2016", aliases=("finding dory",)),
    MovieFact("Moana", "November 23, 2016", aliases=("moana",)),
    MovieFact("Coco", "November 22, 2017", aliases=("coco",)),
    MovieFact("Ralph Breaks the Internet", "November 21, 2018", aliases=("ralph breaks the internet",)),
    MovieFact("Toy Story 4", "June 21, 2019", aliases=("toy story 4",)),
 
    # 2020s
    MovieFact("Onward", "March 6, 2020", aliases=("onward",)),
    MovieFact("Soul", "December 25, 2020", aliases=("soul",)),
    MovieFact("Raya and the Last Dragon", "March 5, 2021", aliases=("raya",)),
    MovieFact("Luca", "June 18, 2021", aliases=("luca",)),
    MovieFact("Encanto", "November 24, 2021", aliases=("encanto",)),
    MovieFact("Turning Red", "March 11, 2022", aliases=("turning red",)),
    MovieFact("Lightyear", "June 17, 2022", aliases=("lightyear",)),
    MovieFact("Strange World", "November 23, 2022", aliases=("strange world",)),
    MovieFact("Elemental", "June 16, 2023", aliases=("elemental",)),
    MovieFact("Wish", "November 22, 2023", aliases=("wish",)),
]
 
COMPANY_FACTS: dict[str, str] = {
    "founded": "The Walt Disney Company was founded on October 16, 1923.",
    "founder": "The Walt Disney Company was founded by Walt Disney and Roy O. Disney.",
    "ceo": "The current CEO of The Walt Disney Company is Bob Iger.",
    "headquarters": "The Walt Disney Company is headquartered in Burbank, California.",
    "stock": "The Walt Disney Company trades on the NYSE under the ticker symbol DIS.",
    "ticker": "The Walt Disney Company trades on the NYSE under the ticker symbol DIS.",
    "pixar": "Disney acquired Pixar Animation Studios in 2006.",
    "marvel": "Disney acquired Marvel Entertainment in 2009.",
    "lucasfilm": "Disney acquired Lucasfilm (and the Star Wars franchise) in 2012.",
}
 

def find_movie(user_input: str) -> MovieFact | None:
    """Find a movie fact whose alias appears in the user's message."""
    text = user_input.lower()
    # Sort so more specific aliases (e.g. "aladdin 2") are checked before
    # shorter ones (e.g. "aladdin"), avoiding false positives.
    for movie in sorted(MOVIES, key=lambda m: -max(len(a) for a in m.aliases)):
        for alias in movie.aliases:
            if alias in text:
                return movie
    return None
 