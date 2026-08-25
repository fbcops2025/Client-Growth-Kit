#!/usr/bin/env python3
"""
Client-readable PDF for the We Forge Web recommended inquiry system.

This is a separate, self-contained generator for the simplified Taglish system
copy. It references only assets copied into client_ready_pdf.
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
PREVIEWS = ROOT / "previews"
OUTPUT = ROOT / "WeForgeWeb_Inirerekomendang_Sistema_Para_Sa_Tamang_Inquiries.pdf"
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
    c.drawString(M, 13, "We Forge Web")
    c.drawCentredString(W / 2, 13, "Sistema Para Sa Tamang Inquiries")
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
    c.drawString(M + 54, H - 84, "SISTEMA PARA SA TAMANG INQUIRIES")
    chip(c, "Gabay Para Sa Client", W - M - 133, H - 69)

    y = H - 195
    chip(c, "Inirerekomendang Sistema", M, y)
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
    card(c, M, y - 100, W - 2 * M, 100, fill=WHITE)
    c.setFont(BOLD, 10)
    c.setFillColor(BLUE)
    c.drawString(M + 16, y - 23, "GANITO ANG SIMPLE NA DALOY")
    flow = [
        ("KAYO", "Ads", ORANGE),
        ("KAMI", "FB Page", BLUE),
        ("KAMI", "Landing Page", CYAN),
        ("KAMI", "Google", GREEN),
        ("KAYO", "Call / Message", colors.HexColor("#3B82F6")),
        ("KAYO", "Estimate / Closing", colors.HexColor("#F59E0B")),
    ]
    step_gap = (W - 2 * M - 54) / 5
    sx = M + 26
    for i, (owner, name, color) in enumerate(flow):
        c.setFillColor(color)
        c.circle(sx, y - 53, 10, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont(BOLD, 7.5)
        c.drawCentredString(sx, y - 56, str(i + 1))
        c.setFont(BOLD, 6.8)
        c.setFillColor(color)
        c.drawCentredString(sx, y - 72, owner)
        c.setFont(BOLD, 7.1)
        c.setFillColor(INK)
        for line_no, line in enumerate(wrap(name, BOLD, 7.1, 78)):
            c.drawCentredString(sx, y - 84 - line_no * 8, line)
        if i < len(flow) - 1:
            c.setFillColor(CYAN)
            c.setFont(BOLD, 8.5)
            c.drawCentredString(sx + step_gap / 2, y - 55, "->")
        sx += step_gap

    y -= 132
    col_w = (W - 2 * M - 24) / 3
    feature_card(c, M, y - 105, col_w, 105, "Kayo", "Ads at customer handling", "Kayo po ang magbo-boost, sasagot sa calls/messages, magbibigay ng estimate, at magha-handle ng closing.", ORANGE)
    feature_card(c, M + col_w + 12, y - 105, col_w, 105, "Kami", "Proof pages at profiles", "Kami po ang mag-aayos ng Facebook Page, landing page, at Google Business Profile para malinaw ang proof.", BLUE)
    feature_card(c, M + 2 * (col_w + 12), y - 105, col_w, 105, "Resulta", "Mas tamang inquiries", "Mas maraming customer na may actual need, nakita na ang proof, at mas ready nang magpa-estimate.", GREEN)

    c.setStrokeColor(LINE)
    c.line(M, 75, W - M, 75)
    c.setFont(BOLD, 10)
    c.setFillColor(INK)
    c.drawString(M, 50, "WE FORGE WEB")
    c.setFont(FONT, 8.6)
    c.setFillColor(MUTED)
    c.drawRightString(W - M, 50, "weforgeweb.com    +63 991 917 3652    hello@weforgeweb.com")
    c.showPage()


def page_roles(c: canvas.Canvas) -> None:
    header(c, "Kami Ang Mag-aayos Ng Proof", 2)
    y = page_title(
        c,
        "KAMI ang magse-setup ng foundation",
        "Ito po ang tutulungan naming ayusin",
        "Para kapag may customer na nag-check sa business, hindi sila maliligaw. Makikita nila agad kung ano ang services, saan kayo nagse-service, ano ang actual na gawa, at paano kayo kokontakin.",
        H - 110,
    )

    col_w = (W - 2 * M - 16) / 2
    feature_card(
        c, M, y - 126, col_w, 126, "KAMI", "Facebook Page Creation / Optimization",
        "Aayusin namin yung Facebook Page para professional, organized, at malinaw agad ang services, service areas, actual work, at contact information.",
        BLUE,
    )
    feature_card(
        c, M + col_w + 16, y - 126, col_w, 126, "KAMI", "Professional Landing Page",
        "Gagawa kami ng main proof page kung saan makikita agad ang services, actual projects, experience, service areas, reviews, at contact options.",
        CYAN,
    )

    y -= 154
    card(c, M, y - 126, W - 2 * M, 126, fill=WHITE, accent=GREEN, accent_side="top")
    c.setFont(BOLD, 8.2)
    c.setFillColor(GREEN)
    c.drawString(M + 14, y - 23, "KAMI")
    c.setFont(BOLD, 15)
    c.setFillColor(INK)
    c.drawString(M + 14, y - 47, "Google Business Profile")
    text_block(
        c,
        "Ise-setup or io-optimize namin ito para makita rin kayo ng customers na sila mismo yung naghahanap sa Google. Dito nila makikita ang service area or location, photos, business information, website, at genuine customer reviews.",
        M + 14,
        y - 70,
        W - 2 * M - 28,
        size=9.3,
        leading=12.6,
        color=TEXT,
    )

    y -= 154
    card(c, M, y - 104, W - 2 * M, 104, fill=NAVY, stroke=NAVY)
    c.setFont(BOLD, 15)
    c.setFillColor(WHITE)
    c.drawString(M + 18, y - 29, "Hindi na kailangan mag-scroll ang customer kung saan-saan.")
    text_block(
        c,
        "Ang trabaho ng foundation na ito ay gawing madali maintindihan ang business bago pa sila tumawag. Kapag malinaw ang page, website, at Google profile, mas kampante ang customer magtanong.",
        M + 18,
        y - 55,
        W - 2 * M - 36,
        size=9.3,
        leading=12.8,
        color=colors.HexColor("#D1D5DB"),
    )
    c.showPage()


def page_decision(c: canvas.Canvas) -> None:
    header(c, "Kayo Ang Hahawak Ng Inquiry", 3)
    y = page_title(
        c,
        "KAYO ang magpapalakas at kakausap sa customer",
        "Dito na papasok ang direct customer handling",
        "Kapag maayos na ang proof at naging interested na ang customer, ang next step ay simple: makita nila kayo, kontakin kayo, at makakuha ng malinaw na estimate.",
        H - 110,
    )

    card(c, M, y - 118, W - 2 * M, 118, fill=ORANGE_SOFT, stroke=colors.HexColor("#FED7AA"), accent=ORANGE)
    c.setFont(BOLD, 8.2)
    c.setFillColor(ORANGE)
    c.drawString(M + 16, y - 25, "KAYO")
    c.setFont(BOLD, 16)
    c.setFillColor(INK)
    c.drawString(M + 16, y - 50, "Facebook Boosting / Ads")
    text_block(
        c,
        "Kayo po yung magbo-boost or magra-run ng ads para mas mabilis ma-reach yung potential customers. Ang ilalabas natin ay actual projects, before-and-after, reviews, service locations, at content na may magandang proof.",
        M + 16,
        y - 75,
        W - 2 * M - 32,
        size=9.3,
        leading=12.5,
    )

    y -= 148
    col_w = (W - 2 * M - 16) / 2
    card(c, M, y - 120, col_w, 120, fill=BLUE_SOFT, stroke=colors.HexColor("#BBD7FF"), accent=BLUE)
    c.setFont(BOLD, 8.2)
    c.setFillColor(BLUE)
    c.drawString(M + 16, y - 25, "KAYO")
    c.setFont(BOLD, 15)
    c.setFillColor(INK)
    c.drawString(M + 16, y - 50, "Call / Message")
    text_block(
        c,
        "Kapag naging interested na yung customer at kumontak, kayo na po yung direktang kakausap sa kanila. Dapat madali ang next step: tumawag, mag-message, or magpa-estimate.",
        M + 16,
        y - 75,
        col_w - 32,
        size=9.1,
        leading=12.2,
    )

    card(c, M + col_w + 16, y - 120, col_w, 120, fill=WHITE, stroke=LINE, accent=colors.HexColor("#F59E0B"))
    c.setFont(BOLD, 8.2)
    c.setFillColor(colors.HexColor("#F59E0B"))
    c.drawString(M + col_w + 32, y - 25, "KAYO")
    c.setFont(BOLD, 15)
    c.setFillColor(INK)
    c.drawString(M + col_w + 32, y - 50, "Estimate / Closing")
    text_block(
        c,
        "Kayo po yung magbibigay ng estimate, pricing, schedule, at magha-handle ng final closing ng project. Dito na papasok ang actual decision ng customer.",
        M + col_w + 32,
        y - 75,
        col_w - 32,
        size=9.1,
        leading=12.2,
    )

    y -= 154
    c.setFont(BOLD, 13)
    c.setFillColor(INK)
    c.drawString(M, y, "Ang gusto nating pumasok na inquiry:")
    y -= 30
    statements = [
        ("May actual need.", BLUE),
        ("Alam na ang ginagawa ninyo.", CYAN),
        ("Nakita na ang proof.", GREEN),
        ("Alam kung covered ang location nila.", ORANGE),
        ("Mas ready nang magtanong: Pwede po ba magpa-estimate?", BLUE),
    ]
    for idx, (statement, color) in enumerate(statements):
        if idx == 4:
            x = M
            row = 2
            w = W - 2 * M
        else:
            x = M + (idx % 2) * (col_w + 16)
            row = idx // 2
            w = col_w
        card(c, x, y - 42 - row * 54, w, 42, fill=WHITE, accent=color)
        c.setFont(BOLD, 9.7)
        c.setFillColor(INK)
        c.drawString(x + 16, y - 25 - row * 54, statement)
    c.showPage()


def page_proof_flywheel(c: canvas.Canvas) -> None:
    header(c, "Bawat Project Nagiging Proof", 4)
    y = page_title(
        c,
        "Kapag may natapos na project, huwag nating sayangin ang proof",
        "Ito ang magpapalakas sa buong system",
        "Bawat magandang project pwedeng gamitin ulit. Pwede siyang maging bagong photos, before-and-after, Facebook content, Google photos, website project, at customer review.",
        H - 110,
    )

    card(c, M, y - 140, W - 2 * M, 140, fill=NAVY, stroke=NAVY)
    c.setFont(BOLD, 13)
    c.setFillColor(CYAN)
    c.drawString(M + 16, y - 28, "Mula sa completed project, gumawa tayo ng:")
    items = [
        ("Photos", ORANGE),
        ("Before and after", CYAN),
        ("Facebook post", BLUE),
        ("Google photos", GREEN),
        ("Website sample", colors.HexColor("#3B82F6")),
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
    c.drawString(M, y, "Saan ulit siya gagamitin?")
    y -= 92
    col_w = (W - 2 * M - 24) / 4
    for i, (eyebrow, name, body, color) in enumerate([
        ("KAMI", "FB Page", "Mas maraming post na may tunay na gawa.", BLUE),
        ("KAMI", "Google", "Mas updated ang photos at reviews.", GREEN),
        ("KAMI", "Landing Page", "Mas maraming sample na pwedeng makita.", CYAN),
        ("KAYO", "Ads", "Mas madaling paniwalaan ang susunod na ads.", ORANGE),
    ]):
        feature_card(c, M + i * (col_w + 8), y, col_w, 80, eyebrow, name, body, color)

    y -= 26
    card(c, M, y - 88, W - 2 * M, 88, fill=GREEN_SOFT, stroke=colors.HexColor("#BBF7D0"), accent=GREEN)
    c.setFont(BOLD, 15)
    c.setFillColor(colors.HexColor("#047857"))
    c.drawString(M + 16, y - 28, "Ito yung dahilan kung bakit lumalakas over time.")
    text_block(
        c,
        "Habang mas dumadami ang natapos na trabaho, mas dumadami rin ang patunay. Kapag mas marami ang patunay, mas madali para sa susunod na customer na magtiwala, magtanong, at magpa-estimate.",
        M + 16,
        y - 53,
        W - 2 * M - 32,
        size=9.5,
        leading=13,
    )
    c.showPage()


def page_rollout(c: canvas.Canvas) -> None:
    header(c, "Step By Step Na Gagawin", 5)
    y = page_title(
        c,
        "Yun po yung system na irerecommend naming buuin",
        "Hindi kailangan lahat gawin agad",
        "Ang importante, malinaw kung ano ang unang aayusin, ano ang palalakasin, sino ang hahawak ng inquiry, at paano gagamitin ang bawat completed project para makatulong makuha ang next opportunity.",
        H - 110,
    )

    phases = [
        ("01", "KAMI", "Ayusin muna ang foundation", "Facebook Page, landing page, Google Business Profile, contact buttons, at existing proof.", BLUE),
        ("02", "KAYO", "Palakasin ang pag-abot sa tao", "Mag-boost or mag-run ng ads gamit ang actual projects, reviews, locations, at clear na offers.", ORANGE),
        ("03", "KAYO", "Kausapin ang interested customers", "Sagutin ang calls/messages, alamin ang kailangan, at tulungan silang makapagpa-estimate.", CYAN),
        ("04", "KAYO", "Estimate at closing", "Ibigay ang pricing, schedule, estimate, at final details para ma-close ang potential project.", colors.HexColor("#F59E0B")),
        ("05", "KAMI + KAYO", "Gawing bagong proof ang project", "Gamitin ang completed project sa photos, reviews, Facebook, Google, website, at future ads.", GREEN),
    ]
    for num, owner, title, body, color in phases:
        card(c, M, y - 72, W - 2 * M, 72, fill=WHITE, accent=color)
        c.setFillColor(color)
        c.circle(M + 27, y - 35, 13, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont(BOLD, 8.5)
        c.drawCentredString(M + 27, y - 38, num)
        c.setFont(BOLD, 7.8)
        c.setFillColor(color)
        c.drawString(M + 52, y - 20, owner)
        c.setFont(BOLD, 13)
        c.setFillColor(INK)
        c.drawString(M + 52, y - 37, title)
        text_block(c, body, M + 52, y - 55, W - 2 * M - 72, size=8.8, leading=11.5, color=TEXT, max_lines=2)
        y -= 82

    y -= 2
    card(c, M, y - 112, W - 2 * M, 112, fill=NAVY, stroke=NAVY)
    c.setFont(BOLD, 14)
    c.setFillColor(ORANGE)
    c.drawString(M + 18, y - 30, "Pinakasimpleng paliwanag")
    c.setFont(BOLD, 18)
    c.setFillColor(WHITE)
    c.setFont(BOLD, 16)
    for line_no, line in enumerate(wrap("Hindi lang mas maraming messages. Mas maraming tamang inquiries.", BOLD, 16, W - 2 * M - 36)):
        c.drawString(M + 18, y - 57 - line_no * 20, line)
    text_block(
        c,
        "Mas maraming customer na may actual need, mas may tiwala bago magtanong, at mas ready magpa-estimate dahil nakita na nila ang gawa, services, lugar na covered, at paano kayo kokontakin.",
        M + 18,
        y - 92,
        W - 2 * M - 36,
        size=8.5,
        leading=11.2,
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
    c.setTitle("We Forge Web - Inirerekomendang Sistema Para Sa Tamang Inquiries")
    c.setAuthor("We Forge Web")
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
