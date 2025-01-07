import json

from bot.fetcher import fetch_tweets
# from bot.aggregator import aggregate_data
# # from bot.follower_logic import follow_accounts
# from bot.reporter import generate_report
# import time
import logging

# Configure logging
logging.basicConfig(filename='logs/bot.log', level=logging.INFO, format='%(asctime)s %(message)s')

def run_bot():
    logging.info("Starting the bot...")
    
    # Step 1: Fetch tweets
    tweets = fetch_tweets()
    pretty_json = json.dumps(tweets, indent=4, sort_keys=True)

    logging.info(pretty_json)


    
    # Step 2: Aggregate data
    # aggregated_data = aggregate_data(tweets)
    
    # Step 3: Follow new accounts
    # follow_accounts()
    
    # Step 4: Generate report
    # generate_report(aggregated_data)
    
    logging.info("Bot run completed.")

if __name__ == "__main__":
    run_bot()
