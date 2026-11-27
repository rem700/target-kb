"""SEO post-processing: absolute hreflang links with x-default, JSON-LD structured data."""
import json
import re
from urllib.parse import urljoin

ALT = re.compile(r'<link rel="alternate" href="([^"]+)" hreflang="([a-z-]+)">')
LANG_ROOT = {"ru": "", "en": "en/", "uk": "uk/"}


def _lang(page):
    url = page.url or ""
    for code in ("en", "uk"):
        if url == f"{code}/" or url.startswith(f"{code}/"):
            return code
    return "ru"


def on_post_page(output, page, config):
    base = page.canonical_url or config["site_url"]
    links = {}

    def absolutize(match):
        href, lang = match.group(1), match.group(2)
        full = urljoin(base, href)
        links[lang] = full
        return f'<link rel="alternate" href="{full}" hreflang="{lang}">'

    output = ALT.sub(absolutize, output)
    if "ru" in links and 'hreflang="x-default"' not in output:
        tag = f'<link rel="alternate" href="{links["ru"]}" hreflang="x-default">'
        output = output.replace("</head>", f"  {tag}\n  </head>", 1)

    lang = _lang(page)
    site_url = config["site_url"].rstrip("/") + "/"
    home = site_url + LANG_ROOT[lang]
    site_name = config.get("site_name", "")
    desc = page.meta.get("description", "")
    graph = [{
        "@type": "WebSite",
        "@id": home + "#website",
        "url": home,
        "name": site_name,
        "inLanguage": lang,
        "publisher": {"@type": "Organization", "name": site_name, "url": home},
    }]
    if not page.is_homepage and page.url not in LANG_ROOT.values():
        modified = page.meta.get("git_revision_date_localized_raw_iso_date")
        article = {
            "@type": "TechArticle",
            "@id": page.canonical_url + "#article",
            "headline": page.title,
            "description": desc,
            "inLanguage": lang,
            "url": page.canonical_url,
            "isPartOf": {"@id": home + "#website"},
            "publisher": {"@type": "Organization", "name": site_name, "url": home},
            "image": f"{site_url}assets/og/og-{lang}.png",
        }
        if modified:
            article["dateModified"] = modified
        graph.append(article)
        crumbs = [{"@type": "ListItem", "position": 1, "name": site_name, "item": home}]
        if page.parent is not None and page.parent.title:
            crumbs.append({"@type": "ListItem", "position": 2, "name": page.parent.title})
        crumbs.append({"@type": "ListItem", "position": len(crumbs) + 1, "name": page.title,
                       "item": page.canonical_url})
        graph.append({"@type": "BreadcrumbList", "itemListElement": crumbs})
    data = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)
    script = f'<script type="application/ld+json">{data}</script>'
    return output.replace("</head>", f"  {script}\n  </head>", 1)
