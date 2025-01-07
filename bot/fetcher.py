import os
import logging
from config.settings import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, BEARER_TOKEN

import requests 

# Configure logging
logging.basicConfig(filename='logs/bot.log', level=logging.INFO, format='%(asctime)s %(message)s')

os.environ["CONSUMER_KEY"] = API_KEY
os.environ["CONSUMER_SECRET"] = API_SECRET_KEY
os.environ["BEARER_TOKEN"] = BEARER_TOKEN

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {BEARER_TOKEN}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

        
def fetch_tweets(count=10):
    """
    Fetch recent tweets from the accounts followed by the bot.

    Args:
        count (int): Maximum number of tweets to fetch (default: 100).

    Returns:
        list[dict]: A list of dictionaries containing tweet data.
    """
    try:
        
        logging.info("Connecting to X API")
        search_url = "https://api.twitter.com/2/tweets/search/recent"
        query_params = {'query': '(from:nearcyan)','tweet.fields': 'author_id'}
        response = requests.get(search_url, auth=bearer_oauth, params=query_params)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        
        return response.json()

    except Exception as e:
        logging.error(f"Error in fetch_tweets: {e}")
        return []
