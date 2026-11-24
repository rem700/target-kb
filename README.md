# Targeted Ads Knowledge Base

A beginner-friendly knowledge base about targeted social media ads (Meta: Facebook / Instagram / Threads, plus TikTok), up to date as of November 2026.

**Live site:** https://rem700.github.io/target-kb/

Built with MkDocs Material. Three languages: Russian (default), English (`/en/`), Ukrainian (`/uk/`).

## Sections
- **Getting started:** basics and numbers, glossary, choosing a platform, setting up from scratch, payment/invoices/taxes
- **Launching ads:** Meta Ads Manager, creatives, copywriting formulas, landing pages, click-to-chat ads, tracking, TikTok
- **Growth and analysis:** tests and problems, benchmarks, seasonal calendar, organic + paid, non-obvious things
- **Practice:** a full example campaign, playbooks by business type, templates, problem cases
- **Rules:** restrictions and moderation, law and transparency (EU)
- **What's new:** changelog of platform updates

Every page ends with a **Sources** list and a "Checked" date. Abbreviations (CPM, CTR, CAPI…) show a tooltip on hover.

## Structure
```
docs/ru/   — Russian version (main)
docs/en/   — English
docs/uk/   — Ukrainian
mkdocs.yml — site settings
.github/workflows/deploy.yml — automatic publishing to GitHub Pages
```
File names are the same in all three folders, so the language switcher opens the same page in another language.

## Publishing
Every push to `main` rebuilds and publishes the site automatically (1–2 minutes). Progress is visible in the Actions tab. GitHub Pages source is set to **GitHub Actions** (Settings → Pages).

## How to add content
- **Edit a page:** change the `.md` file in `docs/ru/`, then make the same change in `docs/en/` and `docs/uk/`.
- **New page:** create a file with the same name in all three folders (e.g. `google-ads.md`) and add it to the `nav` section in `mkdocs.yml` (menu groups are translated via `nav_translations`). The `# Heading` on the first line becomes the menu title. End the page with a `## Sources` list, a "Checked" date and the tooltip include line, e.g. `--8<-- "abbr-en.md"` (tooltip texts live in `includes/`).
- **No translation yet?** Put the file only in `docs/ru/`: other languages will show the Russian version in its place.
- **Platform changes** go to `99-changelog.md`, newest at the top.
- **Reliability tags:** (official) — from the platform's own help or blog; (practice) — specialists' experience, not confirmed by the platform; (own test).

## Local preview
```
pip install -r requirements.txt
mkdocs serve
```
Open http://127.0.0.1:8000
