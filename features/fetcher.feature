Feature: Fetch Tweets
  As a Twitter bot
  I want to fetch tweets from followed accounts
  So that I can aggregate and analyze them

  Scenario: Successfully fetch tweets
    Given the Twitter API is accessible
    When I fetch tweets
    Then I should receive a list of tweets
