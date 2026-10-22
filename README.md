# Google Trends API alternative — interest, related queries, Trending Now (Python, JS, LangChain, n8n)

Google Trends data without the API: interest over time, interest by region, related and rising queries, keyword comparisons and Trending Now for any country.

Runs on the Apify actor **[torix33/google-trends-scraper](https://apify.com/torix33/google-trends-scraper)** — pay per result, no subscription. This repo has copy-paste
examples for Python, JavaScript, LangChain, LlamaIndex, n8n.

## Numbers (measured 2026-10-15)

| | |
|---|---|
| Price | **$3.00 per 1,000 results** ($0.003 per result) |
| Cloud test, 40 runs (random country / period / property) | 40/40 runs succeeded, 36/40 with full interest-over-time data (2026-10-15) |

## Quick start

```bash
export APIFY_TOKEN=...            # https://console.apify.com/settings/integrations
pip install apify-client && python python/example.py
# or
cd js && npm install && node example.mjs
```

```python
from apify_client import ApifyClient
client = ApifyClient("<APIFY_TOKEN>")
run = client.actor("torix33/google-trends-scraper").call(run_input={'searchTerms': ['pickleball', 'coffee, tea'], 'geo': '', 'timeRange': 'today 12-m', 'property': 'web'})
rows = list(client.dataset(run["defaultDatasetId"]).iterate_items())
```

## Output

One row per keyword group (`type: "explore"`): `searchTerms`, `geo`, `timeRange`, `property`, `interestOverTime`, `averages`, `interestByRegion`, `relatedQueries`, `relatedTopics`, `status` (`ok` / `no_data`), `exploreUrl`, `scrapedAt`. Trending Now rows (`type: "trending"`) carry `rank`, `title`, `approxTraffic`, `publishedAt`.

## LangChain / LlamaIndex

- [`python/langchain_loader.py`](python/langchain_loader.py) — `langchain-apify` `ApifyWrapper` → `Document`s (`page_content` = `exploreUrl`).
- [`python/llamaindex_reader.py`](python/llamaindex_reader.py) — `llama-index-readers-apify` `ApifyActor` reader.

## n8n

Import [`n8n/workflow.json`](n8n/workflow.json) (Workflows → Import from file). It calls the actor's
`run-sync-get-dataset-items` endpoint; add a Header Auth credential `Authorization: Bearer <APIFY_TOKEN>`.

## Packages (not on PyPI/npm yet)

[`packages/python`](packages/python) (`apify-google-trends` → `get_trends()`) and [`packages/npm`](packages/npm) (`apify-google-trends` → `getTrends()`):
thin wrappers around `apify-client`.

## Limitations

- One row per keyword group ("coffee, tea" compares the two terms in one row) plus one row per Trending Now topic.
- Google shows no data for very small keywords; such rows come back with status "no_data" and are not charged.
- Google rate-limits datacenter IPs: from a datacenter/VPS IP a run can end with 0 rows; the Apify cloud runs use the Apify proxy.

## License

MIT. The data comes from public sources; use it in line with their terms and applicable law.
