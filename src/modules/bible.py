from requests import get

def get_verse_of_the_day(verse):
    url = f"https://bible-api.com/{verse.replace(' ', '+')}"
    response = get(url)
    if response.status_code != 200:
        return "Failed to fetch verse.", verse
    data = response.json()
    verse_text = data.get("text", "Verse not found").replace("\n", " ").strip()
    reference = data.get("reference", verse)
    return verse_text, reference