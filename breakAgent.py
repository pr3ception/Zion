import json
import requests
from datetime import datetime


def fetchBreakthroughs(query, limit=5):
    url = f"https://hn.algolia.com/api/v1/search?query={query}"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    hits = data.get('hits', [])[:limit]
    return [(h.get('title'), h.get('url')) for h in hits]


def updateLog(entries, logFile="BreakthroughLog.md"):
    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')
    with open(logFile, 'a') as f:
        f.write(f"\n## {now}\n")
        for title, url in entries:
            if url:
                f.write(f"- [{title}]({url})\n")
            else:
                f.write(f"- {title}\n")


def main():
    keywords = ["breakthrough", "shattering", "unheard of"]
    allEntries = []
    for kw in keywords:
        try:
            entries = fetchBreakthroughs(kw)
            allEntries.extend(entries)
        except Exception as e:
            print(f"Error fetching {kw}: {e}")
    if allEntries:
        updateLog(allEntries)


if __name__ == "__main__":
    main()
