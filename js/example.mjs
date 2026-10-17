// Run murch1k/google-trends-scraper and print the results. Usage: APIFY_TOKEN=... node example.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('murch1k/google-trends-scraper').call({"searchTerms": ["pickleball", "coffee, tea"], "geo": "", "timeRange": "today 12-m", "property": "web"});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) console.log(JSON.stringify({ type: item.type, searchTerms: item.searchTerms, geo: item.geo, timeRange: item.timeRange, averages: item.averages }));
