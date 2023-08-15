import requests
from sys import argv

API_KEY = 'yourkullanıcıadı'

URL = 'https://newsapi.org/v2/top-headlines?'

def get_articles_by_category(category):
    query_parameters = {
        "category": category,
        "sortBy": "top",
        "country": "tr",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

def get_articles_by_query(query):
    query_parameters = {
        "q": query,
        "sortBy": "top",
        "country": "tr",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

def _get_articles(params):
    response = requests.get(URL, params=params)
    articles = response.json()['articles']
    results = []
    for article in articles:
        results.append({"title": article["title"], "url": article["url"]})
    for result in results:
        print(result['title'])
        print(result['url'])
        print('')

def get_sources_by_category(category):
    url = 'https://newsapi.org/v2/top-headlines/sources'
    query_parameters = {
        "category": category,
        "language": "tr",
        "apiKey": API_KEY
    }
    response = requests.get(url, params=query_parameters)
    sources = response.json()['sources']
    for source in sources:
        print(source['name'])
        print(source['url'])

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python script_name.py category_or_query")
        exit()

    option = argv[1]

    if option == 'sources':
        category = argv[2] if len(argv) > 2 else 'technology'
        get_sources_by_category(category)
    else:
        print(f"Getting news for {option}...\n")
        get_articles_by_category(option)
        print(f"Successfully retrieved top {option} headlines")
