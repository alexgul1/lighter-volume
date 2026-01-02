#!/usr/bin/env python3
"""
Scraper for nado-python-sdk documentation from GitHub Pages.
Saves all pages to docs/sdk/ folder.

Usage:
    pip install requests beautifulsoup4
    python scrape_sdk_docs.py
"""

import os
import re
import time
from urllib.parse import urljoin, urlparse
from pathlib import Path

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://nadohq.github.io/nado-python-sdk/"
OUTPUT_DIR = "docs/sdk"
DELAY = 0.5  # seconds between requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}


def get_page(url: str) -> tuple[str, list[str]]:
    """Fetch page and extract content + links."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
    except Exception as e:
        print(f"  Error: {e}")
        return "", []

    soup = BeautifulSoup(resp.text, "html.parser")

    # Extract main content (Sphinx documentation)
    content_div = (
        soup.find("div", class_="document") or
        soup.find("div", class_="body") or
        soup.find("main") or
        soup.find("article") or
        soup.find("body")
    )

    content = ""
    if content_div:
        # Convert to markdown-like text
        content = extract_text(content_div)

    # Find all internal links
    links = []
    base_domain = urlparse(url).netloc
    for a in soup.find_all("a", href=True):
        href = a["href"]
        full_url = urljoin(url, href)
        parsed = urlparse(full_url)

        # Only internal links
        if parsed.netloc == base_domain:
            # Clean URL (remove anchors, normalize)
            clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
            if clean_url.endswith(".html") or clean_url.endswith("/"):
                if clean_url not in links:
                    links.append(clean_url)

    return content, links


def extract_text(element) -> str:
    """Extract readable text from HTML element."""
    lines = []

    for el in element.find_all(["h1", "h2", "h3", "h4", "p", "li", "pre", "code", "dt", "dd"]):
        if el.name == "h1":
            lines.append(f"\n# {el.get_text(strip=True)}\n")
        elif el.name == "h2":
            lines.append(f"\n## {el.get_text(strip=True)}\n")
        elif el.name == "h3":
            lines.append(f"\n### {el.get_text(strip=True)}\n")
        elif el.name == "h4":
            lines.append(f"\n#### {el.get_text(strip=True)}\n")
        elif el.name == "p":
            text = el.get_text(strip=True)
            if text:
                lines.append(f"\n{text}\n")
        elif el.name == "li":
            text = el.get_text(strip=True)
            if text:
                lines.append(f"- {text}")
        elif el.name == "pre":
            code = el.get_text()
            lines.append(f"\n```python\n{code}\n```\n")
        elif el.name == "dt":
            text = el.get_text(strip=True)
            if text:
                lines.append(f"\n**{text}**")
        elif el.name == "dd":
            text = el.get_text(strip=True)
            if text:
                lines.append(f"  {text}")

    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def url_to_filename(url: str) -> str:
    """Convert URL to filename."""
    parsed = urlparse(url)
    path = parsed.path.strip("/")

    if not path or path.endswith("/"):
        path = "index"

    # Remove .html extension
    path = re.sub(r"\.html$", "", path)

    # Replace slashes
    path = path.replace("/", "_")

    # Clean up
    path = re.sub(r"[^a-zA-Z0-9_-]", "_", path)
    path = re.sub(r"_+", "_", path)

    return f"{path}.md"


def scrape_docs():
    """Scrape all SDK documentation."""
    output_path = Path(OUTPUT_DIR)
    output_path.mkdir(parents=True, exist_ok=True)

    visited = set()
    to_visit = [BASE_URL]
    saved = 0

    print(f"Scraping {BASE_URL}")
    print(f"Output: {output_path.absolute()}")
    print("-" * 50)

    while to_visit:
        url = to_visit.pop(0)

        if url in visited:
            continue

        visited.add(url)
        print(f"[{saved + 1}] {url}")

        content, links = get_page(url)

        if content:
            filename = url_to_filename(url)
            filepath = output_path / filename

            # Add URL as header
            full_content = f"---\nurl: {url}\n---\n\n{content}"

            filepath.write_text(full_content, encoding="utf-8")
            print(f"  -> {filename} ({len(content)} chars)")
            saved += 1
        else:
            print(f"  -> skipped (no content)")

        # Add new links
        for link in links:
            if link not in visited and link not in to_visit:
                # Only follow links within sdk docs
                if "nado-python-sdk" in link:
                    to_visit.append(link)

        time.sleep(DELAY)

    print("-" * 50)
    print(f"Done! Saved {saved} pages to {output_path}")

    # Create index
    index_path = output_path / "_INDEX.md"
    index = "# SDK Documentation Index\n\n"
    for url in sorted(visited):
        filename = url_to_filename(url)
        index += f"- [{url}](./{filename})\n"
    index_path.write_text(index, encoding="utf-8")
    print(f"Index: {index_path}")


if __name__ == "__main__":
    scrape_docs()
