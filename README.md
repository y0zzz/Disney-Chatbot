# Disney Chatbot

![Disney Chatbot demo](docs/demo.gif)

A small Q&A chatbot that answers questions about Disney movies and company trivia. Local facts answer instantly; anything else routes through a self-hosted LLM proxy ([llm-api](https://github.com/y0zzz/llm-api)), with a Wikipedia fallback if that's unavailable.

## Features

- Answers movie release-date questions (Lion King, Mulan, Aladdin + sequels)
- Answers company trivia (founding date, founders, current CEO)
- Falls back to an LLM for open-ended questions, then Wikipedia if the LLM is unreachable
- Fully typed, tested FastAPI backend
- Automated tests + Docker build on every push (GitHub Actions)

## Tech stack

- **FastAPI** — web framework
- **Pydantic** — request/response validation
- **httpx** — calls to the llm-api proxy
- **wikipedia-api** — Wikipedia fallback lookups
- **pytest / pytest-asyncio** — test suite
- **Docker** — containerized deployment

## Project structure

```
├── app/
│   ├── main.py            # FastAPI app + routes
│   ├── disneychatbot.py   # Routing logic
│   ├── disneydata.py      # Local knowledge base
│   ├── llm_client.py      # llm-api proxy client
│   ├── config.py          # Env var config
│   └── wiki.py            # Wikipedia fallback helper
├── tests/
│   └── test_main.py
├── .github/workflows/
│   └── ci.yml
├── Dockerfile
├── pytest.ini
├── requirements.txt
└── requirements-dev.txt
```

## Getting started

Install dependencies:

```
pip install -r requirements-dev.txt
```

(Optional) point it at your own llm-api proxy for open-ended answers:

```
export LLM_API_BASE_URL="http://localhost:8080"
export LLM_API_KEY="your-key-here"
```

Run the server:

```
uvicorn app.main:app --reload --port 5000
```

Try it out:

```
curl -X POST http://localhost:5000/chat -H "Content-Type: application/json" -d '{"message": "When was Disney founded?"}'
```

Run with Docker instead:

```
docker build -t disney-chatbot .
docker run -p 5000:5000 disney-chatbot
```

## Running tests

```
pytest -v
```

## API

| Endpoint | Method | Description |
|---|---|---|
| `/health` | GET | Health check |
| `/chat` | POST | Send `{"message": "..."}`, get `{"response": "..."}` back |

## Adding new facts

Add an entry to `app/disneydata.py` — no chatbot logic needs to change:

```
MovieFact("Encanto", "November 24, 2021", aliases=("encanto",))
```

## Roadmap

- [x] Modernize architecture (FastAPI, tests, CI)
- [x] LLM fallback via self-hosted llm-api proxy
- [ ] Add a lightweight chat frontend
- [ ] Deploy (Render + Vercel)
