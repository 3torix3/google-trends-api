# apify-google-trends

Google Trends data without the API: interest over time, interest by region, related and rising queries, keyword comparisons and Trending Now for any country.

```python
from apify_google_trends import get_trends
rows = get_trends({'searchTerms': ['pickleball', 'coffee, tea'], 'geo': '', 'timeRange': 'today 12-m', 'property': 'web'}, token="<APIFY_TOKEN>")
```

Runs [murch1k/google-trends-scraper](https://apify.com/murch1k/google-trends-scraper) on your Apify account.
