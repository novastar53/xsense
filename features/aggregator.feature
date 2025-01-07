Feature: Aggregate Tweets
  As a Twitter bot
  I want to aggregate tweets into structured data
  So that I can analyze user activity

  Scenario: Successfully aggregate tweets
    Given I have a list of tweets
    When I aggregate the tweets
    Then I should get a DataFrame with aggregated data
