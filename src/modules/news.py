from openai import OpenAI
from os import getenv
from utils.yaml import get_yaml_safely
from requests import get

SYSTEM_PROMPT = get_yaml_safely("config/systemprompts.yaml")["news"]
COUNTRY_CODE = get("https://ipapi.co/json/").json()["country"]

def get_news_as_json(client):
    pass

def get_news_as_summary(client: OpenAI):
    ai_response = client.responses.create(
        model="gpt-5",
        reasoning={"effort": "low"},
        instructions=SYSTEM_PROMPT,
        input="to be inputted",
    ).output_text
    
    return ai_response