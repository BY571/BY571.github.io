# by571.github.io

Personal site of Sebastian Dittert, served by GitHub Pages from the root of `master`.
Plain HTML, one stylesheet, one small script. No build step.

## Layout

```
index.html                 publications, talks, project areas, articles
rl.html                    reinforcement learning projects and repositories
robotics.html              robotics projects, videos, gallery
llms.html                  LLM projects
agentic-automation.html    agent projects
assets/style.css           shared styles; light tokens on :root, dark under [data-theme="dark"]
assets/site.js             theme toggle, star counts, click-to-load YouTube embeds
data/stars.json            cached GitHub star counts (refreshed weekly by the workflow)
scripts/build_stars.py     regenerates data/stars.json (needs `gh` logged in)
media/                     images
```

## Editing

- Add a publication: copy one `<li class="pub">` block in `index.html`.
- Add a project: copy one `<article class="card">` block on the matching subpage.
- Add a repository to the RL page: copy one `<a class="repo">` block; the `data-repo`
  attribute must be `owner/name` so the star count is filled from `data/stars.json`.
- Embed a video: copy one `<a class="yt" ...>` block from `robotics.html` and replace the video ID
  in all three places (href, `data-id`, thumbnail URL). The player loads only after a click.

## Theme

Light by default. Dark mode follows the OS preference unless the toggle stored a choice
in `localStorage`. The inline script in each page's `<head>` applies the theme before
first paint.

## Star counts

`.github/workflows/stars.yml` runs every Monday (or on demand from the Actions tab),
rebuilds `data/stars.json`, and commits it if anything changed. To refresh locally:

```
python3 scripts/build_stars.py
```

## Preview locally

```
python3 -m http.server 8765
```
