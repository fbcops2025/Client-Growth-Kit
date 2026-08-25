#!/usr/bin/env python3
"""Safe render of the canonical master from growth_kit.html.

Does NOT touch growth_kit.html. Reads it, renders to the canonical PDF,
regenerates previews, and prints a quick text check.
"""
import os
from playwright.sync_api import sync_playwright
import fitz

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = os.path.join(SCRIPT_DIR, "growth_kit.html")
PDF_PATH = os.path.join(SCRIPT_DIR, "WeForgeWeb_Client_Growth_Kit_System.pdf")


def render():
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        html = f.read()
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(html, wait_until="load")
        page.wait_for_timeout(1000)
        page.pdf(
            path=PDF_PATH,
            format="A4",
            print_background=True,
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
            prefer_css_page_size=True,
        )
        browser.close()
    print(f"Rendered PDF -> {PDF_PATH}")

    doc = fitz.open(PDF_PATH)
    print(f"Total PDF pages: {len(doc)}")
    preview_dir = os.path.join(SCRIPT_DIR, "pdf_previews")
    os.makedirs(preview_dir, exist_ok=True)
    for old in os.listdir(preview_dir):
        if old.endswith(".png"):
            os.remove(os.path.join(preview_dir, old))
    for i, pg in enumerate(doc):
        pix = pg.get_pixmap(dpi=150)
        pix.save(os.path.join(preview_dir, f"page_{i+1}.png"))
    print("Previews regenerated.")


if __name__ == "__main__":
    render()
