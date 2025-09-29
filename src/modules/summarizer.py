from openai import OpenAI
from utils.yaml import get_yaml_safely
from random import randint

SYSTEM_PROMPTS = get_yaml_safely("config/systemprompts.yaml")

def retrieve_random_bible_verse(client: OpenAI):
    ai_response = client.responses.create(
        model="gpt-5",
        reasoning={"effort": "low"},
        instructions=SYSTEM_PROMPTS["bible"],
        input=f"Choose a random important theme throughout the bible. Great, now give me a random Bible verse reference about said theme. It cannot include the number: {randint(100000, 10000000000)} in it.",
    ).output_text
    return ai_response

def get_news_as_summary(client: OpenAI, top_articles: list):
    articles_text = "\n".join(top_articles)
    ai_response = client.responses.create(
        model="gpt-5",
        reasoning={"effort": "low"},
        instructions=SYSTEM_PROMPTS["news"],
        input=articles_text,
    ).output_text
    return ai_response

def get_emails_as_summary(client: OpenAI, emails: list):
    emails_text = "\n".join(emails)
    ai_response = client.responses.create(
        model="gpt-5",
        reasoning={"effort": "low"},
        instructions=SYSTEM_PROMPTS["emails"],
        input=emails_text,
    ).output_text
    return ai_response

def get_calendar_as_summary(client: OpenAI, events: list):
    events_text = "\n".join(events)
    ai_response = client.responses.create(
        model="gpt-5",
        reasoning={"effort": "low"},
        instructions=SYSTEM_PROMPTS["calendar"],
        input=events_text,
    ).output_text
    return ai_response
