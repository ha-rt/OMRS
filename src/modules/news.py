from requests import get

COUNTRY_CODE = get("https://ipapi.co/json/").json().get("country")

def get_top_headlines(api_key: str):
    top_articles = get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}").json()
    
    if top_articles.get("status") != "ok":
        return []
    
    headlines = [article['title'] for article in top_articles.get('articles', [])]
    return headlines