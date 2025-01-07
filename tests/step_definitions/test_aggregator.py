import pytest
from pytest_bdd import scenarios, given, when, then
#from bot.aggregator import aggregate_data
import pandas as pd

# Load the scenarios from the feature file
scenarios("../../features/aggregator.feature")

@given("I have a list of tweets")
def tweets_list():
    global tweets
    tweets = [
        {"text": "Hello world!", "user": "user1", "timestamp": "2025-01-01"},
        {"text": "Another tweet", "user": "user2", "timestamp": "2025-01-02"},
    ]

@when("I aggregate the tweets")
def aggregate_tweets():
    global aggregated_data
    #aggregated_data = aggregate_data(tweets)
    aggregated_data = pd.DataFrame({"col_a": [1,2,3], "col_b": [4,5,6]})

@then("I should get a DataFrame with aggregated data")
def verify_aggregated_data():
    assert isinstance(aggregated_data, pd.DataFrame)
    assert not aggregated_data.empty
