#!/usr/bin/env python3
"""
GitBook documentation scraper for nado.xyz
Saves all pages as markdown files to docs/ folder
"""

import os
import re
import time
import argparse
from urllib.parse import urljoin, urlparse
from pathlib import Path

import requests
from bs4 import BeautifulSoup

# Default GitBook URL - change this to actual nado docs URL
DEFAULT_BASE_URL = "https://docs.nado.xyz"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}


def get_page_content(url: str, session: requests.Session) -> tuple[str, str, list[str]]:
    """Fetch page and extract title, content, and links."""
    try:
        resp = session.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"  Error fetching {url}: {e}")
        return "", "", []

    soup = BeautifulSoup(resp.text, "html.parser")

    # Extract title
    title = ""
    title_tag = soup.find("h1") or soup.find("title")
    if title_tag:
        title = title_tag.get_text(strip=True)

    # Extract main content (GitBook specific selectors)
    content_selectors = [
        "main",
        "[data-testid='page.contentEditor']",
        ".markdown-body",
        "article",
        ".content",
        "#content",
    ]

    content = ""
    for selector in content_selectors:
        content_div = soup.select_one(selector)
        if content_div:
            content = extract_markdown(content_div)
            break

    if not content:
        # Fallback: get body text
        body = soup.find("body")
        if body:
            content = extract_markdown(body)

    # Extract internal links
    links = []
    base_domain = urlparse(url).netloc
    for a in soup.find_all("a", href=True):
        href = a["href"]
        full_url = urljoin(url, href)
        parsed = urlparse(full_url)

        # Only internal links, no anchors only
        if parsed.netloc == base_domain and parsed.path and parsed.path != "/":
            clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
            if clean_url not in links:
                links.append(clean_url)

    return title, content, links


def extract_markdown(element) -> str:
    """Convert HTML element to markdown-like text."""
    lines = []

    for child in element.descendants:
        if child.name == "h1":
            lines.append(f"\n# {child.get_text(strip=True)}\n")
        elif child.name == "h2":
            lines.append(f"\n## {child.get_text(strip=True)}\n")
        elif child.name == "h3":
            lines.append(f"\n### {child.get_text(strip=True)}\n")
        elif child.name == "h4":
            lines.append(f"\n#### {child.get_text(strip=True)}\n")
        elif child.name == "p":
            text = child.get_text(strip=True)
            if text:
                lines.append(f"\n{text}\n")
        elif child.name == "li":
            text = child.get_text(strip=True)
            if text:
                lines.append(f"- {text}")
        elif child.name == "pre" or child.name == "code":
            if child.parent.name != "pre":  # Avoid duplicates
                code = child.get_text()
                if "\n" in code:
                    lines.append(f"\n```\n{code}\n```\n")
                else:
                    lines.append(f"`{code}`")
        elif child.name == "a" and child.get("href"):
            text = child.get_text(strip=True)
            href = child.get("href")
            if text and not text.startswith("http"):
                lines.append(f"[{text}]({href})")

    # Clean up
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def url_to_filename(url: str, base_url: str) -> str:
    """Convert URL path to filename."""
    parsed = urlparse(url)
    path = parsed.path.strip("/")

    if not path:
        return "index.md"

    # Replace slashes with underscores
    filename = path.replace("/", "_")
    # Clean up
    filename = re.sub(r"[^a-zA-Z0-9_-]", "_", filename)
    filename = re.sub(r"_+", "_", filename)

    return f"{filename}.md"


def scrape_gitbook(base_url: str, output_dir: str, delay: float = 1.0, max_pages: int = 100):
    """Scrape all pages from GitBook documentation."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    session = requests.Session()

    visited = set()
    to_visit = [base_url]
    pages_saved = 0

    print(f"Starting scrape of {base_url}")
    print(f"Output directory: {output_path.absolute()}")
    print(f"Max pages: {max_pages}, Delay: {delay}s")
    print("-" * 50)

    while to_visit and pages_saved < max_pages:
        url = to_visit.pop(0)

        if url in visited:
            continue

        visited.add(url)
        print(f"[{pages_saved + 1}/{max_pages}] Fetching: {url}")

        title, content, links = get_page_content(url, session)

        if content:
            filename = url_to_filename(url, base_url)
            filepath = output_path / filename

            # Add frontmatter
            markdown = f"---\nurl: {url}\ntitle: {title}\n---\n\n{content}"

            filepath.write_text(markdown, encoding="utf-8")
            print(f"  Saved: {filename} ({len(content)} chars)")
            pages_saved += 1
        else:
            print(f"  Skipped: no content")

        # Add new links to queue
        for link in links:
            if link not in visited and link not in to_visit:
                to_visit.append(link)

        time.sleep(delay)

    print("-" * 50)
    print(f"Done! Saved {pages_saved} pages to {output_path.absolute()}")

    # Create index file
    index_path = output_path / "_INDEX.md"
    index_content = "# Scraped Documentation Index\n\n"
    for url in sorted(visited):
        filename = url_to_filename(url, base_url)
        index_content += f"- [{url}](./{filename})\n"
    index_path.write_text(index_content, encoding="utf-8")
    print(f"Index saved to {index_path}")


def main():
    parser = argparse.ArgumentParser(description="Scrape GitBook documentation")
    parser.add_argument(
        "url",
        nargs="?",
        default=DEFAULT_BASE_URL,
        help=f"Base URL of GitBook docs (default: {DEFAULT_BASE_URL})"
    )
    parser.add_argument(
        "-o", "--output",
        default="docs",
        help="Output directory (default: docs)"
    )
    parser.add_argument(
        "-d", "--delay",
        type=float,
        default=1.0,
        help="Delay between requests in seconds (default: 1.0)"
    )
    parser.add_argument(
        "-m", "--max-pages",
        type=int,
        default=100,
        help="Maximum pages to scrape (default: 100)"
    )

    args = parser.parse_args()

    scrape_gitbook(args.url, args.output, args.delay, args.max_pages)


if __name__ == "__main__":
    main()
