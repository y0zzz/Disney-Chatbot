from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient

from app.disneychatbot import FALLBACK_MESSAGE, DisneyChatbot
from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def bot_with_fake_wiki():
    fake_wiki = MagicMock()
    fake_wiki.get_summary.return_value = "A mocked summary."
    return DisneyChatbot(wiki_helper=fake_wiki), fake_wiki


def test_lion_king_fact(bot_with_fake_wiki):
    bot, _ = bot_with_fake_wiki
    assert "June 15, 1994" in bot.respond("When was The Lion King released?")


def test_mulan_vs_mulan_2_disambiguation(bot_with_fake_wiki):
    bot, _ = bot_with_fake_wiki
    assert "Mulan II" in bot.respond("What year did Mulan 2 come out?")
    assert "Mulan was released" in bot.respond("What year did Mulan come out?")


def test_aladdin_sequels_disambiguation(bot_with_fake_wiki):
    bot, _ = bot_with_fake_wiki
    assert "Aladdin and the King of Thieves" in bot.respond("aladdin 3 release date")
    assert "The Return of Jafar" in bot.respond("aladdin 2 release date")


def test_company_founded(bot_with_fake_wiki):
    bot, _ = bot_with_fake_wiki
    assert "October 16, 1923" in bot.respond("When was Disney founded?")


def test_company_ceo(bot_with_fake_wiki):
    bot, _ = bot_with_fake_wiki
    assert "Bob Iger" in bot.respond("Who is the current CEO?")


def test_unknown_film_falls_back_to_wikipedia(bot_with_fake_wiki):
    bot, fake_wiki = bot_with_fake_wiki
    result = bot.respond("tell me about the film Encanto")
    fake_wiki.get_summary.assert_called_once()
    assert result == "A mocked summary."


def test_empty_message_returns_fallback(bot_with_fake_wiki):
    bot, _ = bot_with_fake_wiki
    assert bot.respond("") == FALLBACK_MESSAGE
    assert bot.respond("   ") == FALLBACK_MESSAGE


def test_gibberish_returns_fallback(bot_with_fake_wiki):
    bot, _ = bot_with_fake_wiki
    assert bot.respond("asdkjfhaksjdhf") == FALLBACK_MESSAGE


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
