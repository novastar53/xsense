import pytest
import logging
from pytest_bdd import scenarios, given, when, then
from bot.fetcher import fetch_tweets

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load the scenarios from the feature file
scenarios("../../features/fetcher.feature")

@given("the Twitter API is accessible")
def twitter_api_accessible():
    # In a real test, mock the Twitter API connection here
    assert True  # Assume API is accessible for this test

@when("I fetch tweets")
def fetch_tweets_action():
    global tweets
    tweets = fetch_tweets()
    logger.info(tweets)

@then("I should receive a list of tweets")
def verify_tweets():
    assert isinstance(tweets, list)
    assert all("text" in tweet for tweet in tweets)
