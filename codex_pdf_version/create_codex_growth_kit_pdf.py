#!/usr/bin/env python3
"""
Codex-built premium PDF version of the We Forge Web Client Growth Kit.

This file intentionally does not reuse the previous HTML/CSS generator. It uses
ReportLab directly and references only assets copied into codex_pdf_version.
"""

from __future__ import annotations

import os
from pathlib import Path

import fitz
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
PREVIEWS = ROOT / "previews"
OUTPUT = ROOT / "WeForgeWeb_Client_Growth_Kit_Codex_Premium_Playbook.pdf"
LOGO = ASSETS / "weforgeweb-logo.png"

W, H = A4
M = 46


COLORS = {
    "ink": colors.HexColor("#111827"),
    "text": colors.HexColor("#374151"),
    "muted": colors.HexColor("#6B7280"),
    "line": colors.HexColor("#DADCE0"),
    "soft": colors.HexColor("#F5F7FA"),
    "blue": colors.HexColor("#0071E3"),
    "blue_soft": colors.HexColor("#EAF4FF"),
    "cyan": colors.HexColor("#00A4D6"),
    "orange": colors.HexColor("#FF6B35"),
    "orange_soft": colors.HexColor("#FFF4EC"),
    "green": colors.HexColor("#10B981"),
    "green_soft": colors.HexColor("#ECFDF5"),
    "red": colors.HexColor("#EF4444"),
    "red_soft": colors.HexColor("#FEF2F2"),
    "navy": colors.HexColor("#111827"),
    "white": colors.white,
}


def register_fonts() -> tuple[str, str, str]:
    fonts_dir = Path("C:/Windows/Fonts")
    regular = fonts_dir / "segoeui.ttf"
    bold = fonts_dir / "segoeuib.ttf"
    italic = fonts_dir / "segoeuii.ttf"
    if regular.exists() and bold.exists():
        pdfmetrics.registerFont(TTFont("WF-Regular", str(regular)))
        pdfmetrics.registerFont(TTFont("WF-Bold", str(bold)))
        if italic.exists():
            pdfmetrics.registerFont(TTFont("WF-Italic", str(italic)))
        else:
            pdfmetrics.registerFont(TTFont("WF-Italic", str(regular)))
        return "WF-Regular", "WF-Bold", "WF-Italic"
    return "Helvetica", "Helvetica-Bold", "Helvetica-Oblique"


FONT, BOLD, ITALIC = register_fonts()


def sw(text: str, font: str, size: float) -> float:
    return pdfmetrics.stringWidth(text, font, size)


def wrap_text(text: str, font: str, size: float, max_width: float) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = f"{current} {word}".strip()
        if not current or sw(trial, font, size) <= max_width:
            current = trial
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def para(c: canvas.Canvas, text: str, x: float, y: float, max_width: float, *,
         font: str = FONT, size: float = 9.2, leading: float = 12.4,
         color=COLORS["text"], max_lines: int | None = None) -> float:
    c.setFont(font, size)
    c.setFillColor(color)
    lines = wrap_text(text, font, size, max_width)
    if max_lines is not None:
        lines = lines[:max_lines]
    for line in lines:
        c.drawString(x, y, line)
        y -= leading
    return y


def label(c: canvas.Canvas, text: str, x: float, y: float, *,
          fill=COLORS["blue_soft"], stroke=colors.HexColor("#BBD7FF"),
          color=COLORS["blue"]) -> None:
    c.setFont(BOLD, 8.6)
    width = sw(text.upper(), BOLD, 8.6) + 22
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.roundRect(x, y - 7, width, 18, 6, fill=1, stroke=1)
    c.setFillColor(color)
    c.drawString(x + 11, y - 1.7, text.upper())


def card(c: canvas.Canvas, x: float, y: float, w: float, h: float, *,
         fill=colors.white, stroke=COLORS["line"], radius: float = 8,
         accent=None, accent_side: str = "left") -> None:
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.roundRect(x, y, w, h, radius, fill=1, stroke=1)
    if accent:
        c.setFillColor(accent)
        if accent_side == "left":
            c.roundRect(x, y, 4, h, radius, fill=1, stroke=0)
        elif accent_side == "top":
            c.roundRect(x, y + h - 4, w, 4, radius, fill=1, stroke=0)


def heading(c: canvas.Canvas, text: str, x: float, y: float, size: float = 20,
            color=COLORS["ink"]) -> float:
    c.setFont(BOLD, size)
    c.setFillColor(color)
    c.drawString(x, y, text)
    return y - size - 4


def header(c: canvas.Canvas, section: str, page_num: int) -> None:
    c.setFillColor(colors.white)
    c.rect(0, H - 56, W, 56, fill=1, stroke=0)
    c.setStrokeColor(COLORS["line"])
    c.line(0, H - 56, W, H - 56)
    c.drawImage(ImageReader(str(LOGO)), M, H - 38, width=28, height=28, mask="auto")
    c.setFont(BOLD, 13.5)
    c.setFillColor(COLORS["ink"])
    c.drawString(M + 38, H - 24, "WE FORGE")
    c.setFillColor(COLORS["blue"])
    c.drawString(M + 111, H - 24, "WEB")
    c.setFont(BOLD, 7.8)
    c.setFillColor(COLORS["muted"])
    c.drawString(M + 38, H - 40, section.upper())
    badge_w = sw(section.upper(), BOLD, 8) + 28
    c.setFillColor(COLORS["soft"])
    c.setStrokeColor(COLORS["line"])
    c.roundRect(W - M - badge_w, H - 39, badge_w, 22, 7, fill=1, stroke=1)
    c.setFillColor(COLORS["text"])
    c.setFont(BOLD, 8)
    c.drawCentredString(W - M - badge_w / 2, H - 31, section.upper())

    c.setFillColor(COLORS["soft"])
    c.rect(0, 0, W, 30, fill=1, stroke=0)
    c.setStrokeColor(COLORS["line"])
    c.line(0, 30, W, 30)
    c.setFont(BOLD, 8)
    c.setFillColor(COLORS["ink"])
    c.drawString(M, 12, "We Forge Web - Client Growth Kit")
    c.drawCentredString(W / 2, 12, "weforgeweb.com")
    c.setFillColor(COLORS["blue"])
    c.drawRightString(W - M, 12, f"Page {page_num} of 7")


def title_block(c: canvas.Canvas, tag: str, title: str, subtitle: str, y: float) -> float:
    label(c, tag, M, y)
    y -= 28
    y = heading(c, title, M, y, 19)
    y = para(c, subtitle, M, y + 6, W - 2 * M, size=9.7, leading=13,
             color=COLORS["muted"])
    return y - 8


def mini_metric(c: canvas.Canvas, x: float, y: float, w: float, h: float,
                title: str, body: str, accent) -> None:
    card(c, x, y, w, h, fill=colors.white, accent=accent, accent_side="top")
    c.setFont(BOLD, 8.8)
    c.setFillColor(accent)
    title_y = y + h - 20 if h >= 44 else y + h - 17
    body_y = y + h - 35 if h >= 44 else y + h - 30
    body_lines = 1 if h < 44 else 2
    c.drawString(x + 10, title_y, title)
    para(c, body, x + 10, body_y, w - 20, size=7.6, leading=9.5,
         color=COLORS["muted"], max_lines=body_lines)


def two_column_item(c: canvas.Canvas, x: float, y: float, label_text: str,
                    body: str, max_body_width: float) -> float:
    c.setFillColor(COLORS["soft"])
    c.setStrokeColor(COLORS["line"])
    c.circle(x + 6, y - 1, 5.5, fill=1, stroke=1)
    c.setFont(BOLD, 9)
    c.setFillColor(COLORS["text"])
    c.drawString(x + 20, y - 4, label_text)
    para(c, body, x + 112, y - 4, max_body_width + 8, size=8.35, leading=10.6,
         color=COLORS["text"], max_lines=2)
    return y - 27


def cover(c: canvas.Canvas) -> None:
    c.setFillColor(colors.HexColor("#F7FAFF"))
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(colors.HexColor("#EAF4FF"))
    c.circle(-50, H - 80, 190, fill=1, stroke=0)
    c.drawImage(ImageReader(str(LOGO)), M, H - 92, width=42, height=42, mask="auto")
    c.setFont(BOLD, 21)
    c.setFillColor(COLORS["ink"])
    c.drawString(M + 54, H - 66, "WE FORGE")
    c.setFillColor(COLORS["blue"])
    c.drawString(M + 166, H - 66, "WEB")
    c.setFont(BOLD, 8)
    c.setFillColor(COLORS["muted"])
    c.drawString(M + 54, H - 84, "BUILT TO AUTOMATE - FORGED TO LAST")
    label(c, "Codex Premium Playbook", W - M - 158, H - 69)

    y = H - 205
    label(c, "Client Acquisition & Revenue Infrastructure", M, y)
    y -= 42
    c.setFont(BOLD, 32)
    c.setFillColor(COLORS["ink"])
    c.drawString(M, y, "CLIENT GROWTH KIT")
    y -= 38
    c.setFont(BOLD, 29)
    c.setFillColor(COLORS["blue"])
    c.drawString(M, y, "Connected Acquisition System")
    y -= 30
    y = para(
        c,
        "A premium execution guide for building a connected client-acquisition machine: Facebook Ads, Google Business Profile, conversion website, proof assets, follow-up, and revenue tracking working as one system.",
        M,
        y,
        W - 2 * M,
        size=11,
        leading=15,
        color=COLORS["text"],
    )

    y -= 16
    card(c, M, y - 96, W - 2 * M, 96, fill=colors.white)
    c.setFont(BOLD, 10)
    c.setFillColor(COLORS["blue"])
    c.drawString(M + 14, y - 22, "THE 4 OPERATING PILLARS")
    pillar_w = (W - 2 * M - 42) / 4
    px = M + 14
    for num, title, body, accent in [
        ("01", "Foundation", "Profiles, website, proof, and contact paths ready before ads.", COLORS["orange"]),
        ("02", "Attention", "Targeted reach through paid social and search capture.", COLORS["cyan"]),
        ("03", "Trust Hub", "A website and GBP that answer doubts before clients call.", COLORS["blue"]),
        ("04", "Flywheel", "Finished jobs become reusable proof assets.", COLORS["green"]),
    ]:
        mini_metric(c, px, y - 83, pillar_w, 50, f"{num}. {title}", body, accent)
        px += pillar_w + 7

    y -= 126
    stages = ["Demand", "Proof", "Inquiry", "Estimate", "Revenue"]
    card(c, M, y - 54, W - 2 * M, 54, fill=COLORS["navy"], stroke=COLORS["navy"])
    sx = M + 34
    gap = (W - 2 * M - 68) / 4
    for i, stage in enumerate(stages, 1):
        c.setFillColor([COLORS["orange"], COLORS["cyan"], colors.HexColor("#3B82F6"), colors.HexColor("#F59E0B"), COLORS["green"]][i - 1])
        c.circle(sx, y - 20, 10, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont(BOLD, 8)
        c.drawCentredString(sx, y - 23, str(i))
        c.drawCentredString(sx, y - 42, stage)
        if i < 5:
            c.setFillColor(COLORS["cyan"])
            c.setFont(BOLD, 10)
            c.drawCentredString(sx + gap / 2, y - 24, "->")
        sx += gap

    y -= 84
    for x, title, body in [
        (M, "Turnkey Setup", "Built as a deployable client-acquisition system, not a loose list of tactics."),
        (M + 171, "Measurable Pipeline", "Tracks inquiry source, lead quality, estimates sent, close rate, and ROI."),
        (M + 342, "Owned Assets", "Domain, pages, proof assets, and customer data stay tied to the client business."),
    ]:
        card(c, x, y - 62, 158, 62, fill=colors.white)
        c.setFont(BOLD, 9)
        c.setFillColor(COLORS["orange"])
        c.drawString(x + 11, y - 19, title)
        para(c, body, x + 11, y - 34, 136, size=7.8, leading=10, color=COLORS["muted"])

    c.setStrokeColor(COLORS["line"])
    c.line(M, 72, W - M, 72)
    c.setFont(BOLD, 10)
    c.setFillColor(COLORS["ink"])
    c.drawString(M, 48, "WE FORGE WEB - CLIENT ACQUISITION TEAM")
    c.setFont(FONT, 8.6)
    c.setFillColor(COLORS["muted"])
    c.drawRightString(W - M, 48, "weforgeweb.com    +63 991 917 3652    hello@weforgeweb.com")
    c.showPage()


def page_strategy(c: canvas.Canvas) -> None:
    header(c, "Core Strategy & Architecture", 2)
    y = title_block(
        c,
        "Strategic Foundation",
        "Why one platform is too risky",
        "Client growth becomes predictable when attention, trust, follow-up, and measurement are connected instead of scattered.",
        H - 105,
    )
    col_w = (W - 2 * M - 12) / 2
    card(c, M, y - 150, col_w, 150, fill=COLORS["red_soft"], accent=COLORS["red"])
    c.setFont(BOLD, 10.5)
    c.setFillColor(colors.HexColor("#991B1B"))
    c.drawString(M + 14, y - 23, "DISCONNECTED & RISKY")
    yy = y - 48
    for a, b in [
        ("Algorithmic luck", "Reach disappears when organic Facebook slows down."),
        ("No trust hub", "Customers dig through old posts to understand the service."),
        ("Lost searchers", "High-intent Google users never find a convincing profile."),
        ("No follow-up", "Interested people disappear without value nurturing."),
    ]:
        yy = two_column_item(c, M + 14, yy, a + ":", b, col_w - 148)

    x2 = M + col_w + 12
    card(c, x2, y - 150, col_w, 150, fill=COLORS["green_soft"], accent=COLORS["green"])
    c.setFont(BOLD, 10.5)
    c.setFillColor(colors.HexColor("#047857"))
    c.drawString(x2 + 14, y - 23, "CONNECTED SYSTEM")
    yy = y - 48
    for a, b in [
        ("Lead capture", "Google and website capture attention created by ads."),
        ("Decision page", "Portfolio, testimonials, and credentials reduce doubt."),
        ("Local search", "GBP makes urgent buyers find and call faster."),
        ("ROI tracking", "Budget moves toward the best source of closed deals."),
    ]:
        yy = two_column_item(c, x2 + 14, yy, a + ":", b, col_w - 148)

    y -= 176
    c.setFont(BOLD, 11)
    c.setFillColor(COLORS["ink"])
    c.drawString(M, y, "CONNECTED LEAD ENGINE")
    y -= 64
    px = M
    for title, body, accent in [
        ("Online Foundation", "Facebook Page, Google Profile, and conversion landing page.", COLORS["blue"]),
        ("Targeted Reach", "Paid ads shown to the right market in the right service area.", COLORS["orange"]),
        ("Decision Engine", "Website and proof assets that make contact feel safe.", colors.HexColor("#3B82F6")),
        ("Asset Flywheel", "Every finished project becomes reusable trust content.", COLORS["green"]),
    ]:
        mini_metric(c, px, y, (W - 2 * M - 24) / 4, 55, title, body, accent)
        px += (W - 2 * M - 24) / 4 + 8

    y -= 35
    card(c, M, y - 75, W - 2 * M, 75, fill=COLORS["soft"])
    c.setFont(BOLD, 10)
    c.setFillColor(COLORS["ink"])
    c.drawString(M + 12, y - 19, "PIPELINE ECONOMICS SAMPLE")
    metric_w = (W - 2 * M - 54) / 4
    px = M + 12
    for top, bottom in [
        ("100 inquiries", "Ads and Google"),
        ("40 qualified", "Budget and area match"),
        ("20 estimates", "Detailed proposals"),
        ("8-12 closed", "High-ROI growth"),
    ]:
        card(c, px, y - 62, metric_w, 28, fill=colors.white, stroke=colors.HexColor("#BBD7FF"))
        c.setFont(BOLD, 8.4)
        c.setFillColor(COLORS["blue"])
        c.drawCentredString(px + metric_w / 2, y - 45, top)
        c.setFont(FONT, 7.3)
        c.setFillColor(COLORS["muted"])
        c.drawCentredString(px + metric_w / 2, y - 56, bottom)
        px += metric_w + 10

    y -= 105
    card(c, M, y - 56, W - 2 * M, 56, fill=COLORS["navy"], stroke=COLORS["navy"])
    c.setFont(BOLD, 10)
    c.setFillColor(COLORS["cyan"])
    c.drawString(M + 13, y - 20, "NORTH STAR: QUALIFIED LEADS AND CLOSED PROJECTS")
    para(c, "The goal is not likes. The goal is the right person seeing proof, trusting faster, contacting with intent, receiving a clear estimate, and becoming revenue.", M + 13, y - 36, W - 2 * M - 140, size=8.2, leading=11, color=colors.white)
    label(c, "Predictable Growth", W - M - 136, y - 28, fill=COLORS["orange"], stroke=COLORS["orange"], color=colors.white)
    c.showPage()


def page_foundation(c: canvas.Canvas) -> None:
    header(c, "Phase 1: Foundation & Demand", 3)
    y = H - 105
    y = heading(c, "Step 1: Prepare the online foundation before ads", M, y, 17)
    y = para(c, "Before spending on reach, the business must look legitimate, easy to contact, and ready to convert a skeptical visitor.", M, y + 4, W - 2 * M, size=9.3, color=COLORS["muted"])
    y -= 8
    col_w = (W - 2 * M - 12) / 2
    card(c, M, y - 148, col_w, 148, fill=colors.white, accent=COLORS["orange"])
    c.setFont(BOLD, 10)
    c.setFillColor(COLORS["ink"])
    c.drawString(M + 13, y - 22, "FOUNDATION AUDIT CHECKLIST")
    yy = y - 48
    for a, b in [
        ("Facebook page", "High-res logo, cover, business description, active CTA."),
        ("Google profile", "Exact location pin, service radius, hours, and phone."),
        ("Landing page", "Mobile speed, clear packages, proof, and direct booking."),
        ("Contact routes", "Click-to-call, WhatsApp or Viber, and inquiry form."),
    ]:
        yy = two_column_item(c, M + 13, yy, a + ":", b, col_w - 142)

    card(c, M + col_w + 12, y - 148, col_w, 148, fill=colors.white, accent=COLORS["blue"])
    c.setFont(BOLD, 10)
    c.setFillColor(COLORS["blue"])
    c.drawString(M + col_w + 25, y - 22, "WHY THIS MATTERS")
    para(c, "If customers click an ad and see an incomplete page, weak proof, or unclear estimate path, they hesitate. The foundation makes the first touch feel credible, current, and easy to act on.", M + col_w + 25, y - 48, col_w - 28, size=9.2, leading=12.5)

    y -= 172
    card(c, M, y - 48, W - 2 * M, 48, fill=COLORS["soft"])
    c.setFont(BOLD, 9.7)
    c.setFillColor(COLORS["ink"])
    c.drawString(M + 12, y - 18, "TECHNICAL READINESS STANDARDS")
    para(c, "Speed: below 3 seconds on mobile. Security: HTTPS and trust cues. Clarity: sticky call and message buttons. Proof: visible reviews and finished work.", M + 12, y - 33, W - 2 * M - 24, size=8.1, leading=10)

    y -= 82
    y = heading(c, "Step 2: Use Facebook Ads to reach buyers with proof", M, y, 17)
    y = para(c, "Do not rely only on organic reach. Paid distribution puts strong proof in front of people who are most likely to need the service.", M, y + 4, W - 2 * M, size=9.3, color=COLORS["muted"])
    y -= 10
    card(c, M, y - 74, W - 2 * M, 74, fill=COLORS["soft"])
    c.setFont(BOLD, 10)
    c.setFillColor(COLORS["ink"])
    c.drawString(M + 12, y - 20, "HIGH-PERFORMING CREATIVE FORMATS")
    px = M + 12
    for title, body, accent in [
        ("Actual Works", "Finished work with project specs.", COLORS["orange"]),
        ("Before & After", "Visual proof of transformation.", COLORS["cyan"]),
        ("Problem Solver", "Direct answer to customer pain.", colors.HexColor("#3B82F6")),
        ("Local Spotlight", "Targeted to subdivisions and cities.", COLORS["green"]),
    ]:
        mini_metric(c, px, y - 62, (W - 2 * M - 54) / 4, 36, title, body, accent)
        px += (W - 2 * M - 54) / 4 + 10

    y -= 98
    card(c, M, y - 56, col_w, 56, fill=colors.white, accent=colors.HexColor("#3B82F6"))
    c.setFont(BOLD, 10)
    c.setFillColor(colors.HexColor("#2563EB"))
    c.drawString(M + 13, y - 20, "HYPER-LOCAL GEOTARGETING")
    para(c, "Concentrate budget on the exact radius, city, or subdivision where the business can deliver fastest.", M + 13, y - 36, col_w - 26, size=8.3, leading=10)
    card(c, M + col_w + 12, y - 56, col_w, 56, fill=colors.white, accent=COLORS["green"])
    c.setFont(BOLD, 10)
    c.setFillColor(colors.HexColor("#047857"))
    c.drawString(M + col_w + 25, y - 20, "CLEAR CALL TO ACTION")
    para(c, 'Every ad should point to one action: "Send Message", "Request Estimate", or "Call for Consultation".', M + col_w + 25, y - 36, col_w - 26, size=8.3, leading=10)

    y -= 78
    card(c, M, y - 66, W - 2 * M, 66, fill=COLORS["orange_soft"], stroke=colors.HexColor("#FED7AA"))
    c.setFont(BOLD, 10)
    c.setFillColor(colors.HexColor("#C2410C"))
    c.drawString(M + 13, y - 20, "AD COPY FORMULA")
    para(c, "Local hook and problem -> visual proof and solution -> trust credentials -> direct call to action. The ad should make the next step obvious.", M + 13, y - 38, W - 2 * M - 26, size=8.5, leading=11)
    c.showPage()


def page_trust_search(c: canvas.Canvas) -> None:
    header(c, "Phase 2: Trust & Search", 4)
    y = H - 105
    y = heading(c, "Step 3: Build a website that answers customer doubts", M, y, 17)
    y = para(c, "The website should help a visitor decide within 30 seconds whether the business is credible, relevant, and easy to contact.", M, y + 4, W - 2 * M, size=9.3, color=COLORS["muted"])
    y -= 10
    card(c, M, y - 118, W - 2 * M, 118, fill=colors.white, accent=COLORS["orange"])
    c.setFont(BOLD, 10)
    c.setFillColor(COLORS["ink"])
    c.drawString(M + 13, y - 21, "SIX QUESTIONS THE PAGE MUST ANSWER")
    q_w = (W - 2 * M - 50) / 3
    q_y = y - 56
    for i, question in enumerate([
        "What exactly do they do?", "Are they near me?", "Do they have experience?",
        "Do they have proof?", "Can I trust them?", "How do I request an estimate?",
    ], 1):
        px = M + 13 + ((i - 1) % 3) * (q_w + 12)
        py = q_y - ((i - 1) // 3) * 38
        card(c, px, py, q_w, 29, fill=COLORS["soft"])
        c.setFont(BOLD, 8.8)
        c.setFillColor(COLORS["orange"] if i <= 3 else COLORS["blue"])
        c.drawString(px + 7, py + 10, f"{i}. {question}")

    y -= 140
    card(c, M, y - 48, W - 2 * M, 48, fill=COLORS["soft"])
    c.setFont(BOLD, 9.8)
    c.setFillColor(COLORS["ink"])
    c.drawString(M + 12, y - 18, "HIGH-CONVERTING LANDING PAGE WIREFRAME")
    para(c, "Header / hero -> proof portfolio -> client reviews -> booking form. The visitor should never wonder what to do next.", M + 12, y - 34, W - 2 * M - 24, size=8.4)

    y -= 82
    y = heading(c, "Step 4: Use Google Business Profile for local trust", M, y, 17)
    y = para(c, "Some clients do not come from Facebook. Urgent buyers often search directly on Google and compare the top local options.", M, y + 4, W - 2 * M, size=9.3, color=COLORS["muted"])
    y -= 12
    col_w = (W - 2 * M - 12) / 2
    card(c, M, y - 116, col_w, 116, fill=colors.white, accent=COLORS["blue"])
    c.setFont(BOLD, 10)
    c.setFillColor(COLORS["blue"])
    c.drawString(M + 13, y - 22, "HIGH-INTENT SEARCHES")
    para(c, '"[Service] near me"   "[Service] in [City]"   "[Service] contact number"   "[Service] price estimate"', M + 13, y - 45, col_w - 26, font="Courier", size=8.5, leading=12)
    para(c, "The Google card should show exact location, phone, service category, reviews, photos, and website link.", M + 13, y - 88, col_w - 26, size=8.2, leading=10.5)

    card(c, M + col_w + 12, y - 124, col_w, 124, fill=colors.white, accent=COLORS["green"])
    c.setFont(BOLD, 10)
    c.setFillColor(colors.HexColor("#047857"))
    c.drawString(M + col_w + 25, y - 22, "GOOGLE REVIEW FLYWHEEL")
    yy = y - 50
    for a, b in [
        ("5-star proof", "Real people trusted the service."),
        ("Recent velocity", "The business is active and consistent."),
        ("Local SEO edge", "Better proof can multiply calls from Maps."),
    ]:
        yy = two_column_item(c, M + col_w + 25, yy, a + ":", b, col_w - 142)

    y -= 148
    card(c, M, y - 58, W - 2 * M, 58, fill=COLORS["soft"])
    c.setFont(BOLD, 10)
    c.setFillColor(COLORS["ink"])
    c.drawString(M + 12, y - 20, "GBP QUICK WINS")
    para(c, "Upload 3-5 geotagged photos weekly, answer each review within 24 hours, keep hours current, add service keywords, and embed Google Map on the website.", M + 12, y - 38, W - 2 * M - 24, size=8.5, leading=11)
    c.showPage()


def page_assets_boosting(c: canvas.Canvas) -> None:
    header(c, "Phase 3: Assets & Boosting", 5)
    y = H - 105
    y = heading(c, "Step 5: Turn every project into a proof asset", M, y, 17)
    y = para(c, "A completed project should create marketing fuel for the next client, not disappear after delivery.", M, y + 4, W - 2 * M, size=9.3, color=COLORS["muted"])
    y -= 10
    card(c, M, y - 78, W - 2 * M, 78, fill=COLORS["navy"], stroke=COLORS["navy"])
    c.setFont(BOLD, 10)
    c.setFillColor(COLORS["cyan"])
    c.drawString(M + 13, y - 21, "5-ASSET CAPTURE PROTOCOL")
    px = M + 13
    for title, body, accent in [
        ("Before & during", "Show the starting point and work process.", COLORS["orange"]),
        ("After photos", "Clean finished result from multiple angles.", COLORS["cyan"]),
        ("Client review", "Short authentic quote or screenshot.", COLORS["green"]),
    ]:
        mini_metric(c, px, y - 66, (W - 2 * M - 50) / 3, 40, title, body, accent)
        px += (W - 2 * M - 50) / 3 + 12

    y -= 110
    c.setFont(BOLD, 10)
    c.setFillColor(COLORS["ink"])
    c.drawString(M, y, "WHERE EACH NEW ASSET SHOULD GO")
    y -= 62
    px = M
    for title, body, accent in [
        ("Facebook Organic", "Location-tagged proof post.", colors.HexColor("#3B82F6")),
        ("Facebook Ads", "Creative for nearby buyers.", COLORS["orange"]),
        ("Google Profile", "Photo upload for local search.", COLORS["green"]),
        ("Website Portfolio", "Permanent case study asset.", COLORS["cyan"]),
    ]:
        mini_metric(c, px, y, (W - 2 * M - 24) / 4, 50, title, body, accent)
        px += (W - 2 * M - 24) / 4 + 8

    y -= 28
    y = heading(c, "Step 6: Boost only content with strong proof", M, y, 17)
    y = para(c, "Not every post deserves budget. Spend behind content that gives a buyer a clear reason to inquire.", M, y + 4, W - 2 * M, size=9.3, color=COLORS["muted"])
    y -= 12
    col_w = (W - 2 * M - 12) / 2
    card(c, M, y - 148, col_w, 148, fill=colors.white, accent=COLORS["orange"])
    c.setFont(BOLD, 10)
    c.setFillColor(COLORS["ink"])
    c.drawString(M + 13, y - 22, "BOOSTING CRITERIA")
    yy = y - 50
    for a, b in [
        ("Clear before-after", "Value appears in the first 3 seconds."),
        ("Specific breakdown", "Explains the problem and solution."),
        ("Location relatability", "Mentions the city or service area."),
        ("Direct CTA", "Tells the client exactly how to request help."),
    ]:
        yy = two_column_item(c, M + 13, yy, a + ":", b, col_w - 142)

    card(c, M + col_w + 12, y - 148, col_w, 148, fill=COLORS["orange_soft"], stroke=colors.HexColor("#FED7AA"))
    c.setFont(BOLD, 10)
    c.setFillColor(colors.HexColor("#C2410C"))
    c.drawString(M + col_w + 25, y - 22, "DO NOT BOOST WITHOUT A REASON")
    para(c, "Generic quotes, stock images, and simple posters usually spend money without building trust. The best boosted post should show real capability, real proof, and a next step.", M + col_w + 25, y - 48, col_w - 28, size=8.8, leading=12)

    y -= 172
    card(c, M, y - 52, W - 2 * M, 52, fill=colors.white, accent=COLORS["blue"])
    c.setFont(BOLD, 10)
    c.setFillColor(COLORS["blue"])
    c.drawString(M + 13, y - 20, "70 / 20 / 10 BUDGET RULE")
    para(c, "70% to proven proof-first ads, 20% to retargeting and case studies, 10% to new creative tests.", M + 13, y - 38, W - 2 * M - 26, size=8.5)
    y -= 72
    card(c, M, y - 52, W - 2 * M, 52, fill=COLORS["soft"])
    c.setFont(BOLD, 10)
    c.setFillColor(COLORS["ink"])
    c.drawString(M + 13, y - 20, "RETARGETING BLUEPRINT")
    para(c, "Retarget people who clicked, visited, watched, or messaged within the last 30-60 days using new proof assets and helpful case studies.", M + 13, y - 38, W - 2 * M - 26, size=8.5)
    c.showPage()


def page_nurturing_roi(c: canvas.Canvas) -> None:
    header(c, "Phase 4: Nurturing & ROI", 6)
    y = H - 105
    y = heading(c, "Step 7: Follow up with value, not pressure", M, y, 17)
    y = para(c, "Some leads need comparison time, budget time, or schedule clarity. Follow-up should make the decision easier.", M, y + 4, W - 2 * M, size=9.3, color=COLORS["muted"])
    y -= 12
    col_w = (W - 2 * M - 12) / 2
    card(c, M, y - 88, col_w, 88, fill=COLORS["red_soft"], accent=COLORS["red"])
    c.setFont(BOLD, 10)
    c.setFillColor(colors.HexColor("#991B1B"))
    c.drawString(M + 13, y - 22, "WRONG: PRESSURE FOLLOW-UP")
    para(c, '"Hi maam/sir, follow up lang po sa estimate kahapon. Kukunin nyo po ba?"', M + 13, y - 48, col_w - 26, size=8.6, leading=11)
    para(c, "This can feel pushy and can reduce trust.", M + 13, y - 72, col_w - 26, size=8.3, leading=10, color=COLORS["muted"])

    card(c, M + col_w + 12, y - 88, col_w, 88, fill=COLORS["green_soft"], accent=COLORS["green"])
    c.setFont(BOLD, 10)
    c.setFillColor(colors.HexColor("#047857"))
    c.drawString(M + col_w + 25, y - 22, "RIGHT: VALUE-FIRST MESSAGE")
    para(c, '"Hi [Name], sharing photos from a similar project nearby and a rough cost range so you can compare properly."', M + col_w + 25, y - 48, col_w - 28, size=8.6, leading=11, max_lines=3)
    para(c, "This helps the client decide with more confidence.", M + col_w + 25, y - 78, col_w - 28, size=8.3, leading=10, color=COLORS["muted"])

    y -= 112
    px = M
    for title, body, accent in [
        ("Template A: Case Study", "Share a similar project that solves the same concern.", colors.HexColor("#3B82F6")),
        ("Template B: Client Review", "Send a review from a similar customer.", COLORS["green"]),
        ("Template C: Schedule Update", "Offer a respectful availability update.", COLORS["orange"]),
    ]:
        mini_metric(c, px, y - 48, (W - 2 * M - 24) / 3, 48, title, body, accent)
        px += (W - 2 * M - 24) / 3 + 12

    y -= 82
    y = heading(c, "Step 8: Track where the best leads really come from", M, y, 17)
    y = para(c, "Measure the whole funnel so decisions are made from revenue behavior, not vanity metrics.", M, y + 4, W - 2 * M, size=9.3, color=COLORS["muted"])
    y -= 10
    stages = [
        ("Stage 1", "Total inquiries received", "All inquiries", COLORS["cyan"]),
        ("Stage 2", "Qualified leads", "Filtered clients", COLORS["blue"]),
        ("Stage 3", "Estimates sent", "Active opportunity", colors.HexColor("#3B82F6")),
        ("Stage 4", "Booked & closed projects", "Closed client", colors.HexColor("#F59E0B")),
        ("Stage 5", "Actual revenue & net marketing ROI", "Profitable growth", COLORS["green"]),
    ]
    for stage, title, right, accent in stages:
        card(c, M, y - 28, W - 2 * M, 28, fill=COLORS["green_soft"] if stage == "Stage 5" else colors.white, accent=accent)
        label(c, stage, M + 12, y - 17, fill=COLORS["blue_soft"], color=accent, stroke=colors.HexColor("#D7E7FF"))
        c.setFont(BOLD, 10)
        c.setFillColor(COLORS["ink"])
        c.drawString(M + 92, y - 15, title)
        c.setFillColor(accent)
        c.drawRightString(W - M - 12, y - 15, right)
        y -= 38

    y -= 6
    card(c, M, y - 62, W - 2 * M, 62, fill=colors.white, accent=COLORS["blue"])
    c.setFont(BOLD, 10)
    c.setFillColor(COLORS["blue"])
    c.drawString(M + 13, y - 21, "DATA-DRIVEN STRATEGY DECISION")
    para(c, "After several weeks, scale the channels with the highest quality leads and best close rate. If Google Search closes faster or before-after ads produce lower cost per lead, the budget moves there.", M + 13, y - 40, W - 2 * M - 26, size=8.6, leading=11)
    c.showPage()


def page_roadmap(c: canvas.Canvas) -> None:
    header(c, "Journey & 30-60-90 Roadmap", 7)
    y = title_block(
        c,
        "Complete System Integration",
        "The rollout plan clients can follow",
        "This roadmap turns the strategy into staged execution: foundation first, then reach, then scale.",
        H - 105,
    )
    card(c, M, y - 58, W - 2 * M, 58, fill=COLORS["navy"], stroke=COLORS["navy"])
    sx = M + 54
    gap = (W - 2 * M - 108) / 4
    for i, stage in enumerate(["Ads", "Website & GBP", "Call / DM", "Estimate", "Proof Asset"], 1):
        c.setFillColor([COLORS["orange"], COLORS["cyan"], colors.HexColor("#3B82F6"), colors.HexColor("#F59E0B"), COLORS["green"]][i - 1])
        c.circle(sx, y - 21, 10, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont(BOLD, 8)
        c.drawCentredString(sx, y - 24, str(i))
        c.drawCentredString(sx, y - 43, stage)
        if i < 5:
            c.setFillColor(COLORS["cyan"])
            c.drawCentredString(sx + gap / 2, y - 25, "->")
        sx += gap

    y -= 96
    phase_w = (W - 2 * M - 24) / 3
    for x, title, subtitle, items, accent in [
        (M, "Phase 1: Days 1-15", "Foundation & setup", ["Conversion website", "Google profile", "Facebook CTA", "Initial proof batch"], COLORS["cyan"]),
        (M + phase_w + 12, "Phase 2: Days 16-30", "Reach & ad launch", ["Proof-based ads", "Geo targeting", "Call routing", "Daily lead tracking"], COLORS["orange"]),
        (M + 2 * (phase_w + 12), "Phase 3: Days 31-90+", "Flywheel & scale", ["Project proof capture", "Value follow-up", "Scale best ROI", "Review collection"], COLORS["green"]),
    ]:
        card(c, x, y - 132, phase_w, 132, fill=colors.white, accent=accent, accent_side="top")
        c.setFont(BOLD, 10)
        c.setFillColor(accent)
        c.drawString(x + 12, y - 24, title.upper())
        c.setFillColor(COLORS["ink"])
        c.drawString(x + 12, y - 42, subtitle)
        yy = y - 64
        for item in items:
            c.setFillColor(COLORS["soft"])
            c.setStrokeColor(COLORS["line"])
            c.circle(x + 18, yy + 2, 5, fill=1, stroke=1)
            para(c, item, x + 31, yy + 5, phase_w - 44, size=8.7, leading=11, max_lines=1)
            yy -= 20

    y -= 160
    card(c, M, y - 50, W - 2 * M, 50, fill=COLORS["soft"])
    c.setFont(BOLD, 9.8)
    c.setFillColor(COLORS["ink"])
    c.drawString(M + 12, y - 18, "INDUSTRY COMPATIBILITY")
    para(c, "Contractors and trades: transformations and ocular quotes. Clinics and health: credentials and consultation slots. Professional B2B and law: case studies and discovery calls.", M + 12, y - 34, W - 2 * M - 24, size=8.3, leading=10.5)

    y -= 78
    card(c, M, y - 82, W - 2 * M, 82, fill=COLORS["navy"], stroke=COLORS["navy"])
    c.setFont(BOLD, 9)
    c.setFillColor(COLORS["orange"])
    c.drawString(M + 14, y - 23, "READY TO START THE SYSTEM?")
    c.setFont(BOLD, 15)
    c.setFillColor(colors.white)
    c.drawString(M + 14, y - 46, "WE FORGE WEB - YOUR CLIENT GROWTH PARTNER")
    para(c, "Build the foundation. Strengthen reach. Show proof. Generate inquiries. Track what works. Then scale.", M + 14, y - 64, W - 2 * M - 180, size=8.3, leading=10, color=colors.HexColor("#D1D5DB"))
    c.setStrokeColor(colors.HexColor("#374151"))
    c.line(W - M - 150, y - 72, W - M - 150, y - 16)
    c.setFont(BOLD, 12)
    c.setFillColor(COLORS["cyan"])
    c.drawRightString(W - M - 14, y - 35, "+63 991 917 3652")
    c.setFont(FONT, 8.6)
    c.setFillColor(colors.white)
    c.drawRightString(W - M - 14, y - 53, "hello@weforgeweb.com")
    c.setFillColor(COLORS["cyan"])
    c.drawRightString(W - M - 14, y - 69, "weforgeweb.com")
    c.showPage()


def render_previews() -> None:
    PREVIEWS.mkdir(exist_ok=True)
    for old in PREVIEWS.glob("codex_page_*.png"):
        old.unlink()
    doc = fitz.open(str(OUTPUT))
    for i, page in enumerate(doc, 1):
        pix = page.get_pixmap(dpi=150)
        pix.save(str(PREVIEWS / f"codex_page_{i}.png"))


def build_pdf() -> None:
    if not LOGO.exists():
        raise FileNotFoundError(f"Missing copied logo asset: {LOGO}")
    c = canvas.Canvas(str(OUTPUT), pagesize=A4)
    c.setTitle("We Forge Web - Client Growth Kit - Codex Premium Playbook")
    c.setAuthor("Codex for We Forge Web")
    cover(c)
    page_strategy(c)
    page_foundation(c)
    page_trust_search(c)
    page_assets_boosting(c)
    page_nurturing_roi(c)
    page_roadmap(c)
    c.save()
    render_previews()
    doc = fitz.open(str(OUTPUT))
    print(f"Generated: {OUTPUT}")
    print(f"Pages: {doc.page_count}")
    print(f"Previews: {PREVIEWS}")


if __name__ == "__main__":
    build_pdf()
