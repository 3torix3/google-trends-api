"""Run murch1k/google-trends-scraper and print the results. Usage: APIFY_TOKEN=... python example.py"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("murch1k/google-trends-scraper").call(run_input={'searchTerms': ['pickleball', 'coffee, tea'], 'geo': '', 'timeRange': 'today 12-m', 'property': 'web'})
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(json.dumps(item, ensure_ascii=False)[:300])
