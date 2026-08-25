#!/usr/bin/env python3
"""
Codex-built client-readable PDF for the recommended acquisition system.

This is a separate, self-contained generator for the user's simplified Taglish
system copy. It references only assets copied into codex_pdf_version.
"""

from __future__ import annotations

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
PREVIEWS = ROOT / "previews_recommended_system"
OUTPUT = ROOT / "WeForgeWeb_Recommended_Client_Acquisition_System_Codex.pdf"
LOGO = ASSETS / "weforgeweb-logo.png"

W, H = A4
M = 46


INK = colors.HexColor("#111827")
TEXT = colors.HexColor("#374151")
MUTED = colors.HexColor("#6B7280")
LINE = colors.HexColor("#DADCE0")
SOFT = colors.HexColor("#F5F7FA")
BLUE = colors.HexColor("#0071E3")
BLUE_SOFT = colors.HexColor("#EAF4FF")
CYAN = colors.HexColor("#00A4D6")
ORANGE = colors.HexColor("#FF6B35")
ORANGE_SOFT = colors.HexColor("#FFF4EC")
GREEN = colors.HexColor("#10B981")
GREEN_SOFT = colors.HexColor("#ECFDF5")
NAVY = colors.HexColor("#111827")
WHITE = colors.white


def register_fonts() -> tuple[str, str, str]:
    fonts_dir = Path("C:/Windows/Fonts")
    regular = fonts_dir / "segoeui.ttf"
    bold = fonts_dir / "segoeuib.ttf"
    italic = fonts_dir / "segoeuii.ttf"
    if regular.exists() and bold.exists():
        pdfmetrics.registerFont(TTFont("RS-Regular", str(regular)))
        pdfmetrics.registerFont(TTFont("RS-Bold", str(bold)))
        if italic.exists():
            pdfmetrics.registerFont(TTFont("RS-Italic", str(italic)))
        else:
            pdfmetrics.registerFont(TTFont("RS-Italic", str(regular)))
        return "RS-Regular", "RS-Bold", "RS-Italic"
    return "Helvetica", "Helvetica-Bold", "Helvetica-Oblique"


FONT, BOLD, ITALIC = register_fonts()


def width(text: str, font: str, size: float) -> float:
    return pdfmetrics.stringWidth(text, font, size)


def wrap(text: str, font: str, size: float, max_width: float) -> list[str]:
    lines: list[str] = []
    current = ""
    for word in text.split():
        trial = f"{current} {word}".strip()
        if not current or width(trial, font, size) <= max_width:
            current = trial
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def text_block(c: canvas.Canvas, text: str, x: float, y: float, max_width: float,
               *, font: str = FONT, size: float = 9.5, leading: float = 13,
               color=TEXT, max_lines: int | None = None) -> float:
    c.setFont(font, size)
    c.setFillColor(color)
    lines = wrap(text, font, size, max_width)
    if max_lines is not None:
        lines = lines[:max_lines]
    for line in lines:
        c.drawString(x, y, line)
        y -= leading
    return y


def card(c: canvas.Canvas, x: float, y: float, w: float, h: float,
         *, fill=WHITE, stroke=LINE, accent=None, accent_side: str = "left") -> None:
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.roundRect(x, y, w, h, 10, fill=1, stroke=1)
    if accent:
        c.setFillColor(accent)
        if accent_side == "left":
            c.roundRect(x, y, 5, h, 10, fill=1, stroke=0)
        elif accent_side == "top":
            c.roundRect(x, y + h - 5, w, 5, 10, fill=1, stroke=0)


def chip(c: canvas.Canvas, text: str, x: float, y: float,
         *, fill=BLUE_SOFT, stroke=colors.HexColor("#BBD7FF"), color=BLUE) -> None:
    c.setFont(BOLD, 8.5)
    w = width(text.upper(), BOLD, 8.5) + 20
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.roundRect(x, y - 7, w, 18, 6, fill=1, stroke=1)
    c.setFillColor(color)
    c.drawString(x + 10, y - 1.5, text.upper())


def header(c: canvas.Canvas, title: str, page: int, pages: int = 5) -> None:
    c.setFillColor(WHITE)
    c.rect(0, H - 58, W, 58, fill=1, stroke=0)
    c.setStrokeColor(LINE)
    c.line(0, H - 58, W, H - 58)
    c.drawImage(ImageReader(str(LOGO)), M, H - 42, width=30, height=30, mask="auto")
    c.setFont(BOLD, 13)
    c.setFillColor(INK)
    c.drawString(M + 40, H - 25, "WE FORGE")
    c.setFillColor(BLUE)
    c.drawString(M + 111, H - 25, "WEB")
    c.setFont(BOLD, 7.8)
    c.setFillColor(MUTED)
    c.drawString(M + 40, H - 42, title.upper())
    c.setFont(BOLD, 8)
    c.setFillColor(TEXT)
    label_w = width(title.upper(), BOLD, 8) + 28
    c.setFillColor(SOFT)
    c.setStrokeColor(LINE)
    c.roundRect(W - M - label_w, H - 41, label_w, 24, 8, fill=1, stroke=1)
    c.setFillColor(TEXT)
    c.drawCentredString(W - M - label_w / 2, H - 31, title.upper())

    c.setFillColor(SOFT)
    c.rect(0, 0, W, 31, fill=1, stroke=0)
    c.setStrokeColor(LINE)
    c.line(0, 31, W, 31)
    c.setFont(BOLD, 8)
    c.setFillColor(INK)
    c.drawString(M, 13, "We Forge Web - Recommended Client System")
    c.drawCentredString(W / 2, 13, "weforgeweb.com")
    c.setFillColor(BLUE)
    c.drawRightString(W - M, 13, f"Page {page} of {pages}")


def page_title(c: canvas.Canvas, tag: str, title: str, body: str, y: float) -> float:
    chip(c, tag, M, y)
    y -= 33
    c.setFont(BOLD, 25)
    c.setFillColor(INK)
    for line in wrap(title, BOLD, 25, W - 2 * M):
        c.drawString(M, y, line)
        y -= 30
    y -= 2
    y = text_block(c, body, M, y, W - 2 * M, size=11, leading=15, color=TEXT)
    return y - 12


def bullet(c: canvas.Canvas, text: str, x: float, y: float, *, color=BLUE) -> float:
    c.setFillColor(color)
    c.circle(x + 4, y - 3, 3.2, fill=1, stroke=0)
    return text_block(c, text, x + 16, y, 210, size=9.2, leading=12, color=TEXT, max_lines=2)


def feature_card(c: canvas.Canvas, x: float, y: float, w: float, h: float,
                 eyebrow: str, title: str, body: str, accent) -> None:
    card(c, x, y, w, h, fill=WHITE, accent=accent, accent_side="top")
    c.setFont(BOLD, 8.2)
    c.setFillColor(accent)
    c.drawString(x + 12, y + h - 22, eyebrow.upper())
    c.setFont(BOLD, 13)
    c.setFillColor(INK)
    c.drawString(x + 12, y + h - 42, title)
    text_block(c, body, x + 12, y + h - 61, w - 24, size=8.7, leading=11.5,
               color=TEXT, max_lines=5)


def cover(c: canvas.Canvas) -> None:
    c.setFillColor(colors.HexColor("#F7FAFF"))
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(colors.HexColor("#EAF4FF"))
    c.circle(-48, H - 75, 180, fill=1, stroke=0)
    c.drawImage(ImageReader(str(LOGO)), M, H - 92, width=42, height=42, mask="auto")
    c.setFont(BOLD, 21)
    c.setFillColor(INK)
    c.drawString(M + 54, H - 66, "WE FORGE")
    c.setFillColor(BLUE)
    c.drawString(M + 166, H - 66, "WEB")
    c.setFont(BOLD, 8)
    c.setFillColor(MUTED)
    c.drawString(M + 54, H - 84, "RECOMMENDED CLIENT ACQUISITION SYSTEM")
    chip(c, "Codex Client Version", W - M - 145, H - 69)

    y = H - 195
    chip(c, "Recommended System", M, y)
    y -= 44
    c.setFont(BOLD, 30)
    c.setFillColor(INK)
    c.drawString(M, y, "Mas Madaling Makakuha")
    y -= 34
    c.setFillColor(BLUE)
    c.drawString(M, y, "Ng Tamang Inquiries")
    y -= 34
    y = text_block(
        c,
        "Simple lang po yung idea: hindi natin iaasa sa Facebook lang, Google lang, or website lang yung pagkuha ng customers. Mas maganda kapag may malinaw na trabaho yung bawat isa at magkakabit sila.",
        M,
        y,
        W - 2 * M,
        size=11.5,
        leading=16,
        color=TEXT,
    )

    y -= 18
    card(c, M, y - 86, W - 2 * M, 86, fill=WHITE)
    c.setFont(BOLD, 10)
    c.setFillColor(BLUE)
    c.drawString(M + 16, y - 23, "THE SIMPLE FLOW")
    flow = [
        ("Facebook Ads", ORANGE),
        ("Facebook Page", BLUE),
        ("Website", CYAN),
        ("Google", GREEN),
        ("Call / Message", colors.HexColor("#3B82F6")),
        ("Estimate", colors.HexColor("#F59E0B")),
        ("New Proof", GREEN),
    ]
    step_gap = (W - 2 * M - 54) / 6
    sx = M + 26
    for i, (name, color) in enumerate(flow):
        c.setFillColor(color)
        c.circle(sx, y - 53, 10, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont(BOLD, 7.5)
        c.drawCentredString(sx, y - 56, str(i + 1))
        c.setFont(BOLD, 7.3)
        c.setFillColor(INK)
        c.drawCentredString(sx, y - 73, name)
        if i < len(flow) - 1:
            c.setFillColor(CYAN)
            c.setFont(BOLD, 8.5)
            c.drawCentredString(sx + step_gap / 2, y - 55, "->")
        sx += step_gap

    y -= 118
    col_w = (W - 2 * M - 24) / 3
    feature_card(c, M, y - 105, col_w, 105, "Goal", "Hindi lang messages", "Ang goal is mas maraming customer na may actual need, nakita na yung proof, alam yung service area, at ready nang magpa-estimate.", BLUE)
    feature_card(c, M + col_w + 12, y - 105, col_w, 105, "Method", "Step by step", "Hindi kailangan lahat gawin agad. Ang importante, may malinaw na direction kung ano ang unang aayusin at palalakasin.", ORANGE)
    feature_card(c, M + 2 * (col_w + 12), y - 105, col_w, 105, "Flywheel", "Every project helps", "Bawat completed project nagiging bagong proof para mas lumakas ang Facebook, Google, website, at future ads.", GREEN)

    c.setStrokeColor(LINE)
    c.line(M, 75, W - M, 75)
    c.setFont(BOLD, 10)
    c.setFillColor(INK)
    c.drawString(M, 50, "WE FORGE WEB - CLIENT GROWTH SYSTEM")
    c.setFont(FONT, 8.6)
    c.setFillColor(MUTED)
    c.drawRightString(W - M, 50, "weforgeweb.com    +63 991 917 3652    hello@weforgeweb.com")
    c.showPage()


def page_roles(c: canvas.Canvas) -> None:
    header(c, "Roles Of Each Platform", 2)
    y = page_title(
        c,
        "System Foundation",
        "May malinaw na trabaho yung bawat isa",
        "Mas effective ang client acquisition kapag hindi hiwa-hiwalay ang Facebook, ads, website, Google, at follow-up. Bawat channel may role, tapos nagtutulungan sila.",
        H - 110,
    )

    col_w = (W - 2 * M - 16) / 2
    feature_card(
        c, M, y - 118, col_w, 118, "Facebook Page", "Magandang unang impression",
        "Kapag may customer na nag-check sa business, professional, organized, at clear agad kung ano yung services, saan kayo nagse-service, at paano kayo makokontak.",
        BLUE,
    )
    feature_card(
        c, M + col_w + 16, y - 118, col_w, 118, "Facebook Boosting / Ads", "Mas mabilis ma-reach",
        "Hindi lang tayo maghihintay na organically makita yung business. Palalakasin natin yung actual projects, before-and-after, reviews, service locations, at proof-based content.",
        ORANGE,
    )

    y -= 145
    feature_card(
        c, M, y - 130, col_w, 130, "Website / Landing Page", "Complete proof bago mag-decide",
        "Kapag interested na yung customer, may isang clear page silang makikita: services, actual projects, experience, service areas, before and after, reviews, at contact options.",
        CYAN,
    )
    feature_card(
        c, M + col_w + 16, y - 130, col_w, 130, "Google Business Profile", "Search, location, at reviews",
        "Kapag customer mismo yung naghahanap sa Google, gusto natin may chance nilang makita kayo. Dito nila makikita service area, photos, phone number, website, business info, at genuine reviews.",
        GREEN,
    )

    y -= 158
    card(c, M, y - 92, W - 2 * M, 92, fill=NAVY, stroke=NAVY)
    c.setFont(BOLD, 15)
    c.setFillColor(WHITE)
    c.drawString(M + 18, y - 28, "Kapag magkakabit sila, mas informed ang customer bago pa kayo kausapin.")
    text_block(
        c,
        "Kung nakita muna kayo sa Facebook, pwede nilang i-check at i-confirm sa Google. Kung naging interested sila, pupunta sila sa website. Kapag comfortable na sila, mas madali na silang tatawag or magme-message.",
        M + 18,
        y - 52,
        W - 2 * M - 36,
        size=9.2,
        leading=12.5,
        color=colors.HexColor("#D1D5DB"),
    )
    c.showPage()


def page_decision(c: canvas.Canvas) -> None:
    header(c, "Decision & Inquiry Flow", 3)
    y = page_title(
        c,
        "Customer journey na mas madaling sundan",
        "From proof to inquiry",
        "Ang system ay hindi lang para magparami ng views. Ginagawa nitong mas malinaw sa customer kung ano yung business, bakit mapagkakatiwalaan, at paano sila magpapa-estimate.",
        H - 110,
    )

    card(c, M, y - 142, W - 2 * M, 142, fill=WHITE, accent=CYAN)
    c.setFont(BOLD, 13)
    c.setFillColor(INK)
    c.drawString(M + 16, y - 28, "Sa website / landing page, dapat makita nila:")
    left = M + 18
    right = M + 260
    yy = y - 55
    for item in ["Services", "Actual projects", "Experience", "Service areas"]:
        yy = bullet(c, item, left, yy, color=CYAN)
    yy = y - 55
    for item in ["Before and after", "Reviews", "Contact options"]:
        yy = bullet(c, item, right, yy, color=CYAN)
    c.setFont(BOLD, 10)
    c.setFillColor(BLUE)
    c.drawString(M + 16, y - 122, "Goal: mas informed na sila bago pa kayo kausapin.")

    y -= 172
    col_w = (W - 2 * M - 16) / 2
    card(c, M, y - 112, col_w, 112, fill=BLUE_SOFT, stroke=colors.HexColor("#BBD7FF"), accent=BLUE)
    c.setFont(BOLD, 14)
    c.setFillColor(BLUE)
    c.drawString(M + 16, y - 28, "Call / Message")
    text_block(
        c,
        "Dito na papasok yung inquiry. Kapag nakita na nila yung proof at naging comfortable na sila sa business, dapat madali na yung next step: tumawag, mag-message, or magpa-estimate.",
        M + 16,
        y - 53,
        col_w - 32,
        size=9.2,
        leading=12.3,
    )
    card(c, M + col_w + 16, y - 112, col_w, 112, fill=ORANGE_SOFT, stroke=colors.HexColor("#FED7AA"), accent=ORANGE)
    c.setFont(BOLD, 14)
    c.setFillColor(ORANGE)
    c.drawString(M + col_w + 32, y - 28, "Estimate")
    text_block(
        c,
        "Mas mataas ang chance na quality inquiry yung papasok dahil may context na sila: nakita na nila services, proof, location coverage, at paano kayo nagtatrabaho.",
        M + col_w + 32,
        y - 53,
        col_w - 32,
        size=9.2,
        leading=12.3,
    )

    y -= 145
    c.setFont(BOLD, 13)
    c.setFillColor(INK)
    c.drawString(M, y, "Ang gusto natin: mas maraming customer na...")
    y -= 28
    statements = [
        ("May actual need.", BLUE),
        ("Alam na kung ano yung ginagawa ninyo.", CYAN),
        ("Nakita na yung proof.", GREEN),
        ("Alam kung covered yung location nila.", ORANGE),
        ("Mas ready nang magtanong: Pwede po ba magpa-estimate?", BLUE),
    ]
    for idx, (statement, color) in enumerate(statements):
        x = M + (idx % 2) * (col_w + 16)
        row = idx // 2
        card(c, x, y - 42 - row * 54, col_w, 42, fill=WHITE, accent=color)
        c.setFont(BOLD, 9.8)
        c.setFillColor(INK)
        c.drawString(x + 16, y - 25 - row * 54, statement)
    c.showPage()


def page_proof_flywheel(c: canvas.Canvas) -> None:
    header(c, "Completed Project Flywheel", 4)
    y = page_title(
        c,
        "Every completed project becomes new proof",
        "Gamitin ulit para makuha yung next customer",
        "Bawat magandang project pwedeng gawing bagong marketing asset. Hindi siya matatapos sa delivery. Magiging proof siya para sa susunod na inquiry.",
        H - 110,
    )

    card(c, M, y - 140, W - 2 * M, 140, fill=NAVY, stroke=NAVY)
    c.setFont(BOLD, 13)
    c.setFillColor(CYAN)
    c.drawString(M + 16, y - 28, "Mula sa completed project, gumawa tayo ng:")
    items = [
        ("Photos", ORANGE),
        ("Before and after", CYAN),
        ("Facebook content", BLUE),
        ("Google photos", GREEN),
        ("Website project", colors.HexColor("#3B82F6")),
        ("Customer review", colors.HexColor("#F59E0B")),
    ]
    box_w = (W - 2 * M - 56) / 3
    for i, (item, color) in enumerate(items):
        x = M + 16 + (i % 3) * (box_w + 12)
        yy = y - 66 - (i // 3) * 44
        card(c, x, yy, box_w, 31, fill=WHITE, accent=color, accent_side="top")
        c.setFont(BOLD, 9.5)
        c.setFillColor(INK)
        c.drawCentredString(x + box_w / 2, yy + 11, item)

    y -= 170
    c.setFont(BOLD, 14)
    c.setFillColor(INK)
    c.drawString(M, y, "Then gagamitin ulit natin yung bagong proof para lumakas ang:")
    y -= 68
    col_w = (W - 2 * M - 24) / 4
    for i, (name, body, color) in enumerate([
        ("Facebook", "Mas maraming useful proof posts and ads.", BLUE),
        ("Google", "Mas updated photos and stronger reviews.", GREEN),
        ("Website", "Mas maraming actual projects na makikita.", CYAN),
        ("Future Ads", "Mas credible campaigns for the next customers.", ORANGE),
    ]):
        feature_card(c, M + i * (col_w + 8), y, col_w, 80, "Channel", name, body, color)

    y -= 42
    card(c, M, y - 88, W - 2 * M, 88, fill=GREEN_SOFT, stroke=colors.HexColor("#BBF7D0"), accent=GREEN)
    c.setFont(BOLD, 15)
    c.setFillColor(colors.HexColor("#047857"))
    c.drawString(M + 16, y - 28, "Ito yung compounding effect.")
    text_block(
        c,
        "Habang mas dumadami ang completed projects, mas dumadami rin ang proof. Habang mas dumadami ang proof, mas madali sa next customer na magtiwala, magtanong, at magpa-estimate.",
        M + 16,
        y - 53,
        W - 2 * M - 32,
        size=9.5,
        leading=13,
    )
    c.showPage()


def page_rollout(c: canvas.Canvas) -> None:
    header(c, "Step By Step Rollout", 5)
    y = page_title(
        c,
        "Yun po yung system na irerecommend naming buuin",
        "Hindi kailangan lahat gawin agad",
        "Ang importante, may malinaw tayong direction: ano yung unang aayusin, ano yung palalakasin, at paano gagamitin ang bawat completed project para makuha ang susunod na opportunity.",
        H - 110,
    )

    phases = [
        ("01", "Ayusin muna", "Facebook Page, Google Business Profile, website / landing page, contact options, and proof organization.", BLUE),
        ("02", "Palakasin ang reach", "Boosting / ads for actual projects, before-and-after, reviews, service locations, and proof-based content.", ORANGE),
        ("03", "Gawing madali ang inquiry", "Clear call, message, and estimate path once the customer has seen the proof and service details.", CYAN),
        ("04", "Gawing proof ang bawat project", "Collect photos, reviews, Google updates, website projects, and new content after every completed job.", GREEN),
    ]
    for num, title, body, color in phases:
        card(c, M, y - 76, W - 2 * M, 76, fill=WHITE, accent=color)
        c.setFillColor(color)
        c.circle(M + 28, y - 35, 14, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont(BOLD, 9)
        c.drawCentredString(M + 28, y - 39, num)
        c.setFont(BOLD, 13)
        c.setFillColor(INK)
        c.drawString(M + 54, y - 26, title)
        text_block(c, body, M + 54, y - 47, W - 2 * M - 76, size=9.2, leading=12.3, color=TEXT, max_lines=2)
        y -= 94

    y -= 8
    card(c, M, y - 104, W - 2 * M, 104, fill=NAVY, stroke=NAVY)
    c.setFont(BOLD, 14)
    c.setFillColor(ORANGE)
    c.drawString(M + 18, y - 30, "Final positioning")
    c.setFont(BOLD, 18)
    c.setFillColor(WHITE)
    c.drawString(M + 18, y - 57, "Hindi lang mas maraming messages. Mas maraming tamang inquiries.")
    text_block(
        c,
        "Mas maraming customer na may actual need, mas informed bago magtanong, at mas ready magpa-estimate because they already saw the proof, services, location coverage, and contact path.",
        M + 18,
        y - 78,
        W - 2 * M - 36,
        size=8.8,
        leading=11.5,
        color=colors.HexColor("#D1D5DB"),
    )
    c.showPage()


def render_previews() -> None:
    PREVIEWS.mkdir(exist_ok=True)
    for old in PREVIEWS.glob("recommended_system_page_*.png"):
        old.unlink()
    doc = fitz.open(str(OUTPUT))
    for i, page in enumerate(doc, 1):
        pix = page.get_pixmap(dpi=150)
        pix.save(str(PREVIEWS / f"recommended_system_page_{i}.png"))


def build() -> None:
    if not LOGO.exists():
        raise FileNotFoundError(f"Missing copied logo asset: {LOGO}")
    c = canvas.Canvas(str(OUTPUT), pagesize=A4)
    c.setTitle("We Forge Web - Recommended Client Acquisition System")
    c.setAuthor("Codex for We Forge Web")
    cover(c)
    page_roles(c)
    page_decision(c)
    page_proof_flywheel(c)
    page_rollout(c)
    c.save()
    render_previews()
    doc = fitz.open(str(OUTPUT))
    print(f"Generated: {OUTPUT}")
    print(f"Pages: {doc.page_count}")
    print(f"Previews: {PREVIEWS}")


if __name__ == "__main__":
    build()
