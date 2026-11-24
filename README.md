# Targeted Ads Knowledge Base

A beginner-friendly knowledge base about targeted social media ads (Meta: Facebook / Instagram / Threads, plus TikTok), up to date as of November 2026.

**Live site:** https://rem700.github.io/target-kb/

Built with MkDocs Material. Three languages: Russian (default), English (`/en/`), Ukrainian (`/uk/`).

## Sections
1. Basics and numbers
2. Meta Ads Manager
3. Creatives
4. Tracking and attribution
5. Tests and problems
6. TikTok
7. Restrictions and moderation
8. Non-obvious things
9. Problem cases
10. Changelog of platform updates

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
- **New page:** create a file with the same name in all three folders (e.g. `10-google-ads.md`). The number at the start sets the menu order. The `# Heading` on the first line becomes the menu title.
- **No translation yet?** Put the file only in `docs/ru/`: other languages will show the Russian version in its place.
- **Platform changes** go to `99-changelog.md`, newest at the top.
- **Reliability tags:** (official) — from the platform's own help or blog; (practice) — specialists' experience, not confirmed by the platform; (own test).

## Local preview
```
pip install -r requirements.txt
mkdocs serve
```
Open http://127.0.0.1:8000
