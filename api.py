import requests

def fetch_news(company):
    """Fetches news articles related to the given company."""
    API_KEY = "dc1947daddc4474c876bfa37a0ee77e4"  # Replace with your actual API key
    url = f'https://newsapi.org/v2/everything?q={company}&apiKey={API_KEY}'
    response = requests.get(url)
    articles = response.json().get('articles', [])
    return articles[:10]
