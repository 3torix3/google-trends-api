"""Thin client for the Apify actor torix33/google-trends-scraper."""
import os
from typing import Any, Dict, List, Optional

from apify_client import ApifyClient

ACTOR_ID = "torix33/google-trends-scraper"
__version__ = "0.1.0"


def get_trends(run_input: Dict[str, Any], token: Optional[str] = None, max_total_charge_usd: Optional[float] = None) -> List[Dict[str, Any]]:
    """Run the actor and return its dataset rows. token defaults to the APIFY_TOKEN env variable."""
    client = ApifyClient(token or os.environ["APIFY_TOKEN"])
    run = client.actor(ACTOR_ID).call(run_input=run_input, max_total_charge_usd=max_total_charge_usd)
    return list(client.dataset(run["defaultDatasetId"]).iterate_items())
