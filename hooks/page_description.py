"""Fill page.meta['description'] from the first plain paragraph if a page has none.

Used for the <meta name="description"> tag and social previews (overrides/main.html).
"""
import re

SKIP = ("#", "!!!", "|", "-", "*", ">", "```", "1.", "<", "[", "--8<--")


def _clean(text: str) -> str:
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)          # images
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)      # links -> text
    text = re.sub(r"[*_`]+", "", text)                        # emphasis, code
    return re.sub(r"\s+", " ", text).strip()


def on_page_markdown(markdown, page, config, files):
    if page.meta.get("description"):
        return markdown
    for block in re.split(r"\n\s*\n", markdown):
        line = block.strip()
        if not line or line.startswith(SKIP):
            continue
        text = _clean(line)
        if len(text) < 40:
            continue
        if len(text) > 160:
            text = text[:157].rsplit(" ", 1)[0] + "…"
        page.meta["description"] = text
        break
    return markdown
