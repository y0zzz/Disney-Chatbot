from unittest.mock import AsyncMock, MagicMock
 
import pytest
from fastapi.testclient import TestClient
 
from app.disneychatbot import FALLBACK_MESSAGE, DisneyChatbot
from app.main import app
 
 
@pytest.fixture
def client():
    return TestClient(app)
 
 
def _make_bot(llm_answer=None):
    """Build a DisneyChatbot with mocked wiki + LLM dependencies.
 
    llm_answer=None means the LLM is "unconfigured" (returns None),
    so behavior falls through to Wikipedia -- matching a real deployment
    that hasn't set LLM_API_BASE_URL / LLM_API_KEY yet.
    """
    fake_wiki = MagicMock()
    fake_wiki.get_summary.return_value = "A mocked wiki summary."
 
    fake_llm = MagicMock()
    fake_llm.ask = AsyncMock(return_value=llm_answer)
 
    return DisneyChatbot(wiki_helper=fake_wiki, llm_client=fake_llm), fake_wiki, fake_llm
 
 
# --- Local knowledge base tests (should never hit LLM or Wikipedia) --------
 
@pytest.mark.asyncio
async def test_lion_king_fact():
    bot, _, fake_llm = _make_bot()
    result = await bot.respond("When was The Lion King released?")
    assert "June 15, 1994" in result
    fake_llm.ask.assert_not_called()
 
 
@pytest.mark.asyncio
async def test_mulan_vs_mulan_2_disambiguation():
    bot, _, _ = _make_bot()
    assert "Mulan II" in await bot.respond("What year did Mulan 2 come out?")
    assert "Mulan was released" in await bot.respond("What year did Mulan come out?")
 
 
@pytest.mark.asyncio
async def test_aladdin_sequels_disambiguation():
    bot, _, _ = _make_bot()
    assert "Aladdin and the King of Thieves" in await bot.respond("aladdin 3 release date")
    assert "The Return of Jafar" in await bot.respond("aladdin 2 release date")
 
 
@pytest.mark.asyncio
async def test_company_founded():
    bot, _, _ = _make_bot()
    assert "October 16, 1923" in await bot.respond("When was Disney founded?")
 
 
@pytest.mark.asyncio
async def test_company_ceo():
    bot, _, _ = _make_bot()
    assert "Bob Iger" in await bot.respond("Who is the current CEO?")
 
 
# --- LLM fallback tests -----------------------------------------------------
 
@pytest.mark.asyncio
async def test_llm_answers_open_ended_question():
    bot, fake_wiki, fake_llm = _make_bot(llm_answer="Elsa's powers come from being born with them.")
    result = await bot.respond("Why does Elsa have ice powers?")
    assert result == "Elsa's powers come from being born with them."
    fake_llm.ask.assert_called_once()
    fake_wiki.get_summary.assert_not_called()
 
 
@pytest.mark.asyncio
async def test_wikipedia_used_when_llm_unavailable():
    bot, fake_wiki, fake_llm = _make_bot(llm_answer=None)
    result = await bot.respond("tell me about the film Coraline")
    fake_llm.ask.assert_called_once()
    fake_wiki.get_summary.assert_called_once()
    assert result == "A mocked wiki summary."
 
 
@pytest.mark.asyncio
async def test_empty_message_returns_fallback():
    bot, _, fake_llm = _make_bot()
    assert await bot.respond("") == FALLBACK_MESSAGE
    assert await bot.respond("   ") == FALLBACK_MESSAGE
    fake_llm.ask.assert_not_called()
 
 
@pytest.mark.asyncio
async def test_gibberish_falls_through_to_fallback_when_llm_unavailable():
    bot, _, _ = _make_bot(llm_answer=None)
    assert await bot.respond("asdkjfhaksjdhf") == FALLBACK_MESSAGE
 
 
# --- API-level tests ---------------------------------------------------------
 
def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
 
 
def test_chat_endpoint_known_fact(client):
    response = client.post("/chat", json={"message": "When was Disney founded?"})
    assert response.status_code == 200
    assert "1923" in response.json()["response"]
 
 
def test_chat_endpoint_rejects_empty_message(client):
    response = client.post("/chat", json={"message": ""})
    assert response.status_code == 422
 