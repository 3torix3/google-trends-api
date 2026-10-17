"""LangChain: actor results -> Documents (pip install langchain-apify). Usage: APIFY_TOKEN=... python langchain_loader.py"""
import json

from langchain_apify import ApifyWrapper
from langchain_core.documents import Document

loader = ApifyWrapper().call_actor(
    actor_id="murch1k/google-trends-scraper",
    run_input={'searchTerms': ['pickleball', 'coffee, tea'], 'geo': '', 'timeRange': 'today 12-m', 'property': 'web'},
    dataset_mapping_function=lambda item: Document(
        page_content=json.dumps(item.get("relatedQueries") or {}),
        metadata={"type": item.get("type"), "searchTerms": item.get("searchTerms"), "geo": item.get("geo"), "timeRange": item.get("timeRange"), "averages": item.get("averages")},
    ),
)
docs = loader.load()
print(len(docs), "documents;", docs[0].metadata if docs else None)
