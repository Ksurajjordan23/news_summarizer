#Building an article or news summarizer
#install requests and newspaper3k library

#loading environment variables
import json
from dotenv import load_dotenv
load_dotenv()

#pick an article to generate a summary, fetch article using requests.
#extract title and text of article using newspaper libraby
import requests
from newspaper import Article

#enter your user-agent as a header
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

#insert your url here
article_url = "https://www.nbcnews.com/tech/tech-news/twitter-accuses-meta-stealing-trade-secrets-new-threads-app-rcna92946"

session = requests.Session()

try:
    response = session.get(article_url, headers= headers, timeout =10)

    if response.status_code == 200:
        article = Article(article_url)
        article.download()
        article.parse()

        print(f"Title: {article.title}")
        print(f"Text: {article.text}")

    else:
        print(f"Failed to fetch article at {article_url}")
except Exception as e:
    print(f"Error occurred while fetching article at{article_url}:{e}")
    
