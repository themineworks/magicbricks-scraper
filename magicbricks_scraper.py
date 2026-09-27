#!/usr/bin/env python3
"""India property listings: price, BHK, area and locality. Python, Node.js and cURL clients for the MagicBricks Scraper on Apify, pay per result.

Command-line client for the themineworks/magicbricks-scraper actor on Apify: runs it, waits for it
to finish and saves every result as JSON and CSV. Flags map 1:1 to the actor's input.
Free Apify account and API token: https://console.apify.com/sign-up
Docs and pricing: https://themineworks.com/actors/magicbricks-scraper/
"""
import argparse, csv, json, os, sys
from apify_client import ApifyClient

ACTOR = "themineworks/magicbricks-scraper"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--token", default=os.environ.get("APIFY_TOKEN"), help="Apify API token (or set APIFY_TOKEN)")
    ap.add_argument("--out", default="results", help="Output basename, writes .json and .csv")
    ap.add_argument("--city", help="Indian city name, for example Bangalore, Mumbai, Pune")
    ap.add_argument("--listing-type", help="Whether to search rental or for-sale property listings on MagicBricks, for example RENT…")
    ap.add_argument("--bedrooms", help="Comma-separated. BHK counts to search, for example 2 and 3")
    ap.add_argument("--max-results", type=int, help="Maximum number of properties to return across all searched BHK counts")
    ap.add_argument("--allow-residential-fallback", action=argparse.BooleanOptionalAction, help="If a request fails on the default datacenter proxy, retry it once on Indian residential…")
    a = ap.parse_args()
    if not a.token:
        sys.exit("Provide --token or set APIFY_TOKEN. Free token: https://console.apify.com/sign-up")

    run_input = {}
    if a.city is not None: run_input["city"] = a.city
    if a.listing_type is not None: run_input["listingType"] = a.listing_type
    if a.bedrooms: run_input["bedrooms"] = [s.strip() for s in a.bedrooms.split(",") if s.strip()]
    if a.max_results is not None: run_input["maxResults"] = a.max_results
    if a.allow_residential_fallback is not None: run_input["allowResidentialFallback"] = a.allow_residential_fallback

    client = ApifyClient(a.token)
    print(f"Running {ACTOR} ...")
    run = client.actor(ACTOR).call(run_input=run_input)
    items = list(client.dataset(run["defaultDatasetId"]).iterate_items())

    with open(a.out + ".json", "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)
    keys = []
    for it in items:
        keys += [k for k in it if k not in keys]
    if items:
        with open(a.out + ".csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=keys, extrasaction="ignore")
            w.writeheader()
            for it in items:
                w.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v for k, v in it.items()})
    print(f"Done: {len(items)} results saved to {a.out}.json and {a.out}.csv")


if __name__ == "__main__":
    main()
