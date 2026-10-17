// Thin client for the Apify actor murch1k/google-trends-scraper.
import { ApifyClient } from 'apify-client';

export const ACTOR_ID = 'murch1k/google-trends-scraper';

/** Run the actor and return its dataset rows. token defaults to process.env.APIFY_TOKEN. */
export async function getTrends(input, { token = process.env.APIFY_TOKEN, maxTotalChargeUsd } = {}) {
    const client = new ApifyClient({ token });
    const run = await client.actor(ACTOR_ID).call(input, maxTotalChargeUsd ? { maxTotalChargeUsd } : {});
    const { items } = await client.dataset(run.defaultDatasetId).listItems();
    return items;
}
