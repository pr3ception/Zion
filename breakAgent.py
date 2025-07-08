import json
import os
import requests
from datetime import datetime, timedelta


def fetchBreakthroughs(query, limit=5, days=7):
    """Return recent stories from Hacker News containing the query string."""
    cutoff = int((datetime.utcnow() - timedelta(days=days)).timestamp())
    url = (
        "https://hn.algolia.com/api/v1/search_by_date"
        f"?query={query}&tags=story&numericFilters=created_at_i%3E{cutoff}"
    )
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    hits = data.get("hits", [])[:limit]
    return [(h.get("title"), h.get("url")) for h in hits]


def updateLog(entries, logFile="BrkThrLOG.md"):
    """Append unique entries to the log with a timestamp."""
    seen = set()
    if os.path.exists(logFile):
        with open(logFile, "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith("- "):
                    seen.add(line)

    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    new_lines = []
    for title, url in entries:
        if url:
            line = f"- [{title}]({url})"
        else:
            line = f"- {title}"
        if line not in seen:
            new_lines.append(line)
            seen.add(line)

    if not new_lines:
        return

    with open(logFile, "a") as f:
        f.write(f"\n## {now}\n")
        for line in new_lines:
            f.write(line + "\n")


def main():
    keywords = ["breakthrough", "shattering", "unheard of"]
    allEntries = []
    for kw in keywords:
        try:
            entries = fetchBreakthroughs(kw, days=30)
            allEntries.extend(entries)
        except Exception as e:
            print(f"Error fetching {kw}: {e}")
    if allEntries:
        updateLog(allEntries)


if __name__ == "__main__":
    main()
