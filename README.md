Disney Chatbot

A small Q&A chatbot that answers questions about Disney movies and company trivia, with a live Wikipedia fallback for anything outside its local knowledge base.

Originally built as a simple Flask app with hardcoded rules; rebuilt on FastAPI with a proper package structure, a real test suite, and a working CI pipeline.

Features
Answers movie release-date questions (Lion King, Mulan, Aladdin + sequels)
Answers company trivia (founding date, founders, current CEO)
Falls back to a live Wikipedia summary for anything else
Fully typed, tested FastAPI backend
Automated tests + Docker build on every push (GitHub Actions)
Tech stack
FastAPI — web framework
Pydantic — request/response validation
wikipedia-api — Wikipedia fallback lookups
pytest — test suite
Docker — containerized deployment

Project structure

├── app/
│   ├── main.py            # FastAPI app + routes
│   ├── disneychatbot.py   # Routing logic
│   ├── disneydata.py      # Local knowledge base (movies, company facts)
│   └── wiki.py            # Wikipedia fallback helper
├── tests/
│   └── test_main.py       # Test suite
├── .github/workflows/
│   └── ci.yml             # CI: runs tests + builds Docker image
├── Dockerfile
├── requirements.txt
└── requirements-dev.txt

Getting started

Install dependencies:
pip install -r requirements-dev.txt

Run the server:
uvicorn app.main:app --reload --port 5000

Try it out:
docker build -t disney-chatbot .
docker run -p 5000:5000 disney-chatbot

Run with Docker instead:
docker build -t disney-chatbot .
docker run -p 5000:5000 disney-chatbot

Running tests
pytest -v

API
Endpoint	Method	Description
/health	GET	Health check
/chat	POST	Send {"message": "..."}, get {"response": "..."} back

Adding new facts

Add an entry to app/disneydata.py — no chatbot logic needs to change:

MovieFact("Encanto", "November 24, 2021", aliases=("encanto",))

Roadmap

 Swap keyword matching for LLM-based intent handling via a self-hosted llm-api proxy
 Add a lightweight chat frontend
 Deploy (Render + Vercel)


