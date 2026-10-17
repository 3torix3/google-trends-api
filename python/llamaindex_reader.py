"""LlamaIndex: actor results -> Documents (pip install llama-index-readers-apify). Usage: APIFY_TOKEN=... python llamaindex_reader.py"""
import json
import os

from llama_index.core import Document
from llama_index.readers.apify import ApifyActor

reader = ApifyActor(os.environ["APIFY_TOKEN"])
docs = reader.load_data(
    actor_id="murch1k/google-trends-scraper",
    run_input={'searchTerms': ['pickleball', 'coffee, tea'], 'geo': '', 'timeRange': 'today 12-m', 'property': 'web'},
    dataset_mapping_function=lambda item: Document(
        text=json.dumps(item.get("relatedQueries") or {}),
        metadata={"type": item.get("type"), "searchTerms": item.get("searchTerms"), "geo": item.get("geo"), "timeRange": item.get("timeRange"), "averages": item.get("averages")},
    ),
)
print(len(docs), "documents")
