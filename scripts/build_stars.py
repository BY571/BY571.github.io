"""Write data/stars.json with star counts for every repo under the listed owners.

Runs in the weekly GitHub Action (uses the built-in GH_TOKEN via the gh CLI)
and can be run locally with `gh` logged in.
"""
import datetime
import json
import subprocess

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
data["_updated"] = datetime.date.today().isoformat()

with open("data/stars.json", "w") as f:
    json.dump(data, f, indent=1)
    f.write("\n")
print(f"{len(stars)} repos, {data['_total']} stars")
