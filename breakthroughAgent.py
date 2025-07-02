import json
import requests
from datetime import datetime


def fetch_breakthroughs(query, limit=5):
    url = f"https://hn.algolia.com/api/v1/search?query={query}"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    hits = data.get('hits', [])[:limit]
    return [(h.get('title'), h.get('url')) for h in hits]


def update_log(entries, log_file="BreakthroughLog.md"):
    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')
    with open(log_file, 'a') as f:
        f.write(f"\n## {now}\n")
        for title, url in entries:
            if url:
                f.write(f"- [{title}]({url})\n")
            else:
                f.write(f"- {title}\n")


def main():
    keywords = ["breakthrough", "shattering", "unheard of"]
    all_entries = []
    for kw in keywords:
        try:
            entries = fetch_breakthroughs(kw)
            all_entries.extend(entries)
        except Exception as e:
            print(f"Error fetching {kw}: {e}")
    if all_entries:
        update_log(all_entries)


if __name__ == "__main__":
    main()
