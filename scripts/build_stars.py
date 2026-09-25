"""Write data/stars.json with star counts for every repo under the listed owners.

The file holds counts only, so a weekly run with no change produces no diff and no commit.

Runs in the weekly GitHub Action (uses the built-in GH_TOKEN via the gh CLI)
and can be run locally with `gh` logged in.
"""
import glob
import json
import re
import subprocess
import sys

OWNERS = ("BY571", "TorchTrade")

stars = {}
for owner in OWNERS:
    out = subprocess.check_output(
        ["gh", "api", f"users/{owner}/repos?per_page=100", "--paginate",
         "--jq", ".[] | [.full_name, .stargazers_count] | @tsv"],
        text=True,
    )
    for line in out.splitlines():
        name, n = line.split("\t")
        stars[name] = int(n)

data = dict(sorted(stars.items()))
data["_total"] = sum(stars.values())

with open("data/stars.json", "w") as f:
    json.dump(data, f, indent=1)
    f.write("\n")
print(f"{len(stars)} repos, {data['_total']} stars")

# A renamed repo would silently keep its hardcoded fallback count on the page; say so.
wanted = {m for f in glob.glob("*.html") for m in re.findall(r'data-repo="([^"]+)"', open(f).read())}
for key in sorted(wanted - set(stars)):
    print(f"::warning::data-repo {key} not found on GitHub; the page keeps its fallback count", file=sys.stderr)
