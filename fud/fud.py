#!/usr/bin/env python3
"""fud — fetch the top Urban Dictionary definitions for a term.

Uses the community Urban Dictionary JSON API:
    https://api.urbandictionary.com/v0/define?term=<term>
"""

import json
import sys
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.urbandictionary.com/v0/define"
UA = "fud/1.0 (+https://github.com/tcaxias/fud)"
LIMIT = 5


def usage(prog):
    print(f"Usage: {prog} <term>")
    print(f"Example: {prog} fud")


def fetch(term):
    encoded = urllib.parse.quote(term)
    url = f"{API}?term={encoded}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main(argv):
    if len(argv) < 2:
        usage(argv[0])
        return 1

    term = argv[1]

    try:
        data = fetch(term)
    except urllib.error.HTTPError as exc:
        print(f"error: Urban Dictionary returned HTTP {exc.code}", file=sys.stderr)
        return 1
    except urllib.error.URLError as exc:
        print(f"error: could not reach Urban Dictionary: {exc.reason}", file=sys.stderr)
        return 1

    results = data.get("list", [])[:LIMIT]
    if not results:
        print(f"No Urban Dictionary definition found for: {term}")
        return 0

    for i, entry in enumerate(results, 1):
        word = entry.get("word", term)
        definition = (entry.get("definition") or "").strip()
        example = (entry.get("example") or "").strip()
        permalink = entry.get("permalink", "")

        print(f"{i}. {word}")
        print(f"   Definition: {definition}")
        if example:
            print(f"   Example: {example}")
        print(f"   {permalink}")
        print()

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
