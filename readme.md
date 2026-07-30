# Disney Chatbot

A small Q&A chatbot that answers questions about Disney movies and company trivia, with a Wikipedia fallback for anything outside its local knowledge base.

Originally built as a simple Flask rule-based bot; rebuilt on FastAPI with a proper structure, a real test suite, and a working CI pipeline.

# Features

* Answers movie release-date questions (Lion King, Mulan, Aladdin + sequels)
* Answers company trivia (founding date, founders, CEO)
* Falls back to a live Wikipedia summary for anything else
* Fully typed, tested FastAPI backend 

# Project structure

├── app/
│   ├── __init__.py
│   ├── main.py            # FastAPI app + routes
│   ├── disneychatbot.py   # Routing logic
│   ├── disneydata.py      # Local knowledge base (movies, company facts)
│   └── wiki.py            # Wikipedia fallback helper
├── tests/
│   └── test_main.py
├── Dockerfile
├── requirements.txt
├── requirements-dev.txt
└── .github/workflows/ci.yml

# Running locally

pip install -r requirements-dev.txt
uvicorn app.main:app --reload --port 5000

Then:

curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "When was Disney founded?"}'

  # Running with Docker
  
  docker build -t disney-chatbot .
docker run -p 5000:5000 disney-chatbot

# Running tests

pytest -v

# Adding new facts
Add a MovieFact to app/disneydata.py — no chatbot logic needs to change:

MovieFact("Encanto", "November 24, 2021", aliases=("encanto",))

# Roadmap

 Swap keyword matching for LLM-based intent handling (e.g. via a self-hosted llm-api proxy)
 Add a lightweight chat frontend
 Deploy (Render + Vercel)