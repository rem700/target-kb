"""Checks that every language has the same pages and that every page is in the nav.

Run: python scripts/check_structure.py  (exits with code 1 on problems)
"""
import pathlib
import sys

import yaml


class _Loader(yaml.SafeLoader):
    pass


# mkdocs.yml contains !!python/name tags; treat them as plain strings here.
_Loader.add_multi_constructor("tag:yaml.org,2002:python/", lambda loader, suffix, node: None)

ROOT = pathlib.Path(__file__).resolve().parent.parent
LANGS = ["ru", "en", "uk"]
CHECKED = {"ru": "Проверено:", "en": "Checked:", "uk": "Перевірено:"}


def nav_files(items):
    for item in items:
        if isinstance(item, str):
            yield item
        elif isinstance(item, dict):
            for value in item.values():
                yield from nav_files(value if isinstance(value, list) else [value])


def main() -> int:
    config = yaml.load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"), Loader=_Loader)
    in_nav = set(nav_files(config.get("nav", [])))
    problems = []

    pages = {lang: {p.name for p in (ROOT / "docs" / lang).glob("*.md")} for lang in LANGS}
    all_pages = set().union(*pages.values())
    for lang in LANGS:
        for missing in sorted(all_pages - pages[lang]):
            problems.append(f"[{lang}] missing translation: {missing}")
        for page in sorted(pages[lang]):
            text = (ROOT / "docs" / lang / page).read_text(encoding="utf-8")
            if CHECKED[lang] not in text:
                problems.append(f"[{lang}] {page}: no '{CHECKED[lang]}' date line")
            if f'--8<-- "abbr-{lang}.md"' not in text:
                problems.append(f"[{lang}] {page}: tooltip include line missing")
    for page in sorted(all_pages - in_nav):
        problems.append(f"not in nav (mkdocs.yml): {page}")
    for page in sorted(in_nav - all_pages):
        problems.append(f"in nav but no file: {page}")

    for line in problems:
        print("✗", line)
    if not problems:
        print(f"✓ structure OK: {len(all_pages)} pages × {len(LANGS)} languages, all in nav")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
