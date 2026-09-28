# MagicBricks Scraper: India Property Prices & Rent Data

Scrape MagicBricks property listings across Indian cities: price, BHK, carpet area, project, locality, poster and listing date, for rent or sale. Parses the site structured data, no login, no browser, pay per property.

**Run it on Apify:** [apify.com/themineworks/magicbricks-scraper](https://apify.com/themineworks/magicbricks-scraper)
**Docs, FAQ and pricing:** [themineworks.com/actors/magicbricks-scraper](https://themineworks.com/actors/magicbricks-scraper/)

**Price:** From $0.60 per 1,000 properties on Apify's higher plans ($1.00 on the free plan), plus a $0.005 start fee per run. Failed and empty results are never charged.

## What it returns

* Rent or sale listings across any Indian city
* Price, BHK, carpet area and locality
* Project name, poster and listing date
* Parses schema.org structured data: no browser needed
* No login, pay per property

## Quick start

You need a free [Apify account](https://console.apify.com/sign-up) and its API token (Settings, API & Integrations).

### Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")
run = client.actor("themineworks/magicbricks-scraper").call(run_input={
    "city": "Bangalore",
    "listingType": "RENT",
    "bedrooms": [
        "2"
    ],
    "maxResults": 10
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
```

### Node.js

```bash
npm install apify-client
```

```javascript
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: 'YOUR_APIFY_TOKEN' });
const run = await client.actor('themineworks/magicbricks-scraper').call({
    "city": "Bangalore",
    "listingType": "RENT",
    "bedrooms": [
        "2"
    ],
    "maxResults": 10
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

### cURL

One request that runs the actor and returns the results in the response (for runs under 5 minutes):

```bash
curl -X POST "https://api.apify.com/v2/acts/themineworks~magicbricks-scraper/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"city": "Bangalore", "listingType": "RENT", "bedrooms": ["2"], "maxResults": 10}'
```

### Command line

This repo includes ready-made clients that save results to JSON and CSV:

```bash
python3 magicbricks_scraper.py --token YOUR_APIFY_TOKEN --city "Bangalore" --listing-type "RENT" --bedrooms "2" --max-results "10"
node magicbricks_scraper.mjs --token YOUR_APIFY_TOKEN --city "Bangalore" --listing-type "RENT" --bedrooms "2" --max-results "10"
```

## Input

| Field | Type | Default | Description |
|---|---|---|---|
| `city` | string | `"Bangalore"` | Indian city name, for example Bangalore, Mumbai, Pune |
| `listingType` | string | `"RENT"` | Whether to search rental or for-sale property listings on MagicBricks, for example RENT for flats to let or… |
| `bedrooms` | array | `["2"]` | BHK counts to search, for example 2 and 3 |
| `maxResults` | integer | `25` | Maximum number of properties to return across all searched BHK counts |
| `allowResidentialFallback` | boolean | `true` | If a request fails on the default datacenter proxy, retry it once on Indian residential before giving up |

## Output

One row per result, as JSON, CSV, Excel or through the API.

| Field | Type | Description |
|---|---|---|
| `property_id` | string |  |
| `title` | string |  |
| `listing_type` | string |  |
| `price` | integer |  |
| `bhk` | integer |  |
| `area_sqft` | integer |  |
| `project` | string |  |
| `locality` | string |  |
| `city` | string |  |
| `posted_by` | string |  |
| `listed_at` | string |  |
| `url` | string |  |
| `scraped_at` | string |  |

## Use it from an AI agent

The actor works as a tool in Claude, Cursor or any MCP client through Apify's MCP server:

```
https://mcp.apify.com/?tools=themineworks/magicbricks-scraper
```

## FAQ

### Does it cover both rent and sale?

Yes. Set the listing type to rent or sale. The actor returns the same structured fields for both.

### Do I need a login?

No. It reads each listing page's public structured data, so there is no login and no browser automation.

### What does it cost?

You pay per property returned and nothing for a search that finds none.

### What comes back per listing?

Price, BHK, carpet area, project name, locality, who posted it and the listing date.

### Does it cover rentals as well as sales?

Yes. Set the listing type to rent or sale and the same structured fields come back for both.

### How does it avoid using a browser?

It reads the structured data MagicBricks already publishes on each listing page, so no browser is needed and runs stay cheap.

### Can I target one locality rather than a whole city?

Yes. Searches accept a locality as well as a city, which is what you want when comparing a single micro market rather than an entire metro.

### Can I export the results to CSV or Excel?

Yes. Every run saves to an Apify dataset you can download as JSON, CSV, Excel or XML, or read through the API. The Python and Node clients in this repo also write the results to local files.

### Can I run it on a schedule?

Yes. Save your input as a task on Apify and attach a schedule, or call the API from your own cron job. Scheduled runs are billed the same way as manual ones.

## Related scrapers

* [B2B Leads Finder](https://themineworks.com/actors/b2b-leads-finder/): Business emails and LinkedIn profiles for target companies
* [LinkedIn Company Scraper](https://themineworks.com/actors/linkedin-company-details/): Company size, industry, website, and followers without login
* [Zillow Rental Listings Scraper](https://themineworks.com/actors/zillow-rental-listings/): Scrape Zillow for-rent listings by city or zip. $1 per 1,000 results

Part of [The Mine Works](https://themineworks.com/): 151 pay-per-result scrapers with no login and no browser setup on your side.

## License

MIT © The Mine Works
