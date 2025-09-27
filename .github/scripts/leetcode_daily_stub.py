#!/usr/bin/env python3
import re
import json
from pathlib import Path

import requests
from tenacity import retry, stop_after_attempt, wait_exponential

REPO_ROOT = Path(__file__).resolve().parents[2]

LC_GRAPHQL = "https://leetcode.com/graphql"
DAILY_QUERY = """
query questionOfToday {
  activeDailyCodingChallengeQuestion {
    date
    link
    question {
      questionFrontendId
      title
      titleSlug
    }
  }
}
"""

@retry(wait=wait_exponential(multiplier=1, min=1, max=8), stop=stop_after_attempt(5))
def fetch_daily():
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "leetcode-daily-stub-action/1.0"
    }
    r = requests.post(LC_GRAPHQL, json={"query": DAILY_QUERY}, headers=headers, timeout=20)
    r.raise_for_status()
    j = r.json()
    if "errors" in j:
        raise RuntimeError(j["errors"])
    node = j["data"]["activeDailyCodingChallengeQuestion"]
    if not node:
        raise RuntimeError("No daily challenge returned")
    return node

def safe_title(title: str) -> str:
    t = re.sub(r"[^\w\s\-]", "", title)
    t = re.sub(r"\s+", " ", t).strip()
    return t

def main():
    node = fetch_daily()
    q = node["question"]
    qid = q["questionFrontendId"]
    title = safe_title(q["title"])
    filename = f"{qid}. {title}.py"

    path = REPO_ROOT / filename
    if path.exists():
        print(f"Already exists: {filename} — no overwrite.")
        return

    # Default placeholder
    path.write_text("File added, please replace this with the complete solution.\n", encoding="utf-8")

    print(json.dumps({"created": filename}, indent=2))

if __name__ == "__main__":
    main()
