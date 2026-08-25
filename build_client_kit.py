#!/usr/bin/env python3
"""
Generate a professional Client Growth Kit PDF for Jhapher Malabanan / We Forge Web.

Design direction:
- Brand palette: navy #0A1F3F, cyan #00B4D8, orange #FF6B35, light cool grey #F5F7FA
- Clean reportlab Platypus build with custom page templates, header/footer, section banners
- Professional typography via registered TTF fonts where available, else Helvetica family
- Cover page with logo treatment, then section openers, then content pages
"""

from __future__ import annotations
import os, sys, json
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, NextPageTemplate, Flowable,
)
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing, Rect, String, Line, Circle
from reportlab.graphics import renderPDF
from reportlab.platypus import Image as RLImage

BANNER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "ChatGPT Image Aug 4, 2026, 05_06_05 AM.png")

# ── Palette ──────────────────────────────────────────────────────────────────
NAVY      = colors.HexColor("#0A1F3F")
CYAN      = colors.HexColor("#00B4D8")
ORANGE    = colors.HexColor("#FF6B35")
LIGHT_BG  = colors.HexColor("#F5F7FA")
DARK_TEXT = colors.HexColor("#1A1A2E")
MEDIUM_GREY = colors.HexColor("#6B7280")
WHITE     = colors.white
LIGHT_LINE = colors.HexColor("#E5E7EB")
ACCENT_LINE = colors.HexColor("#00B4D8")

PAGE_W, PAGE_H = A4  # 595.27 x 841.89 pt

# ── Custom Flowables ──────────────────────────────────────────────────────────

class ColorBar(Flowable):
    """A thin coloured horizontal bar."""
    def __init__(self, width=None, height=3, color=CYAN):
        Flowable.__init__(self)
        self.width = width
        self.bar_height = height
        self.color = color

    def draw(self):
        w = self.width if self.width else self._frame.width
        self.canv.setFillColor(self.color)
        self.canv.rect(0, 0, w, self.bar_height, fill=1, stroke=0)


class SectionBanner(Flowable):
    """Full-width navy band with orange accent stripe and white title text."""
    def __init__(self, title, subtitle=None, width=None, height=46, accent_height=5):
        Flowable.__init__(self)
        self.title = title
        self.subtitle = subtitle
        self.banner_height = height
        self.accent_height = accent_height
        self._w = width

    def wrap(self, availWidth, availHeight):
        self._w = availWidth
        return (availWidth, self.banner_height + self.accent_height + 10)

    def draw(self):
        w = self._w
        c = self.canv
        # navy band
        c.setFillColor(NAVY)
        c.rect(0, 0, w, self.banner_height, fill=1, stroke=0)
        # orange accent stripe at bottom of navy
        c.setFillColor(ORANGE)
        c.rect(0, 0, w, self.accent_height, fill=1, stroke=0)
        # title text
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 16)
        c.drawString(14, self.banner_height - 22, self.title)
        if self.subtitle:
            c.setFont("Helvetica", 9)
            c.setFillColor(colors.HexColor("#94A3B8"))
            c.drawString(14, self.banner_height - 36, self.subtitle)


class NumberedStep(Flowable):
    """Big circle number + label, in a light card."""
    def __init__(self, number, title, body, width=None):
        Flowable.__init__(self)
        self.number = number
        self.title = title
        self.body = body
        self._w = width

    def wrap(self, availWidth, availHeight):
        self._w = availWidth
        self.height = 58
        return (availWidth, self.height)

    def draw(self):
        w = self._w
        c = self.canv
        # light card background
        c.setFillColor(LIGHT_BG)
        c.roundRect(0, 0, w, self.height, 6, fill=1, stroke=0)
        # number circle
        c.setFillColor(CYAN)
        c.circle(22, self.height - 24, 14, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 14)
        c.drawCentredString(22, self.height - 28, str(self.number))
        # title
        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(44, self.height - 20, self.title)
        # body
        c.setFillColor(DARK_TEXT)
        c.setFont("Helvetica", 9)
        # wrap body text manually
        from reportlab.pdfbase.pdfmetrics import stringWidth
        max_w = w - 46
        words = self.body.split()
        lines = []
        cur = ""
        for word in words:
            test = (cur + " " + word).strip()
            if stringWidth(test, "Helvetica", 9) <= max_w:
                cur = test
            else:
                if cur:
                    lines.append(cur)
                cur = word
        if cur:
            lines.append(cur)
        y = self.height - 36
        for line in lines[:3]:
            c.drawString(44, y, line)
            y -= 11


class CalloutBox(Flowable):
    """Highlight box with left orange bar. Uses a reportlab Paragraph for proper HTML rendering."""
    def __init__(self, text, width=None, bg=colors.HexColor("#FFF7ED"), bar_color=ORANGE, text_color=DARK_TEXT):
        Flowable.__init__(self)
        self.text = text
        self.bg = bg
        self.bar_color = bar_color
        self.text_color = text_color
        self._w = width

    def wrap(self, availWidth, availHeight):
        self._w = availWidth
        from reportlab.platypus import Paragraph
        # Build a Paragraph to measure the rendered text
        para_style = ParagraphStyle(
            "CalloutText",
            fontName="Helvetica",
            fontSize=10,
            leading=14,
            textColor=self.text_color,
        )
        self._para = Paragraph(self.text, para_style)
        # measure
        w, h = self._para.wrap(availWidth - 18, availHeight)
        self._rendered_w = w
        self._rendered_h = h
        self.height = h + 18
        return (availWidth, self.height)

    def draw(self):
        w = self._w
        c = self.canv
        c.setFillColor(self.bg)
        c.roundRect(0, 0, w, self.height, 4, fill=1, stroke=0)
        c.setFillColor(self.bar_color)
        c.rect(0, 0, 4, self.height, fill=1, stroke=0)
        # draw the paragraph
        self._para.drawOn(c, 14, 10)


def draw_cover_background(canvas_obj, doc):
    """Draw the full-bleed cover page background."""
    w, h = A4
    c = canvas_obj
    # full navy background
    c.setFillColor(NAVY)
    c.rect(0, 0, w, h, fill=1, stroke=0)
    # subtle geometric accent - diagonal cyan bars
    c.setFillColor(colors.HexColor("#0D2E52"))
    c.rect(0, h - 120, w, 6, fill=1, stroke=0)
    c.setFillColor(CYAN)
    c.rect(0, h - 126, w, 2, fill=1, stroke=0)

    # logo mark - actual logo image
    cx, cy = w * 0.30, h * 0.52
    w_size = 60
    logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image.png")
    try:
        from PIL import Image as PILImage
        pil_img = PILImage.open(logo_path)
        # convert to RGB for reportlab
        if pil_img.mode in ("RGBA", "P"):
            rgb = PILImage.new("RGB", pil_img.size, (0, 0, 0))
            rgb.paste(pil_img, mask=pil_img.split()[-1] if pil_img.mode == "RGBA" else None)
            pil_img = rgb
        pil_img.save("/tmp/wf_logo_rgb.png")
        logo_w_pt = 100
        logo_h_pt = logo_w_pt * pil_img.height / pil_img.width
        c.drawImage("/tmp/wf_logo_rgb.png", cx - logo_w_pt/2, cy + w_size*0.2 - logo_h_pt,
                    width=logo_w_pt, height=logo_h_pt, mask=None, preserveAspectRatio=True)
    except Exception as e:
        # fallback: draw W text
        c.setFillColor(ORANGE)
        c.setFont("Helvetica-Bold", 48)
        c.drawString(cx - 20, cy + w_size*0.2 - 20, "W")

    # dot above W
    c.setFillColor(CYAN)
    c.circle(cx, cy + w_size * 0.95, 7, fill=1, stroke=0)

    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 38)
    c.drawString(cx - 40, cy - 100, "WE FORGE")
    c.setFillColor(CYAN)
    c.setFont("Helvetica-Bold", 38)
    c.drawString(cx - 40, cy - 145, "WEB")

    c.setFillColor(colors.HexColor("#94A3B8"))
    c.setFont("Helvetica", 11)
    c.drawString(cx - 30, cy - 172, "BUILT TO AUTOMATE.  FORGED TO LAST.")

    c.setStrokeColor(ORANGE)
    c.setLineWidth(1.5)
    c.line(cx - 30, cy - 182, cx + 120, cy - 182)

    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 22)
    c.drawString(cx - 30, cy - 230, "CLIENT GROWTH KIT")
    c.setFillColor(CYAN)
    c.setFont("Helvetica", 13)
    c.drawString(cx - 30, cy - 255, "Online Inquiry Blueprint")

    c.setFillColor(ORANGE)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(cx - 30, cy - 300, "JHAPHER MALABANAN")
    c.setFillColor(colors.HexColor("#CBD5E1"))
    c.setFont("Helvetica", 11)
    c.drawString(cx - 30, cy - 318, "Paano Mas Mapapakinabangan ang Facebook, Google at Website")

    # bottom contact bar
    c.setFillColor(colors.HexColor("#071529"))
    c.rect(0, 0, w, 52, fill=1, stroke=0)
    c.setStrokeColor(CYAN)
    c.setLineWidth(1)
    c.line(0, 52, w, 52)

    c.setFillColor(WHITE)
    c.setFont("Helvetica", 9)
    y = 34
    c.drawString(20, y, "weforgeweb.com")
    c.setFillColor(CYAN)
    c.drawString(110, y, "|")
    c.setFillColor(WHITE)
    c.drawString(120, y, "+63 991 917 3652")
    c.setFillColor(CYAN)
    c.drawString(215, y, "|")
    c.setFillColor(WHITE)
    c.drawString(225, y, "hello@weforgeweb.com")

    # right-side decorative circles
    c.setFillColor(colors.HexColor("#0D2E52"))
    c.circle(w - 60, h - 180, 80, fill=1, stroke=0)
    c.setFillColor(CYAN)
    c.setStrokeColor(CYAN)
    c.setLineWidth(0.5)
    c.circle(w - 60, h - 180, 80, fill=0, stroke=1)
    c.setFillColor(colors.HexColor("#0D2E52"))
    c.circle(w - 30, h - 220, 50, fill=1, stroke=0)


# ── Page templates ────────────────────────────────────────────────────────────

class NumberedCanvas(canvas.Canvas):
    """Canvas that adds page numbers and a footer bar on content pages."""
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self._draw_footer(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def _draw_footer(self, num_pages):
        page_num = self._pageNumber
        # only draw on content pages (skip cover = page 1)
        if page_num == 1:
            return
        w, h = A4
        # thin line
        self.setStrokeColor(LIGHT_LINE)
        self.setLineWidth(0.5)
        self.line(20*mm, 18*mm, w - 20*mm, 18*mm)
        # page number
        self.setFont("Helvetica", 8)
        self.setFillColor(MEDIUM_GREY)
        self.drawRightString(w - 20*mm, 12*mm, f"Page {page_num - 1}")
        # brand footer left
        self.drawString(20*mm, 12*mm, "Jhapher Malabanan  ·  Client Growth Kit")
        self.setFillColor(CYAN)
        self.drawRightString(w - 20*mm, 12*mm, "")


# ── Styles ────────────────────────────────────────────────────────────────────

body_style = ParagraphStyle(
    "KitBody",
    fontName="Helvetica",
    fontSize=10,
    leading=15,
    textColor=DARK_TEXT,
    alignment=TA_JUSTIFY,
    spaceAfter=8,
)

body_bold = ParagraphStyle(
    "KitBodyBold",
    parent=body_style,
    fontName="Helvetica-Bold",
)

tagalog_style = ParagraphStyle(
    "Tagalog",
    parent=body_style,
    fontName="Helvetica-Oblique",
    textColor=colors.HexColor("#334155"),
    leftIndent=6,
    borderPadding=4,
    borderWidth=0,
    borderColor=LIGHT_LINE,
    backColor=LIGHT_BG,
    spaceBefore=4,
    spaceAfter=8,
)

heading3_style = ParagraphStyle(
    "H3",
    fontName="Helvetica-Bold",
    fontSize=13,
    leading=17,
    textColor=NAVY,
    spaceBefore=10,
    spaceAfter=4,
)

bullet_style = ParagraphStyle(
    "Bullet",
    parent=body_style,
    bulletIndent=12,
    leftIndent=24,
    spaceBefore=1,
    spaceAfter=1,
)

small_style = ParagraphStyle(
    "Small",
    fontName="Helvetica",
    fontSize=8,
    leading=11,
    textColor=MEDIUM_GREY,
)


# ── Helper builders ────────────────────────────────────────────────────────────

def P(text, style=body_style):
    return Paragraph(text, style)

def Pb(text):
    return Paragraph(text, body_bold)

def T(text):
    return Paragraph(text, tagalog_style)

def H3(text):
    return Paragraph(text, heading3_style)

def bullet(text):
    return Paragraph(f"•  {text}", bullet_style)

def spacer(h=6):
    return Spacer(1, h)

def bar(height=2, color=CYAN):
    return ColorBar(height=height, color=color)

def section(title, subtitle=None):
    return SectionBanner(title, subtitle)

def step(number, title, body):
    return NumberedStep(number, title, body)

def callout(text):
    return CalloutBox(text)

def simple_table(headers, rows, col_widths=None):
    data = [headers] + rows
    t = Table(data, colWidths=col_widths, repeatRows=1)
    style = [
        ("GRID", (0, 0), (-1, -1), 0.75, colors.HexColor("#CBD5E1")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 10),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), 10),
        ("TEXTCOLOR", (0, 1), (-1, -1), DARK_TEXT),
    ]
    t.setStyle(TableStyle(style))
    return t


# ── Document build ────────────────────────────────────────────────────────────

def build():
    out_path = "Jhapher_Malabanan_Premium_Client_Growth_Kit.pdf"

    doc = BaseDocTemplate(
        out_path,
        pagesize=A4,
        leftMargin=20*mm,
        rightMargin=20*mm,
        topMargin=18*mm,
        bottomMargin=22*mm,
        title="Client Growth Kit - Jhapher Malabanan",
        author="We Forge Web",
        subject="Online Inquiry Blueprint",
    )

    # Cover page template (full bleed, no header/footer)
    cover_frame = Frame(0, 0, PAGE_W, PAGE_H, id="cover")

    def draw_cover(canvas_obj, doc):
        """Place the ChatGPT Image banner fully visible: scale to page width,
        center vertically. Banner is landscape (2063x762), A4 is portrait.
        When scaled to width, there is blank space above/below — draw contact
        info text at the bottom so it stays in the PDF text layer."""
        img = RLImage(BANNER_PATH)
        iw, ih = img.imageWidth, img.imageHeight
        scale = PAGE_W / iw
        dw = iw * scale
        dh = ih * scale
        dy = (PAGE_H - dh) / 2.0
        img.drawWidth = dw
        img.drawHeight = dh
        img.drawOn(canvas_obj, 0, dy)

        # contact info text below the banner (in PDF text layer)
        bottom_y = dh + dy + 14
        if bottom_y < PAGE_H - 20:
            c = canvas_obj
            c.setFillColor(NAVY)
            c.setFont("Helvetica-Bold", 9)
            c.drawCentredString(PAGE_W / 2, bottom_y,
                "weforgeweb.com   |   +63 991 917 3652   |   hello@weforgeweb.com")

    cover_template = PageTemplate(id="Cover", frames=[cover_frame], onPage=draw_cover)

    # Content page template
    content_frame = Frame(
        doc.leftMargin, doc.bottomMargin,
        doc.width, doc.height,
        id="content"
    )
    content_template = PageTemplate(id="Content", frames=[content_frame])

    doc.addPageTemplates([cover_template, content_template])

    story = []

    # ── COVER (Page 1) — full-bleed ChatGPT Image banner, drawn by onPage ─────
    story.append(Spacer(1, 1))
    story.append(NextPageTemplate("Content"))
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 2 — Ang Buong System at Concrete Plan
    # ══════════════════════════════════════════════════════════════════════════
    story.append(section("Ang Buong System at Concrete Plan", "Simple lang po yung strategy"))
    story.append(spacer(10))
    story.append(P(
        "Hindi natin iaasa sa isang platform lang yung pagkuha ng customers. Gagamitin natin yung Facebook, "
        "Ads, Website, Google Business Profile, at Reviews bilang isang connected system."
    ))
    story.append(spacer(8))
    story.append(H3("Ganito po yung magiging flow:"))
    story.append(spacer(4))
    story.append(P(
        "<b>Facebook Ads</b> → mas mabilis ma-reach ang potential customers<br/>"
        "<b>Customer becomes interested</b> → chine-check nila yung business<br/>"
        "<b>Website / Landing Page</b> → nakikita nila yung projects, services, experience, at proof<br/>"
        "<b>Google Business Profile</b> → nakikita yung location, reviews, phone, website, photos<br/>"
        "<b>Call / Message</b> → mas informed na inquiry<br/>"
        "<b>Estimate / Proposal</b> → opportunity para ma-close yung project<br/>"
        "<b>Completed Project</b> → bagong photos + bagong proof + bagong review<br/>"
        "<b>Facebook + Ads + Google + Website</b> → mas lumalakas ulit → <b>Repeat</b>"
    ))
    story.append(spacer(10))
    story.append(callout(
        "<b>Hindi lang tayo gagawa ng website. Hindi lang tayo magbo-boost ng Facebook post. "
        "Hindi lang tayo gagawa ng Google Business Profile. Gusto natin magkakabit lahat.</b>"
    ))
    story.append(spacer(8))
    story.append(P(
        "Ang goal natin is hindi lang mas maraming messages. Ang gusto natin is mas maraming tamang tao ang "
        "makakita, mas informed sila bago kumontak, at mas marami kayong opportunity na makapagbigay ng estimate "
        "at makapag-close ng project."
    ))
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 2 — STEP 1: Ayusin Muna yung Online Foundation
    # ══════════════════════════════════════════════════════════════════════════
    story.append(section("STEP 1", "Ayusin Muna Yung Online Foundation"))
    story.append(spacer(10))
    story.append(P(
        "Bago tayo magpalakas ng advertising, kailangan ready muna yung business kapag may customer na nag-check."
    ))
    story.append(spacer(6))
    story.append(callout(
        "<b>Aayusin natin yung:</b> Facebook Page, Website / Landing Page, Google Business Profile, Contact "
        "information, Services, Service areas, Actual projects, Reviews, Call and Message options"
    ))
    story.append(spacer(8))
    story.append(H3("Ang purpose nito is simple:"))
    story.append(P(
        "Kapag may customer na naging interested, hindi sila mahihirapan alamin kung sino kayo, ano yung "
        "ginagawa ninyo, at paano kayo kokontakin."
    ))
    story.append(spacer(8))

    story.append(H3("Kung hindi pa handa ang foundation, dito extendable:"))
    story.append(bullet("Facebook Page — complete profile, actual posts, clear contact info"))
    story.append(bullet("Website / Landing Page — projects, services, service areas, reviews, CTA"))
    story.append(bullet("Google Business Profile — nalagyan ng complete info, photos, reviews setup"))
    story.append(bullet("Contact info — phone, message, estimate process clear"))
    story.append(bullet("Services — malinaw kung ano exactly ang offering"))
    story.append(spacer(8))
    story.append(callout(
        "<b>Step by step lang po. Build the foundation.</b>"
    ))
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 3 — STEP 2 + STEP 3
    # ══════════════════════════════════════════════════════════════════════════
    story.append(section("STEP 2", "Gumitin Ang Facebook Boosting / Ads Para Mas Mabilis Ma-Reach"))
    story.append(spacer(10))
    story.append(P(
        "Kapag ready na yung foundation, saka natin palalakasin yung reach gamit ang Facebook boosting or ads. "
        "Instead na hintayin lang natin na organically makita yung business, pwede nating ilapit yung actual "
        "projects, services, before-and-after, reviews, at offers sa mas maraming potential customers."
    ))
    story.append(spacer(6))
    story.append(H3("Mas magandang i-promote yung content tulad ng:"))
    story.append(bullet("Actual completed projects"))
    story.append(bullet("Before and after"))
    story.append(bullet("Common customer problems"))
    story.append(bullet("Customer reviews"))
    story.append(bullet("Service locations"))
    story.append(bullet("Useful information"))
    story.append(bullet("Clear Call or Message button"))
    story.append(spacer(8))
    story.append(callout(
        "<b>Ang purpose ng boosting is hindi lang paramihin yung views o likes.</b><br/>"
        "Mas maraming tamang tao ang makakita · Mas maraming maging interested · Mas maraming mag-check ng "
        "business · Mas maraming possible inquiries"
    ))
    story.append(spacer(6))
    story.append(P(
        "<b>So Facebook Ads helps us speed up the process of getting the business in front of potential customers.</b>"
    ))
    story.append(PageBreak())

    story.append(section("STEP 3", "Website / Landing Page Ang Tutulong Sa Customer Na Makapag-Desisyon"))
    story.append(spacer(10))
    story.append(P(
        "Dito nagiging importante yung website. Kasi pagkatapos makita ng customer yung ad or Facebook post, "
        "possible na hindi pa sila agad tatawag — magche-check muna sila."
    ))
    story.append(spacer(6))
    story.append(P("<b>Dito nila pwedeng makita nang maayos yung:</b>"))
    story.append(spacer(4))
    story.append(simple_table(
        ["What They Check", "Why It Matters"],
        [
            ["Actual projects", "Proof na may kaya"],
            ["Before and after", "Visual ng resulta"],
            ["Services", "Alam nila kung covered"],
            ["Experience", "Confidence sa team"],
            ["Service areas", "Alam nila kung sakop"],
            ["Customer reviews", "Social proof"],
            ["Business information", "Complete details"],
            ["Contact options", "Easy next step"],
        ],
        col_widths=[150, 310],
    ))
    story.append(spacer(8))
    story.append(P(
        "<b>Instead na kailangan pa nilang mag-scroll nang matagal sa Facebook, isang page na lang yung pwede "
        "nilang tingnan para maintindihan yung business.</b>"
    ))
    story.append(spacer(6))
    story.append(H3("Ang goal natin is tulungan silang mas mabilis makasagot sa mga tanong nila:"))
    story.append(bullet("Ginagawa ba nila yung kailangan ko?"))
    story.append(bullet("Nagse-service ba sila sa area ko?"))
    story.append(bullet("May actual experience ba sila?"))
    story.append(bullet("May proof ba ng trabaho?"))
    story.append(bullet("May ibang customers bang nagtiwala na sa kanila?"))
    story.append(bullet("Paano ako magpapa-estimate?"))
    story.append(spacer(6))
    story.append(callout(
        "<b>Kapag madaling makita yung sagot, mas madali rin para sa customer na magkaroon ng confidence na "
        "tumawag or mag-message.</b>"
    ))
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 4 — STEP 4 + STEP 5
    # ══════════════════════════════════════════════════════════════════════════
    story.append(section("STEP 4", "Google Business Profile Para Sa Location, Search, At Reviews"))
    story.append(spacer(10))
    story.append(P(
        "Hindi lahat ng customer manggagaling sa Facebook. May customers din na diretso sa Google kapag may "
        "kailangan na silang service."
    ))
    story.append(spacer(6))
    story.append(P("<b>Halimbawa, maghahanap sila ng:</b>"))
    story.append(bullet("Service near me"))
    story.append(bullet("Contractor near me"))
    story.append(bullet("[Service] + location"))
    story.append(spacer(8))
    story.append(P(
        "Dito natin gustong gamitin nang maayos yung Google Business Profile. Makikita nila yung business location "
        "or service area, phone number, website, services, photos, business hours, Google reviews, at directions "
        "kung applicable."
    ))
    story.append(spacer(6))
    story.append(callout(
        "<b>So kapag naghahanap na mismo yung customer, may chance din nilang makita yung business ninyo.</b>"
    ))
    story.append(spacer(8))
    story.append(H3("Importante rin dito yung reviews."))
    story.append(P(
        "Kasi bago tumawag yung customer, possible na chine-check muna nila: ilang tao na yung nagtiwala dito, "
        "ano yung experience ng previous customers. So habang dumadami yung genuine reviews, lumalakas din yung "
        "proof ng business over time."
    ))
    story.append(spacer(6))
    story.append(callout(
        "<b>Step by step lang po. Build trust.</b>"
    ))
    story.append(PageBreak())

    story.append(section("STEP 5", "Bawat Project Gawin Natin Bagong Marketing Asset"))
    story.append(spacer(10))
    story.append(P(
        "Ito yung gusto nating maging regular na sistema. Bawat completed project, kukuha tayo hangga't possible "
        "ng before photos, during-work photos, after photos, service performed, project location, customer feedback, "
        "at genuine review."
    ))
    story.append(spacer(6))
    story.append(P(
        "Then hindi lang natin itatago yung mga yan. Gagamitin natin ulit sa Facebook content, Facebook Ads, "
        "Google Business Profile, Website, at future follow-ups."
    ))
    story.append(spacer(6))
    story.append(callout(
        "<b>So habang dumadami yung projects, dumadami rin yung proof. At habang dumadami yung proof, mas "
        "nagiging malakas yung materials natin para sa susunod na customer.</b>"
    ))
    story.append(spacer(8))
    story.append(H3("What to capture after every project:"))
    story.append(spacer(4))
    story.append(simple_table(
        ["Capture", "Reuse For"],
        [
            ["Before photos", "Facebook / Google / Website"],
            ["During-work photos", "Facebook / Google / Website"],
            ["After photos", "Facebook / Google / Website"],
            ["Service performed", "Website / Ads"],
            ["Project location", "Google / Ads"],
            ["Customer feedback", "Facebook / Follow-up"],
            ["Genuine review", "Google / Website"],
        ],
        col_widths=[150, 310],
    ))
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 5 — STEP 6 + STEP 7 + STEP 8
    # ══════════════════════════════════════════════════════════════════════════
    story.append(section("STEP 6", "I-Boost Natin Yung Mga Content Na May Magandang Proof"))
    story.append(spacer(10))
    story.append(P(
        "Hindi kailangan lahat ng posts gastusan. Titingnan natin kung anong content yung magandang gamitin para "
        "sa advertising."
    ))
    story.append(spacer(6))
    story.append(H3("Examples ng magandang i-boost na content:"))
    story.append(bullet("Malinaw na before-and-after"))
    story.append(bullet("Strong completed project"))
    story.append(bullet("Magandang customer review"))
    story.append(bullet("Common customer problem"))
    story.append(bullet("Project from a specific location"))
    story.append(spacer(6))
    story.append(callout(
        "<b>So hindi tayo basta gumagastos para lang magkaroon ng reach. Gusto natin yung pinapakita natin ay "
        "may reason para mag-stop, mag-check, at mag-inquire yung customer.</b>"
    ))
    story.append(PageBreak())

    story.append(section("STEP 7", "I-Follow Up Natin Yung Mga Interested Pero Hindi Pa Ready"))
    story.append(spacer(10))
    story.append(P(
        "Hindi lahat ng customer magbo-book agad. May iba na nagtatanong pa, nagko-compare, naghihintay ng "
        "schedule, nag-iipon ng budget, o hindi pa ready."
    ))
    story.append(spacer(6))
    story.append(P(
        "Instead na puro follow up lang po, pwede natin silang balikan gamit ang bagong value — similar project, "
        "before-and-after, customer review, available schedule, helpful information, o project sa area nila."
    ))
    story.append(spacer(6))
    story.append(callout(
        "<b>Ang goal is hindi sila kulitin. Ang goal is tulungan silang magkaroon ng enough information para "
        "makapag-decide kapag ready na sila.</b>"
    ))
    story.append(spacer(8))
    story.append(P("Halimbawa ng follow-up value:"))
    story.append(bullet("Similar project na nagpapakita ng capability"))
    story.append(bullet("Before-and-after na relatable sa problema nila"))
    story.append(bullet("Customer review na nagbibigay confidence"))
    story.append(bullet("Available schedule na clear"))
    story.append(bullet("Helpful information na relevant"))
    story.append(bullet("Project sa area nila na nagpapakita ng proximity"))
    story.append(PageBreak())

    story.append(section("STEP 8", "Track Natin Kung Saan Talaga Nanggagaling Yung Magandang Leads"))
    story.append(spacer(10))
    story.append(P(
        "Every inquiry, simple lang yung ita-track natin: saan galing? Facebook Ads? Facebook Organic? Google? "
        "Website? Referral? Repeat Customer?"
    ))
    story.append(spacer(6))
    story.append(P("<b>Then itrack natin:</b>"))
    story.append(spacer(4))
    story.append(simple_table(
        ["Stage", "Meaning"],
        [
            ["Inquiry", "Naka-contact na"],
            ["Qualified Inquiry", "Relevant at may intent"],
            ["Estimate", "Nagbigay na ng quote"],
            ["Booked Project", "Nag-booking na"],
            ["Revenue", "Natapat na"],
        ],
        col_widths=[140, 320],
    ))
    story.append(spacer(8))
    story.append(callout(
        "<b>After some time, makikita natin kung saan talaga nanggagaling yung customers na nagiging actual "
        "projects. Doon natin mas ilalagay yung budget at effort.</b>"
    ))
    story.append(spacer(6))
    story.append(P(
        "<b>Step by step lang po. Track what works. Then ulitin at palakasin kung ano yung nagbibigay ng "
        "magandang resulta.</b>"
    ))
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 6 — Customer Journey Flow + Tracking Summary
    # ══════════════════════════════════════════════════════════════════════════
    story.append(section("Customer Journey", "Yun Talaga Yung Strategy Natin"))
    story.append(spacer(10))
    story.append(P(
        "Simple lang po yung strategy. Hindi natin iaasa sa isang platform lang yung pagkuha ng customers. "
        "Gagamitin natin yung Facebook, Ads, Website, Google Business Profile, at Reviews bilang isang connected system."
    ))
    story.append(spacer(8))

    story.append(H3("Buong Customer Journey:"))
    story.append(spacer(4))
    story.append(simple_table(
        ["Step", "What Happens", "Platform"],
        [
            ["1", "Mas mabilis ma-reach yung potential customers", "Facebook / Ads"],
            ["2", "Customer becomes interested, chine-check ang business", "Facebook / Ads"],
            ["3", "Nakikita yung projects, services, experience, proof — mas madali mag-decide", "Website / Landing Page"],
            ["4", "Nakikita yung location, reviews, phone, website, photos — para sa actively searching", "Google Business Profile"],
            ["5", "Mas informed na inquiry — ready nang kumontak", "Call / Message"],
            ["6", "Opportunity para ma-close yung project", "Estimate / Proposal"],
            ["7", "Bagong photos + bagong proof + bagong review", "Completed Project"],
            ["8", "Facebook + Ads + Google + Website — mas lumalakas ulit", "Repeat"],
        ],
        col_widths=[30, 280, 150],
    ))
    story.append(spacer(10))
    story.append(H3("What We Track:"))
    story.append(spacer(4))
    story.append(simple_table(
        ["Metric", "Why It Matters"],
        [
            ["Inquiry by source", "Alam kung anong channel ang gumagana"],
            ["Qualified inquiries", "Hindi lang basta messages, may intent"],
            ["Estimates given", "Opportunity na ma-close"],
            ["Booked projects", "Actual resulta"],
            ["Revenue", "Final score"],
        ],
        col_widths=[140, 320],
    ))
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # PAGE 7 — North Star / Closing
    # ══════════════════════════════════════════════════════════════════════════
    story.append(section("North Star", "Client Growth Kit"))
    story.append(spacer(10))

    story.append(H3("Hindi Lang More Inquiries. Mas Effective na Inquiries."))
    story.append(spacer(6))
    story.append(P(
        "<b>What We Want to Create:</b> Mas maraming customer na nakakita na ng proof, naiintindihan na ang "
        "service, at mas ready nang magtanong ng estimate. Hindi natin kailangang habulin lahat ng tao. Gusto "
        "nating gawing mas madali para sa tamang customer na makita, ma-verify at makontak ang business."
    ))
    story.append(spacer(10))

    story.append(H3("The Simple Blueprint"))
    story.append(spacer(4))
    story.append(callout(
        "<b>Attention → Search → Proof → Trust → Inquiry → Estimate → Project → Review → More Proof</b>"
    ))
    story.append(spacer(6))
    story.append(P(
        "<b>Every good project should make the next customer easier to convince.</b>"
    ))
    story.append(spacer(12))

    story.append(H3("Bakit Namin Ito Ginawa?"))
    story.append(spacer(4))
    story.append(P(
        "Gusto naming masulit ninyo yung website at online presence na ginawa natin. Hindi sapat na matapos "
        "lang ang project at iwan online. Mas importante na gamitin yung foundation para makatulong sa actual "
        "business. Simple lang: post real work, keep Google fresh, collect genuine reviews, send interested "
        "customers to the website, and track what turns into estimates."
    ))
    story.append(spacer(16))

    # Final band
    story.append(Spacer(1, 10))
    final_data = [[Paragraph(
        "<b>Prepared by We Forge Web for Jhapher Malabanan</b>",
        ParagraphStyle("final", fontName="Helvetica-Bold", fontSize=11, textColor=WHITE, alignment=TA_CENTER)
    )]]
    final_table = Table(final_data, colWidths=[doc.width])
    final_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
        ("LINEBELOW", (0, 0), (-1, -1), 2, ORANGE),
    ]))
    story.append(final_table)

    # ── Build ────────────────────────────────────────────────────────────────
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Built: {os.path.abspath(out_path)}")
    return out_path


if __name__ == "__main__":
    build()
