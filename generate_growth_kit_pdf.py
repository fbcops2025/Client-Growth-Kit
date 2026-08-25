#!/usr/bin/env python3
"""
We Forge Web - Master Client Growth Kit Playbook
Designed as a premium, client-facing strategy document with a restrained
editorial layout, crisp hierarchy, and print-safe visual polish.
"""

import os
import base64
from playwright.sync_api import sync_playwright
import fitz

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO_PATH = os.path.join(SCRIPT_DIR, "image.png")
BANNER_PATH = os.path.join(SCRIPT_DIR, "ChatGPT Image Aug 4, 2026, 05_06_05 AM.png")

with open(LOGO_PATH, "rb") as f:
    logo_base64 = base64.b64encode(f.read()).decode("utf-8")
logo_data_uri = f"data:image/png;base64,{logo_base64}"

with open(BANNER_PATH, "rb") as f:
    banner_base64 = base64.b64encode(f.read()).decode("utf-8")
banner_data_uri = f"data:image/png;base64,{banner_base64}"

HTML_CONTENT = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>We Forge Web - Client Growth Kit Master Playbook</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=Outfit:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
  @page {{
    size: A4 portrait;
    margin: 0;
  }}
  *, *::before, *::after {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}
  body {{
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    color: #1E293B;
    background-color: #F8FAFC;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
    font-size: 10px;
    line-height: 1.5;
  }}

  /* Exact A4 Canvas (210mm x 297mm) */
  .page {{
    width: 210mm;
    height: 297mm;
    max-height: 297mm;
    position: relative;
    page-break-after: always;
    page-break-inside: avoid;
    overflow: hidden;
    background: #FFFFFF;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}

  /* Page Header */
  .page-header {{
    height: 16mm;
    padding: 0 16mm;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1.5px solid #E2E8F0;
    background: #FFFFFF;
    flex-shrink: 0;
  }}
  .header-brand-wrap {{
    display: flex;
    align-items: center;
    gap: 11px;
  }}
  .header-logo {{
    width: 28px;
    height: 28px;
    border-radius: 7px;
  }}
  .header-brand-title {{
    font-family: 'Outfit', sans-serif;
    font-size: 14px;
    font-weight: 800;
    letter-spacing: 0.5px;
    color: #0A1F3F;
    line-height: 1;
  }}
  .header-brand-title span {{
    color: #00B4D8;
  }}
  .header-subtag {{
    font-size: 8.5px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    color: #64748B;
    margin-top: 2px;
  }}
  .header-section-badge {{
    font-size: 9px;
    font-weight: 700;
    color: #475569;
    letter-spacing: 0.4px;
    text-transform: uppercase;
    background: #F1F5F9;
    padding: 4.5px 11px;
    border-radius: 5px;
    border: 1px solid #E2E8F0;
  }}

  /* Page Footer */
  .page-footer {{
    height: 14mm;
    padding: 0 16mm;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-top: 1.5px solid #E2E8F0;
    background: #FAFAFC;
    font-size: 9px;
    color: #64748B;
    flex-shrink: 0;
  }}
  .footer-left {{
    font-weight: 600;
    color: #475569;
  }}
  .footer-links {{
    display: flex;
    align-items: center;
    gap: 14px;
  }}
  .footer-links span.dot {{
    color: #CBD5E1;
  }}
  .footer-contact {{
    font-weight: 700;
    color: #0A1F3F;
  }}
  .footer-page-num {{
    font-weight: 800;
    color: #0077B6;
    background: #F0F9FF;
    padding: 3.5px 10px;
    border-radius: 4px;
    border: 1px solid #BAE6FD;
  }}

  /* Page Content Container */
  .page-content {{
    flex: 1;
    padding: 9.5mm 16mm 9mm 16mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 10px;
    overflow: hidden;
  }}

  /* Typography */
  h1, h2, h3, h4 {{
    font-family: 'Outfit', sans-serif;
    color: #0A1F3F;
    line-height: 1.2;
  }}
  
  .section-tag {{
    display: inline-flex;
    align-items: center;
    gap: 5px;
    font-size: 8.5px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    color: #0077B6;
    background: #F0F9FF;
    padding: 3.5px 10px;
    border-radius: 4px;
    border: 1px solid #BAE6FD;
    width: fit-content;
    margin-bottom: 3px;
  }}

  .page-title {{
    font-size: 19px;
    font-weight: 800;
    color: #0A1F3F;
    margin-bottom: 2px;
    letter-spacing: -0.4px;
  }}
  .page-subtitle {{
    font-size: 9.8px;
    color: #64748B;
    margin-bottom: 3px;
    font-weight: 400;
    line-height: 1.45;
  }}

  /* Grid Layouts */
  .grid-2 {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
  }}
  .grid-3 {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 9px;
  }}
  .grid-4 {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    gap: 8px;
  }}

  /* Cards */
  .card {{
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 7px;
    padding: 10px 13px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.02);
  }}
  .card.navy {{
    background: #0A1F3F;
    color: #FFFFFF;
    border-color: #1E3A8A;
  }}
  .card.cyan-accent {{
    background: #F8FAFC;
    border-left: 4px solid #00B4D8;
  }}
  .card.orange-accent {{
    background: #F8FAFC;
    border-left: 4px solid #FF6B35;
  }}
  .card.green-accent {{
    background: #F8FAFC;
    border-left: 4px solid #10B981;
  }}
  .card.blue-accent {{
    background: #F8FAFC;
    border-left: 4px solid #3B82F6;
  }}

  /* Step Header Bars */
  .step-header {{
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 5px;
  }}
  .step-badge {{
    width: 26px;
    height: 26px;
    border-radius: 7px;
    background: #0A1F3F;
    color: #FFFFFF;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Outfit', sans-serif;
    font-weight: 800;
    font-size: 12.5px;
    flex-shrink: 0;
  }}
  .step-badge.orange {{ background: #FF6B35; }}
  .step-badge.cyan {{ background: #00B4D8; }}
  
  .step-title-text {{
    font-size: 13.5px;
    font-weight: 800;
    color: #0A1F3F;
    line-height: 1.22;
  }}
  .step-title-sub {{
    font-size: 8.8px;
    color: #64748B;
  }}

  /* Lists */
  .clean-list {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 4px;
  }}
  .clean-list li {{
    display: flex;
    align-items: flex-start;
    gap: 6px;
    font-size: 9.2px;
    color: #334155;
    line-height: 1.38;
  }}
  .check-icon {{
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: #ECFDF5;
    color: #059669;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 7.5px;
    font-weight: 900;
    flex-shrink: 0;
    margin-top: 1.5px;
  }}
  .check-icon.blue {{ background: #EFF6FF; color: #2563EB; }}
  .check-icon.orange {{ background: #FFF7ED; color: #EA580C; }}

  /* Quotes & Callouts */
  .quote-box {{
    background: #F8FAFC;
    border-left: 4px solid #00B4D8;
    border-top: 1px solid #E2E8F0;
    border-right: 1px solid #E2E8F0;
    border-bottom: 1px solid #E2E8F0;
    padding: 8.5px 12px;
    border-radius: 6px;
    font-size: 9px;
    color: #1E293B;
    font-style: italic;
    line-height: 1.44;
  }}

  /* Funnel Pipeline Visuals */
  .funnel-container {{
    display: flex;
    flex-direction: column;
    gap: 5px;
  }}
  .funnel-row {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 6.5px 12px;
    border-radius: 6px;
    border: 1px solid #E2E8F0;
    background: #FFFFFF;
  }}
  .funnel-row.s1 {{ border-left: 4px solid #00B4D8; }}
  .funnel-row.s2 {{ border-left: 4px solid #0284C7; }}
  .funnel-row.s3 {{ border-left: 4px solid #3B82F6; }}
  .funnel-row.s4 {{ border-left: 4px solid #F59E0B; }}
  .funnel-row.s5 {{ border-left: 4px solid #10B981; background: #F0FDF4; border-color: #BBF7D0; }}

  /* Cover Page Styling: Full-Bleed Proportions */
  .page-cover {{
    background: radial-gradient(circle at 85% 15%, #0F2D5C 0%, #061325 70%);
    color: #FFFFFF;
    position: relative;
    padding: 16mm 16mm 14mm 16mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .page-cover::after {{
    content: "";
    position: absolute;
    top: 0;
    right: 0;
    width: 160mm;
    height: 160mm;
    background: radial-gradient(circle, rgba(0,180,216,0.15) 0%, rgba(255,107,53,0.06) 50%, transparent 70%);
    pointer-events: none;
  }}
  .cover-top {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    z-index: 2;
  }}
  .cover-logo-wrapper {{
    display: flex;
    align-items: center;
    gap: 13px;
  }}
  .cover-logo-img {{
    width: 52px;
    height: 52px;
    border-radius: 12px;
    box-shadow: 0 4px 16px rgba(0, 180, 216, 0.4);
  }}
  .cover-brand-title {{
    font-family: 'Outfit', sans-serif;
    font-size: 26px;
    font-weight: 900;
    letter-spacing: 1px;
    color: #FFFFFF;
    line-height: 1;
  }}
  .cover-brand-title span {{
    color: #00B4D8;
  }}
  .cover-brand-motto {{
    font-size: 8.8px;
    font-weight: 700;
    letter-spacing: 2px;
    color: #94A3B8;
    margin-top: 3px;
    text-transform: uppercase;
  }}
  .cover-edition-tag {{
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.2);
    padding: 5px 13px;
    border-radius: 30px;
    font-size: 8.5px;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: #38BDF8;
  }}

  .cover-hero {{
    z-index: 2;
    display: flex;
    flex-direction: column;
    gap: 11px;
    margin: auto 0;
  }}
  .cover-pill {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(255, 107, 53, 0.15);
    border: 1px solid rgba(255, 107, 53, 0.4);
    color: #FF8A50;
    padding: 4px 13px;
    border-radius: 20px;
    font-size: 8.8px;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
    width: fit-content;
  }}
  .cover-main-title {{
    font-family: 'Outfit', sans-serif;
    font-size: 38px;
    font-weight: 900;
    line-height: 1.05;
    letter-spacing: -0.8px;
    color: #FFFFFF;
  }}
  .cover-main-title span {{
    color: #00B4D8;
    display: block;
  }}
  .cover-description {{
    font-size: 11.2px;
    line-height: 1.55;
    color: #CBD5E1;
    max-width: 175mm;
  }}

  .cover-pillars-container {{
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 9px;
    padding: 11px 13px;
  }}
  .cover-pillars-header {{
    font-family: 'Outfit', sans-serif;
    font-size: 10.5px;
    font-weight: 800;
    color: #38BDF8;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    margin-bottom: 7px;
  }}
  .cover-pillars-grid {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8px;
  }}
  .cover-pillar-card {{
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 6px;
    padding: 8px 9px;
  }}
  .cover-pillar-num {{
    font-family: 'Outfit', sans-serif;
    font-size: 12.5px;
    font-weight: 900;
    color: #FF6B35;
    margin-bottom: 2px;
  }}
  .cover-pillar-title {{
    font-size: 9.8px;
    font-weight: 800;
    color: #FFFFFF;
    margin-bottom: 2px;
  }}
  .cover-pillar-desc {{
    font-size: 8px;
    color: #94A3B8;
    line-height: 1.3;
  }}

  /* Executive Deliverables Checklist on Cover */
  .cover-highlights-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 9px;
  }}
  .cover-highlight-box {{
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.09);
    border-radius: 7px;
    padding: 9px 11px;
  }}
  .cover-highlight-title {{
    font-size: 9px;
    font-weight: 800;
    color: #38BDF8;
    margin-bottom: 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  .cover-highlight-list {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 3px;
    font-size: 8px;
    color: #CBD5E1;
  }}

  /* Executive Implementation Commitments */
  .cover-commitments-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    gap: 8px;
  }}
  .cover-commit-card {{
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 6px;
    padding: 7px 8.5px;
  }}
  .cover-commit-title {{
    font-size: 8.5px;
    font-weight: 800;
    color: #FF8A50;
    margin-bottom: 2px;
  }}
  .cover-commit-desc {{
    font-size: 7.6px;
    color: #CBD5E1;
    line-height: 1.28;
  }}

  .cover-footer {{
    z-index: 2;
    border-top: 1px solid rgba(255, 255, 255, 0.12);
    padding-top: 6mm;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }}
  .cover-author-block {{
    display: flex;
    flex-direction: column;
  }}
  .cover-author-title {{
    font-size: 7.8px;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #94A3B8;
  }}
  .cover-author-name {{
    font-family: 'Outfit', sans-serif;
    font-size: 13px;
    font-weight: 800;
    color: #FFFFFF;
  }}
  .cover-contact-list {{
    display: flex;
    gap: 15px;
    font-size: 9px;
    color: #CBD5E1;
  }}

  .tag-label {{
    font-size: 7.2px;
    font-weight: 800;
    padding: 2px 5px;
    border-radius: 3px;
    background: #E2E8F0;
    color: #334155;
    text-transform: uppercase;
    display: inline-block;
  }}
  .tag-label.blue {{ background: #DBEAFE; color: #1E40AF; }}
  .tag-label.orange {{ background: #FFEDD5; color: #C2410C; }}
  .tag-label.green {{ background: #DCFCE7; color: #166534; }}
  .tag-label.cyan {{ background: #E0F2FE; color: #0369A1; }}

  /* Premium client-report refinement layer */
  body {{
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Inter', 'Plus Jakarta Sans', 'Segoe UI', sans-serif;
    color: #1D1D1F;
    background: #F5F5F7;
    font-size: 10.4px;
    line-height: 1.55;
  }}

  .page {{
    background: linear-gradient(180deg, #FFFFFF 0%, #FBFBFD 100%);
  }}

  .page-header {{
    height: 17mm;
    padding: 0 16mm;
    border-bottom: 1px solid #DADCE0;
    background: rgba(255, 255, 255, 0.94);
  }}

  .header-logo {{
    width: 30px;
    height: 30px;
    border-radius: 8px;
    box-shadow: 0 1px 6px rgba(0, 0, 0, 0.12);
  }}

  .header-brand-title,
  .cover-brand-title,
  .cover-author-name,
  .page-title,
  .step-title-text {{
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Outfit', 'Segoe UI', sans-serif;
    letter-spacing: 0;
  }}

  .header-brand-title {{
    color: #111827;
    font-size: 13.5px;
    font-weight: 800;
  }}

  .header-brand-title span,
  .cover-brand-title span,
  .cover-main-title span {{
    color: #0071E3;
  }}

  .header-subtag {{
    color: #6E6E73;
    letter-spacing: 0.7px;
    font-weight: 700;
  }}

  .header-section-badge {{
    color: #424245;
    background: #F5F5F7;
    border: 1px solid #D2D2D7;
    border-radius: 8px;
    padding: 5px 12px;
    letter-spacing: 0.5px;
  }}

  .page-content {{
    padding: 12mm 16mm 11mm 16mm;
    justify-content: flex-start;
    gap: 12px;
  }}

  .section-tag {{
    color: #0071E3;
    background: #F5F9FF;
    border: 1px solid #BBD7FF;
    border-radius: 8px;
    padding: 4px 11px;
    letter-spacing: 0.9px;
    margin-bottom: 5px;
  }}

  .page-title {{
    color: #111827;
    font-size: 20.5px;
    font-weight: 800;
    line-height: 1.16;
    margin-bottom: 4px;
  }}

  .page-subtitle {{
    color: #5F6B7A;
    font-size: 10.2px;
    line-height: 1.5;
    max-width: 170mm;
  }}

  .grid-2 {{ gap: 12px; }}
  .grid-3 {{ gap: 11px; }}
  .grid-4 {{ gap: 9px; }}

  .card {{
    border: 1px solid #DADCE0;
    border-radius: 8px;
    background: rgba(255, 255, 255, 0.96);
    box-shadow: 0 8px 22px rgba(15, 23, 42, 0.045);
  }}

  .card.navy {{
    background: #111827;
    border-color: #1F2937;
    box-shadow: 0 10px 28px rgba(17, 24, 39, 0.18);
  }}

  .card.cyan-accent,
  .card.blue-accent,
  .card.green-accent,
  .card.orange-accent {{
    background: #FFFFFF;
    border-top: 1px solid #DADCE0;
    border-right: 1px solid #DADCE0;
    border-bottom: 1px solid #DADCE0;
  }}

  .card.cyan-accent {{ border-left-color: #0071E3; }}
  .card.blue-accent {{ border-left-color: #3B82F6; }}
  .card.green-accent {{ border-left-color: #10B981; }}
  .card.orange-accent {{ border-left-color: #FF6B35; }}

  .clean-list li {{
    font-size: 9.35px;
    color: #334155;
    gap: 7px;
  }}

  .check-icon {{
    background: #F5F5F7;
    color: #0071E3;
    border: 1px solid #D2D2D7;
  }}

  .quote-box {{
    background: #F8FAFC;
    border-color: #DADCE0;
    border-left-color: #0071E3;
    border-radius: 8px;
    color: #334155;
  }}

  .page-footer {{
    height: 14mm;
    padding: 0 16mm;
    border-top: 1px solid #DADCE0;
    background: #F5F5F7;
    color: #6E6E73;
  }}

  .footer-left,
  .footer-contact {{
    color: #111827;
  }}

  .footer-page-num {{
    background: #FFFFFF;
    color: #0071E3;
    border: 1px solid #BBD7FF;
    border-radius: 8px;
  }}

  .page-cover {{
    background:
      linear-gradient(135deg, rgba(0, 113, 227, 0.12) 0%, rgba(255, 255, 255, 0) 42%),
      linear-gradient(180deg, #FFFFFF 0%, #F5F5F7 100%);
    color: #1D1D1F;
    padding: 16mm;
  }}

  .page-cover::after {{
    display: none;
  }}

  .cover-logo-img {{
    box-shadow: 0 10px 28px rgba(0, 0, 0, 0.16);
    border-radius: 12px;
  }}

  .cover-brand-title {{
    color: #111827;
    font-size: 25px;
    font-weight: 850;
  }}

  .cover-brand-motto,
  .cover-author-title,
  .cover-contact-list {{
    color: #6E6E73;
  }}

  .cover-edition-tag {{
    color: #0071E3;
    background: #FFFFFF;
    border: 1px solid #BBD7FF;
    box-shadow: 0 8px 24px rgba(0, 113, 227, 0.08);
    border-radius: 8px;
  }}

  .cover-pill {{
    color: #B45309;
    background: #FFF7ED;
    border: 1px solid #FED7AA;
    border-radius: 8px;
  }}

  .cover-main-title {{
    color: #111827;
    font-size: 39px;
    font-weight: 850;
    letter-spacing: 0;
  }}

  .cover-description {{
    color: #515154;
    font-size: 11.4px;
    max-width: 172mm;
  }}

  .cover-pillars-container,
  .cover-highlight-box,
  .cover-commit-card {{
    background: rgba(255, 255, 255, 0.94);
    border: 1px solid #DADCE0;
    box-shadow: 0 12px 30px rgba(15, 23, 42, 0.06);
  }}

  .cover-pillars-header,
  .cover-highlight-title {{
    color: #0071E3;
  }}

  .cover-pillar-card {{
    background: #F8FAFC;
    border: 1px solid #E5E7EB;
    border-radius: 8px;
  }}

  .cover-pillar-num,
  .cover-commit-title {{
    color: #FF6B35;
  }}

  .cover-pillar-title,
  .cover-author-name {{
    color: #111827;
  }}

  .cover-pillar-desc,
  .cover-highlight-list,
  .cover-commit-desc {{
    color: #515154;
  }}

  .cover-footer {{
    border-top: 1px solid #DADCE0;
  }}

  .cover-system-loop {{
    background: #FFFFFF;
    border: 1px solid #DADCE0;
    border-radius: 8px;
    padding: 8px 12px;
    box-shadow: 0 12px 30px rgba(15, 23, 42, 0.06);
  }}

  .cover-system-loop-title {{
    font-size: 9px;
    font-weight: 800;
    color: #0071E3;
    letter-spacing: 0.6px;
    text-transform: uppercase;
    margin-bottom: 5px;
  }}

  .cover-system-loop-grid {{
    gap: 7px;
    font-size: 7.8px;
    color: #515154;
  }}

  .cover-system-loop-step {{
    background: #F8FAFC;
    padding: 6px 8px;
    border-radius: 7px;
  }}

  .cover-system-loop-step strong {{
    color: #111827 !important;
  }}

  .cover-assurance {{
    background: #EAF4FF;
    border: 1px solid #BBD7FF;
    border-radius: 8px;
    padding: 9px 13px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }}

  .cover-assurance-text {{
    font-size: 8.5px;
    color: #334155;
    max-width: 132mm;
  }}

  .cover-assurance-label {{
    font-size: 8px;
    font-weight: 800;
    color: #0071E3;
    letter-spacing: 0.5px;
    text-transform: uppercase;
  }}

  .tag-label {{
    border-radius: 6px;
    letter-spacing: 0.5px;
  }}
</style>
</head>
<body>

  <!-- ================= PAGE 1: MASTER COVER PAGE ================= -->
  <div class="page page-cover">
    <div class="cover-top">
      <div class="cover-logo-wrapper">
        <img class="cover-logo-img" src="{logo_data_uri}" alt="We Forge Web Logo">
        <div>
          <div class="cover-brand-title">WE FORGE <span>WEB</span></div>
          <div class="cover-brand-motto">Built to Automate • Forged to Last</div>
        </div>
      </div>
      <div class="cover-edition-tag">Universal Strategic Playbook</div>
    </div>

    <div class="cover-hero">
      <div class="cover-pill">Client Acquisition & Revenue Infrastructure</div>
      <div class="cover-main-title">
        CLIENT GROWTH KIT
        <span>The Connected Acquisition System</span>
      </div>
      <div class="cover-description">
        Isang komprehensibo at napatunayang sistema na nag-uugnay sa <strong>Facebook Ads, Google Business Profile, Conversion Website,</strong> at <strong>Project Proof Flywheel</strong> upang makakuha ng tuluy-tuloy na agos ng qualified inquiries, mataas na closing rate ng estimates, at predictable na kita sa anumang industriya.
      </div>

      <!-- Core Pillars Overview Box -->
      <div class="cover-pillars-container">
        <div class="cover-pillars-header">⚡ Ang 4 na Pangunahing Haligi ng Sistemang Ito:</div>
        <div class="cover-pillars-grid">
          <div class="cover-pillar-card">
            <div class="cover-pillar-num">01. Foundation</div>
            <div class="cover-pillar-title">Online Readiness</div>
            <div class="cover-pillar-desc">Buo at kagalang-galang na profile sa Facebook, Google, at Website bago mag-ads.</div>
          </div>
          <div class="cover-pillar-card">
            <div class="cover-pillar-num">02. Attention</div>
            <div class="cover-pillar-title">Proof-Based Ads</div>
            <div class="cover-pillar-desc">Mabilis na reach gamit ang totoong resulta, trabaho, at before-and-after.</div>
          </div>
          <div class="cover-pillar-card">
            <div class="cover-pillar-num">03. Trust Hub</div>
            <div class="cover-pillar-title">Conversion Website</div>
            <div class="cover-pillar-desc">Nasasagot ang 6 na customer questions upang makapag-desisyon silang kumontak.</div>
          </div>
          <div class="cover-pillar-card">
            <div class="cover-pillar-num">04. Flywheel</div>
            <div class="cover-pillar-title">Asset Machine</div>
            <div class="cover-pillar-desc">Bawat natapos na proyekto ay nagiging patunay para sa susunod na kliyente.</div>
          </div>
        </div>
      </div>

      <!-- Executive Strategic Highlights Grid (3 Columns) -->
      <div class="cover-highlights-grid">
        <div class="cover-highlight-box">
          <div class="cover-highlight-title">🎯 Revenue Focus</div>
          <ul class="cover-highlight-list">
            <li>• Inaalis ang budget burn sa bogus inquiries.</li>
            <li>• 24/7 automated qualification machine.</li>
            <li>• Makabuluhang pagtaas sa closing rate ng estimates.</li>
          </ul>
        </div>
        <div class="cover-highlight-box">
          <div class="cover-highlight-title">🌐 Universal Scope</div>
          <ul class="cover-highlight-list">
            <li>• <strong>Contractors:</strong> Solar, Renovation, Build.</li>
            <li>• <strong>Clinics:</strong> Dental, Medical, Aesthetic.</li>
            <li>• <strong>B2B:</strong> Legal, Accounting, Consulting.</li>
          </ul>
        </div>
        <div class="cover-highlight-box">
          <div class="cover-highlight-title">⚙️ Full-Funnel Stack</div>
          <ul class="cover-highlight-list">
            <li>• Hyper-Local FB Paid Ads.</li>
            <li>• Google Maps local search visibility.</li>
            <li>• Sub-3s Lead Capture Website.</li>
          </ul>
        </div>
      </div>

      <!-- System Operational Loop Infographic -->
      <div class="cover-system-loop">
        <div class="cover-system-loop-title">
          🔄 ANG 3-STEP REVENUE GENERATION CYCLE:
        </div>
        <div class="grid-3 cover-system-loop-grid">
          <div class="cover-system-loop-step" style="border-left: 2.5px solid #FF6B35;">
            <strong style="color: #FFF;">1. Demand Generation:</strong> Hyper-targeted Facebook ads & Google Search capture.
          </div>
          <div class="cover-system-loop-step" style="border-left: 2.5px solid #00B4D8;">
            <strong style="color: #FFF;">2. Trust Verification:</strong> 30-second website decision engine & Google reviews.
          </div>
          <div class="cover-system-loop-step" style="border-left: 2.5px solid #10B981;">
            <strong style="color: #FFF;">3. Value Follow-Up:</strong> Structured nurturing scripts & revenue tracking.
          </div>
        </div>
      </div>

      <!-- Executive Implementation Commitments Grid -->
      <div class="cover-commitments-grid">
        <div class="cover-commit-card">
          <div class="cover-commit-title">01. Turnkey Setup</div>
          <div class="cover-commit-desc">Maayos at mabilisang deployment sa loob ng 7–14 araw nang walang abala sa operasyon.</div>
        </div>
        <div class="cover-commit-card">
          <div class="cover-commit-title">02. 100% Ownership</div>
          <div class="cover-commit-desc">Sa inyo nakapangalan ang domain, assets, page, at customer database.</div>
        </div>
        <div class="cover-commit-card">
          <div class="cover-commit-title">03. Weekly Metrics</div>
          <div class="cover-commit-desc">Malinaw na weekly report ng leads, cost-per-estimate, at pipeline.</div>
        </div>
        <div class="cover-commit-card">
          <div class="cover-commit-title">04. Dedicated Team</div>
          <div class="cover-commit-desc">May eksperto kayong katuwang sa patuloy na pag-scale at optimization.</div>
        </div>
      </div>

      <!-- Executive Assurance Box -->
      <div class="cover-assurance">
        <div class="cover-assurance-text">
          💡 <em>"Hindi natin iaasa sa isang platform lang ang paglago ng negosyo. Gagawa tayo ng isang konektadong makina na nagtatrabaho 24/7."</em>
        </div>
        <div class="cover-assurance-label">100% Actionable Blueprint</div>
      </div>
    </div>

    <div class="cover-footer">
      <div class="cover-author-block">
        <div class="cover-author-title">Engineered & Presented By</div>
        <div class="cover-author-name">WE FORGE WEB • CLIENT ACQUISITION TEAM</div>
      </div>
      <div class="cover-contact-list">
        <div>🌐 weforgeweb.com</div>
        <div>📞 +63 991 917 3652</div>
        <div>✉️ hello@weforgeweb.com</div>
      </div>
    </div>
  </div>

  <!-- ================= PAGE 2: STRATEGIC PHILOSOPHY & ARCHITECTURE ================= -->
  <div class="page">
    <div class="page-header">
      <div class="header-brand-wrap">
        <img class="header-logo" src="{logo_data_uri}" alt="Logo">
        <div>
          <div class="header-brand-title">WE FORGE <span>WEB</span></div>
          <div class="header-subtag">Client Growth Kit</div>
        </div>
      </div>
      <div class="header-section-badge">Core Strategy & Architecture</div>
    </div>

    <div class="page-content">
      <div>
        <div class="section-tag">Strategic Foundations</div>
        <div class="page-title">Bakit Hindi Dapat Iaasa sa Isang Platform Lang?</div>
        <div class="page-subtitle">Ang pinakamalaking pagkakamali ng karamihan sa mga negosyo ay ang pag-asa sa isang marketing source lamang (tulad ng organic Facebook posts o referral). Narito kung bakit isang Connected Ecosystem ang kailangan mo upang lumago nang tuluy-tuloy.</div>
      </div>

      <!-- Problem vs Solution Comparison Matrix -->
      <div class="grid-2">
        <div class="card" style="border-left: 4px solid #EF4444; background: #FEF2F2;">
          <div style="font-size: 10.5px; font-weight: 800; color: #991B1B; margin-bottom: 4px;">❌ ANG DISCONNECTED & RISKY TRAP</div>
          <ul class="clean-list">
            <li><strong>Umaasa sa Algorithmic Luck:</strong> Kapag bumaba ang reach ng organic Facebook, biglang walang pumapasok na inquiries.</li>
            <li><strong>Walang Centralized Trust Hub:</strong> Nahihirapan ang customer mag-scroll sa libu-libong lumang posts para alamin ang serbisyo.</li>
            <li><strong>Nawawalang High-Intent Searchers:</strong> Hindi nakikita sa Google kapag naghahanap ang kliyente ng agarang serbisyo.</li>
            <li><strong>Sayang ang Completed Projects:</strong> Natatapos ang trabaho nang hindi nado-dokumento bilang bagong marketing assets.</li>
            <li><strong>Walang Follow-Up System:</strong> Maraming inquiries ang nawawala dahil walang structured value nurturing.</li>
          </ul>
        </div>

        <div class="card" style="border-left: 4px solid #10B981; background: #F0FDF4;">
          <div style="font-size: 10.5px; font-weight: 800; color: #065F46; margin-bottom: 4px;">✅ ANG WE FORGE WEB CONNECTED SYSTEM</div>
          <ul class="clean-list">
            <li><strong>Omni-Channel Lead Capture:</strong> Sinasalo ng Google at Website ang attention na ginagawa ng Facebook Ads.</li>
            <li><strong>1-Click Decision Landing Page:</strong> Malinaw na portfolio, testimonials, credentials, at direct estimate buttons.</li>
            <li><strong>Local Google Search Dominance:</strong> Diretso kayong makikita sa Google Maps ng mga taong handa nang bumili.</li>
            <li><strong>Self-Feeding Marketing Flywheel:</strong> Bawat natapos na proyekto ay nagiging bagong ad campaign at website proof.</li>
            <li><strong>Data-Backed ROI Tracking:</strong> Alam mo bawat buwan kung aling channel ang nagpapasok ng pinakamalaking kita.</li>
          </ul>
        </div>
      </div>

      <!-- Connected System Bridge & Architectural Overview -->
      <div class="card cyan-accent" style="background: #F0F9FF; border: 1px solid #BAE6FD;">
        <div style="font-size: 10px; font-weight: 800; color: #0077B6; margin-bottom: 3px; font-family: 'Outfit', sans-serif;">
          🔗 INTEGRATED MULTI-CHANNEL ENGINE (PAANO NAG-UUGNAY ANG 4 NA HALIGI):
        </div>
        <div style="font-size: 8.3px; color: #334155; line-height: 1.38;">
          Tulad ng binalangkas sa panimula, ang <strong>Online Foundation (Pillar 1)</strong> at <strong>Proof-Based Ads (Pillar 2)</strong> ang nagbubukas ng target reach; ang <strong>Conversion Website & Google Business Profile (Pillar 3)</strong> ang nag-aalis ng pag-aalinlangan bago mag-inquire; at ang bawat natapos na gawa ay awtomatikong pumapasok sa <strong>Asset Flywheel (Pillar 4)</strong> upang palakasin ang susunod na marketing cycle nang hindi lumolobo ang ad spend.
        </div>
      </div>

      <!-- The 3 Pillars of High Closing Rates -->
      <div class="card" style="background: #F8FAFC; border: 1px solid #E2E8F0;">
        <div style="font-size: 9.8px; font-weight: 800; color: #0A1F3F; margin-bottom: 3px;">🏆 ANG 3 ELEMENTO PARA SA MATAAS NA CLOSING RATE NG ESTIMATES:</div>
        <div class="grid-3" style="gap: 8px;">
          <div>
            <strong>1. Clarity (Kalinawan):</strong><br>
            <span style="font-size: 8px; color: #475569;">Madaling maintindihan ang serbisyo, proseso, at timeframe nang walang nakatagong detalye.</span>
          </div>
          <div>
            <strong>2. Proof (Patunay):</strong><br>
            <span style="font-size: 8px; color: #475569;">Nakikita ang tunay na gawa, reviews ng kapitbahay, at aktwal na transformed projects.</span>
          </div>
          <div>
            <strong>3. Speed (Bilis ng Aksyon):</strong><br>
            <span style="font-size: 8px; color: #475569;">1-click call, agarang estimate response, at propesyonal na onboarding workflow.</span>
          </div>
        </div>
      </div>

      <!-- ROI Pipeline Economics Table -->
      <div class="card" style="background: #F0F9FF; border: 1px solid #BAE6FD;">
        <div style="font-size: 9.5px; font-weight: 800; color: #0077B6; margin-bottom: 3px;">📈 ANG PIPELINE ECONOMICS MATRIX (SAMPLE FLOW):</div>
        <div class="grid-4" style="gap: 7px; font-size: 7.8px; color: #0369A1; text-align: center;">
          <div style="background: #FFF; padding: 5px 6px; border-radius: 5px; border: 1px solid #BAE6FD;">
            <strong>100 Inquiries</strong><br><span style="color: #64748B;">From Ads & Google</span>
          </div>
          <div style="background: #FFF; padding: 5px 6px; border-radius: 5px; border: 1px solid #BAE6FD;">
            <strong>40 Qualified</strong><br><span style="color: #64748B;">Budget & Area Match</span>
          </div>
          <div style="background: #FFF; padding: 5px 6px; border-radius: 5px; border: 1px solid #BAE6FD;">
            <strong>20 Estimates Sent</strong><br><span style="color: #64748B;">Detailed Proposals</span>
          </div>
          <div style="background: #FFF; padding: 5px 6px; border-radius: 5px; border: 1px solid #BAE6FD;">
            <strong>8–12 Closed Deals</strong><br><span style="color: #059669; font-weight: 800;">High ROI Growth</span>
          </div>
        </div>
      </div>

      <!-- The Strategic Metric Shift -->
      <div class="card" style="background: #FFFFFF; border: 1px solid #E2E8F0;">
        <div style="font-size: 9.5px; font-weight: 800; color: #0A1F3F; margin-bottom: 2px;">📊 ANG BAGONG METRICS NG TAGUMPAY:</div>
        <div style="font-size: 8.5px; color: #334155; line-height: 1.36;">
          Hindi tayo tumitingin sa <em>vanity metrics</em> tulad ng page likes, viral views, o simpleng heart reactions. Ang sinusukat natin ay: <strong>(1) Bilang ng Qualified Inquiries, (2) Bilang ng Naipadalang Estimates/Proposals, (3) Closing Rate ng Saradong Proyekto, at (4) Net Return on Ad Spend (ROAS).</strong>
        </div>
      </div>

      <!-- Strategic North Star Banner -->
      <div class="card navy" style="display: flex; align-items: center; justify-content: space-between; padding: 10px 14px;">
        <div style="max-width: 125mm;">
          <div style="font-size: 10px; font-weight: 800; color: #38BDF8; font-family: 'Outfit', sans-serif;">🎯 ANG ATING NORTH STAR: QUALIFIED LEADS & CLOSED PROJECTS</div>
          <div style="font-size: 8.2px; color: #CBD5E1; margin-top: 2px; line-height: 1.34;">
            Hindi tayo naghahanap ng simpleng likes. Ang layunin natin ay: <strong>Tamang tao ang makakita ➔ Mas may tiwala bago mag-message ➔ Mas mataas ang conversion rate ng estimates tungo sa saradong kontrata.</strong>
          </div>
        </div>
        <div style="background: #FF6B35; color: #FFF; font-weight: 800; font-size: 8.2px; padding: 5.5px 11px; border-radius: 5px; white-space: nowrap; margin-left: 10px;">
          PREDICTABLE GROWTH
        </div>
      </div>
    </div>

    <div class="page-footer">
      <div class="footer-left">We Forge Web • Client Growth Kit</div>
      <div class="footer-links">
        <span class="footer-contact">weforgeweb.com</span>
        <span class="dot">•</span>
        <span>+63 991 917 3652</span>
      </div>
      <div class="footer-page-num">Page 2 of 7</div>
    </div>
  </div>

  <!-- ================= PAGE 3: STEP 1 & STEP 2 ================= -->
  <div class="page">
    <div class="page-header">
      <div class="header-brand-wrap">
        <img class="header-logo" src="{logo_data_uri}" alt="Logo">
        <div>
          <div class="header-brand-title">WE FORGE <span>WEB</span></div>
          <div class="header-subtag">Phase 1: Foundation & Demand</div>
        </div>
      </div>
      <div class="header-section-badge">Step 1 & Step 2</div>
    </div>

    <div class="page-content">
      <!-- STEP 1 -->
      <div style="display: flex; flex-direction: column; gap: 7px;">
        <div class="step-header">
          <div class="step-badge">1</div>
          <div>
            <div class="step-title-text">STEP 1: Ayusin Muna ang Online Foundation Bago Mag-Ads</div>
            <div class="step-title-sub">Bago tayo magpalakas ng advertising, kailangang 100% handa at kagalang-galang ang business kapag may customer na nag-check.</div>
          </div>
        </div>

        <div class="grid-2">
          <div class="card orange-accent">
            <div style="font-size: 9.8px; font-weight: 800; color: #0A1F3F; margin-bottom: 3px;">🛠️ ANG FOUNDATION AUDIT CHECKLIST:</div>
            <ul class="clean-list">
              <li><span class="check-icon orange">✓</span> <strong>Facebook Business Page:</strong> High-res logo, branded banner cover, updated business description, and active CTA buttons (Call/Message).</li>
              <li><span class="check-icon orange">✓</span> <strong>Google Business Profile (GBP):</strong> Exact location pin, verified service radius, business hours, and phone connectivity.</li>
              <li><span class="check-icon orange">✓</span> <strong>Conversion Landing Page:</strong> Mobile-friendly, sub-3-second load speed, clear service packages, and direct booking options.</li>
              <li><span class="check-icon orange">✓</span> <strong>Unified Contact Channels:</strong> Clickable phone calls, WhatsApp/Viber direct links, and a simple inquiry form.</li>
            </ul>
          </div>

          <div class="card cyan-accent">
            <div style="font-size: 9.8px; font-weight: 800; color: #0077B6; margin-bottom: 3px;">💡 BAKIT KRITIKAL ANG FOUNDATION?</div>
            <div style="font-size: 8.5px; color: #334155; line-height: 1.36; margin-bottom: 4px;">
              Kung mag-a-advertise tayo nang magulo ang Facebook page o walang maayos na website, <strong>masasayang lang ang bawat sentimong budget</strong>.
            </div>
            <div style="font-size: 8.5px; color: #334155; line-height: 1.36;">
              Kapag may customer na naging interesado sa inyong ad, agad nilang susuriin ang inyong profile at credentials. Kapag kumpleto at malinis ang foundation, mabilis na nabubuo ang tiwala at madali silang makakapag-inquire nang may kumpiyansa.
            </div>
          </div>
        </div>

        <!-- Technical Readiness Box -->
        <div class="card" style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 7px 11px;">
          <div style="font-size: 9px; font-weight: 800; color: #0A1F3F; margin-bottom: 2px;">⚡ TECHNICAL READINESS STANDARDS:</div>
          <div class="grid-3" style="gap: 7px; font-size: 7.8px; color: #475569;">
            <div>• <strong>Speed:</strong> Load time below 3.0 seconds on 4G mobile networks.</div>
            <div>• <strong>Security:</strong> Full SSL encryption (HTTPS) & valid trust badges.</div>
            <div>• <strong>Clarity:</strong> Sticky Click-to-Call & WhatsApp floating button.</div>
          </div>
        </div>
      </div>

      <!-- STEP 2 -->
      <div style="display: flex; flex-direction: column; gap: 7px;">
        <div class="step-header">
          <div class="step-badge orange">2</div>
          <div>
            <div class="step-title-text">STEP 2: Gamitin ang Facebook Boosting & Ads Para Mas Mabilis Ma-Reach ang Customers</div>
            <div class="step-title-sub">Huwag maghintay sa mabagal na organic reach. Ilapit ang inyong solusyon sa mga aktibong naghahanap at homeowners sa target area.</div>
          </div>
        </div>

        <div class="card" style="background: #F8FAFC;">
          <div style="font-size: 9.5px; font-weight: 800; color: #0A1F3F; margin-bottom: 4px;">🎨 ANG 4 NA PINAKAEPEKTIBONG AD CREATIVE FORMATS:</div>
          <div class="grid-4">
            <div style="background: #FFF; padding: 6px 7.5px; border-radius: 5px; border: 1px solid #E2E8F0;">
              <div class="tag-label orange" style="margin-bottom: 2px;">Format 1</div>
              <div style="font-size: 8.2px; font-weight: 700; color: #0A1F3F;">Actual Works</div>
              <div style="font-size: 7.4px; color: #64748B; margin-top: 1px;">High-res photos ng totoong natapos na trabaho at material specs.</div>
            </div>
            <div style="background: #FFF; padding: 6px 7.5px; border-radius: 5px; border: 1px solid #E2E8F0;">
              <div class="tag-label cyan" style="margin-bottom: 2px;">Format 2</div>
              <div style="font-size: 8.2px; font-weight: 700; color: #0A1F3F;">Before & After</div>
              <div style="font-size: 7.4px; color: #64748B; margin-top: 1px;">Visual transformation na agarang nagpapatunay ng galing at resulta.</div>
            </div>
            <div style="background: #FFF; padding: 6px 7.5px; border-radius: 5px; border: 1px solid #E2E8F0;">
              <div class="tag-label blue" style="margin-bottom: 2px;">Format 3</div>
              <div style="font-size: 8.2px; font-weight: 700; color: #0A1F3F;">Problem Solver</div>
              <div style="font-size: 7.4px; color: #64748B; margin-top: 1px;">Direktang tugon sa karaniwang sakit ng ulo at pag-aalala ng client.</div>
            </div>
            <div style="background: #FFF; padding: 6px 7.5px; border-radius: 5px; border: 1px solid #E2E8F0;">
              <div class="tag-label green" style="margin-bottom: 2px;">Format 4</div>
              <div style="font-size: 8.2px; font-weight: 700; color: #0A1F3F;">Local Spotlight</div>
              <div style="font-size: 7.4px; color: #64748B; margin-top: 1px;">Targeted sa specific subdivisions, cities, o business districts.</div>
            </div>
          </div>
        </div>

        <div class="grid-2">
          <div class="card blue-accent">
            <div style="font-size: 8.8px; font-weight: 800; color: #1D4ED8; margin-bottom: 2px;">📍 HYPER-LOCAL GEOTARGETING</div>
            <div style="font-size: 7.8px; color: #334155; line-height: 1.3;">
              Hindi natin sasayangin ang ads sa buong bansa. I-ko-concentrate natin ang budget sa inyong eksaktong radius (5km - 25km) kung saan kayo pinakamabilis makakapag-ocular o makakapag-deliver ng serbisyo.
            </div>
          </div>
          <div class="card green-accent">
            <div style="font-size: 8.8px; font-weight: 800; color: #047857; margin-bottom: 2px;">⚡ CLEAR CALL-TO-ACTION (CTA)</div>
            <div style="font-size: 7.8px; color: #334155; line-height: 1.3;">
              Bawat ad post ay may malinaw na "Next Step" para sa customer: <em>"Send Message to Request a Free Estimate"</em> o <em>"Call Us Now for Same-Day Consultation."</em> Walang kalituhan kung paano kumilos.
            </div>
          </div>
        </div>

        <!-- Ad Copy Formula Blueprint -->
        <div class="card" style="background: #FFF7ED; border: 1px solid #FFEDD5;">
          <div style="font-size: 8.8px; font-weight: 800; color: #C2410C; margin-bottom: 2px;">✍️ ANG WINNING AD COPY ANATOMY:</div>
          <div style="font-size: 7.8px; color: #7C2D12; line-height: 1.3;">
            <strong>[Local Hook & Problem]</strong> ("Naghahanap ka ba ng maaasahang contractor sa QC?") ➔ <strong>[Visual Proof & Solution]</strong> ("Tingnan ang natapos naming renovation...") ➔ <strong>[Trust Credentials]</strong> ("Licensed, 5-Star, Transparent Pricing") ➔ <strong>[Direct CTA]</strong> ("Pindutin ang Send Message para sa estimate").
          </div>
        </div>

        <div class="card navy">
          <div style="display: flex; align-items: center; justify-content: space-between;">
            <div>
              <div style="font-size: 9.8px; font-weight: 800; color: #38BDF8;">ANG TUNAY NA LAYUNIN NG FACEBOOK ADS</div>
              <div style="font-size: 7.8px; color: #CBD5E1; margin-top: 2px;">
                Hindi lang paramihin ang views. Ang layunin natin: <strong>Mas maraming tamang tao ang makakita ➔ Mas marami ang magka-interes ➔ Mas marami ang mag-check sa website/profile ➔ Mas marami ang mag-request ng estimate.</strong>
              </div>
            </div>
            <div style="background: rgba(0, 180, 216, 0.2); border: 1px solid #00B4D8; color: #38BDF8; font-weight: 800; font-size: 7.5px; padding: 4.5px 8.5px; border-radius: 4px; white-space: nowrap; margin-left: 10px;">
              HIGH INTENT REACH
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="page-footer">
      <div class="footer-left">We Forge Web • Client Growth Kit</div>
      <div class="footer-links">
        <span class="footer-contact">weforgeweb.com</span>
        <span class="dot">•</span>
        <span>+63 991 917 3652</span>
      </div>
      <div class="footer-page-num">Page 3 of 7</div>
    </div>
  </div>

  <!-- ================= PAGE 4: STEP 3 & STEP 4 ================= -->
  <div class="page">
    <div class="page-header">
      <div class="header-brand-wrap">
        <img class="header-logo" src="{logo_data_uri}" alt="Logo">
        <div>
          <div class="header-brand-title">WE FORGE <span>WEB</span></div>
          <div class="header-subtag">Phase 2: Trust & Search</div>
        </div>
      </div>
      <div class="header-section-badge">Step 3 & Step 4</div>
    </div>

    <div class="page-content">
      <!-- STEP 3 -->
      <div style="display: flex; flex-direction: column; gap: 7px;">
        <div class="step-header">
          <div class="step-badge">3</div>
          <div>
            <div class="step-title-text">STEP 3: Website / Landing Page — Ang Tutulong sa Customer na Magdesisyon</div>
            <div class="step-title-sub">Pagkatapos makita ang inyong ad o post, hindi agad tatawag ang customer. Magche-check muna sila upang maalis ang duda.</div>
          </div>
        </div>

        <div class="card orange-accent">
          <div style="font-size: 9.8px; font-weight: 800; color: #0A1F3F; margin-bottom: 3.5px;">
            🔍 ANG 6 NA TANONG NA DAPAT MASAGOT NG WEBSITE SA LOOB NG 30 SEGUNDO:
          </div>
          <div class="grid-3" style="gap: 6px;">
            <div style="background: #FFF; padding: 6px 7.5px; border-radius: 5px; border: 1px solid #E2E8F0;">
              <span style="color: #FF6B35; font-weight: 800;">1.</span> <strong>Ginagawa ba nila ito?</strong><br>
              <span style="font-size: 7.4px; color: #64748B;">Malinaw na listahan ng serbisyo at deliverables.</span>
            </div>
            <div style="background: #FFF; padding: 6px 7.5px; border-radius: 5px; border: 1px solid #E2E8F0;">
              <span style="color: #FF6B35; font-weight: 800;">2.</span> <strong>Nasa area ko ba sila?</strong><br>
              <span style="font-size: 7.4px; color: #64748B;">Malinaw na service areas, coverage, at lokasyon.</span>
            </div>
            <div style="background: #FFF; padding: 6px 7.5px; border-radius: 5px; border: 1px solid #E2E8F0;">
              <span style="color: #FF6B35; font-weight: 800;">3.</span> <strong>May experience ba sila?</strong><br>
              <span style="font-size: 7.4px; color: #64748B;">Track record, credentials, at mga lisensya.</span>
            </div>
            <div style="background: #FFF; padding: 6px 7.5px; border-radius: 5px; border: 1px solid #E2E8F0;">
              <span style="color: #0077B6; font-weight: 800;">4.</span> <strong>May proof ba ng gawa?</strong><br>
              <span style="font-size: 7.4px; color: #64748B;">High-res project photos at before-and-after.</span>
            </div>
            <div style="background: #FFF; padding: 6px 7.5px; border-radius: 5px; border: 1px solid #E2E8F0;">
              <span style="color: #0077B6; font-weight: 800;">5.</span> <strong>May tiwala ba ang iba?</strong><br>
              <span style="font-size: 7.4px; color: #64748B;">Tunay na customer reviews at ratings.</span>
            </div>
            <div style="background: #FFF; padding: 6px 7.5px; border-radius: 5px; border: 1px solid #E2E8F0;">
              <span style="color: #0077B6; font-weight: 800;">6.</span> <strong>Paano magpa-estimate?</strong><br>
              <span style="font-size: 7.4px; color: #64748B;">1-Click Direct Call, WhatsApp, o Form.</span>
            </div>
          </div>
        </div>

        <!-- Wireframe Anatomy Box -->
        <div class="card" style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 6px 11px;">
          <div style="font-size: 8.8px; font-weight: 800; color: #0A1F3F; margin-bottom: 2px;">🏗️ HIGH-CONVERTING LANDING PAGE WIREFRAME:</div>
          <div class="grid-4" style="gap: 5px; font-size: 7.5px; color: #475569; text-align: center;">
            <div style="background: #FFF; padding: 4.5px; border-radius: 4px; border: 1px solid #E2E8F0;">
              <strong>Header / Hero</strong><br>Value Prop + CTA
            </div>
            <div style="background: #FFF; padding: 4.5px; border-radius: 4px; border: 1px solid #E2E8F0;">
              <strong>Proof Portfolio</strong><br>Before/After Gallery
            </div>
            <div style="background: #FFF; padding: 4.5px; border-radius: 4px; border: 1px solid #E2E8F0;">
              <strong>Client Reviews</strong><br>Google Verified Badges
            </div>
            <div style="background: #FFF; padding: 4.5px; border-radius: 4px; border: 1px solid #E2E8F0;">
              <strong>Booking Form</strong><br>1-Click WhatsApp / Call
            </div>
          </div>
        </div>

        <div class="quote-box">
          "Hindi natin hawak ang final decision ng customer, ngunit ginagawa natin ang ating bahagi upang gawing napakadali para sa kanila na maintindihan, magtiwala, at kumontak nang walang takot."
        </div>
      </div>

      <!-- STEP 4 -->
      <div style="display: flex; flex-direction: column; gap: 7px;">
        <div class="step-header">
          <div class="step-badge cyan">4</div>
          <div>
            <div class="step-title-text">STEP 4: Google Business Profile Para sa Location, Search, at Local Trust</div>
            <div class="step-title-sub">Hindi lahat ng customer ay galing sa Facebook. May mga kliyenteng may agarang pangangailangan at diretso sa Google Search.</div>
          </div>
        </div>

        <div class="grid-2">
          <div class="card cyan-accent">
            <div style="font-size: 9.2px; font-weight: 800; color: #0077B6; margin-bottom: 2px;">📍 HIGH-INTENT "READY-TO-BUY" SEARCHES</div>
            <div style="font-size: 7.6px; color: #334155; margin-bottom: 3.5px;">
              Kapag nag-type ang customer sa Google ng:
            </div>
            <div style="font-family: monospace; font-size: 7.6px; background: #FFF; padding: 4.5px 6px; border-radius: 5px; border: 1px solid #E2E8F0; margin-bottom: 3.5px; color: #0A1F3F;">
              • "[Service Name] near me"<br>
              • "Best [Contractor / Clinic / Specialist] in [City]"<br>
              • "[Service Type] contact number & price estimate"
            </div>
            <div style="font-size: 7.6px; color: #334155; line-height: 1.3;">
              Ang inyong Google Business card ang magpapakita ng inyong exact map location, phone number, direct reviews, at website link.
            </div>
          </div>

          <div class="card green-accent">
            <div style="font-size: 9.2px; font-weight: 800; color: #047857; margin-bottom: 2px;">⭐ ANG REVIEW FLYWHEEL SA GOOGLE</div>
            <div style="font-size: 7.6px; color: #334155; margin-bottom: 3.5px;">
              Bago tumawag ang customer, tinitingnan nila ang inyong Google Rating:
            </div>
            <ul class="clean-list">
              <li><span class="check-icon">★</span> <strong>5-Star Proof:</strong> Ilang totoong tao na ang nagtiwala at natuwa sa serbisyo?</li>
              <li><span class="check-icon">★</span> <strong>Recent Velocity:</strong> Patuloy bang aktibo at consistent ang kalidad ng inyong gawa?</li>
              <li><span class="check-icon">★</span> <strong>Local SEO Edge:</strong> Ang complete at active na profile na may regular reviews ay nakakakuha ng mas maraming direktang tawag sa Google Maps.</li>
            </ul>
          </div>
        </div>

        <!-- Google GBP Quick Wins -->
        <div class="card" style="background: #F8FAFC; border: 1px solid #E2E8F0;">
          <div style="font-size: 8.8px; font-weight: 800; color: #0A1F3F; margin-bottom: 2px;">🎯 GBP QUICK WINS & LOCAL 3-PACK STRATEGY:</div>
          <div style="font-size: 7.8px; color: #475569; line-height: 1.34;">
            Mag-upload ng 3-5 bagong geotagged photos linggu-linggo, sagutin ang bawat review sa loob ng 24 oras, i-update ang business hours, at i-embed ang Google Map sa inyong website para sa mataas na ranking.
          </div>
        </div>
      </div>
    </div>

    <div class="page-footer">
      <div class="footer-left">We Forge Web • Client Growth Kit</div>
      <div class="footer-links">
        <span class="footer-contact">weforgeweb.com</span>
        <span class="dot">•</span>
        <span>+63 991 917 3652</span>
      </div>
      <div class="footer-page-num">Page 4 of 7</div>
    </div>
  </div>

  <!-- ================= PAGE 5: STEP 5 & STEP 6 ================= -->
  <div class="page">
    <div class="page-header">
      <div class="header-brand-wrap">
        <img class="header-logo" src="{logo_data_uri}" alt="Logo">
        <div>
          <div class="header-brand-title">WE FORGE <span>WEB</span></div>
          <div class="header-subtag">Phase 3: Assets & Boosting</div>
        </div>
      </div>
      <div class="header-section-badge">Step 5 & Step 6</div>
    </div>

    <div class="page-content">
      <!-- STEP 5 -->
      <div style="display: flex; flex-direction: column; gap: 7px;">
        <div class="step-header">
          <div class="step-badge">5</div>
          <div>
            <div class="step-title-text">STEP 5: Bawat Project Gawin Nating Bagong Marketing Asset</div>
            <div class="step-title-sub">Huwag hayaang matapos ang isang proyekto nang walang nakukuhang patunay. Bawat project ay gasolina para sa susunod na kliyente.</div>
          </div>
        </div>

        <div class="card navy">
          <div style="font-size: 9.8px; font-weight: 800; color: #38BDF8; margin-bottom: 4px;">📸 ANG 5-ASSET CAPTURE PROTOCOL SA BAWAT NATAPOS NA PROYEKTO:</div>
          <div class="grid-3" style="gap: 6px;">
            <div style="background: rgba(255,255,255,0.06); padding: 6px 8.5px; border-radius: 5px; border: 1px solid rgba(255,255,255,0.1);">
              <div style="color: #FF8A50; font-weight: 800; font-size: 8.2px;">1. Before & During Photos</div>
              <div style="font-size: 7.4px; color: #CBD5E1; margin-top: 2px;">Kuhanan ang kalagayan bago simulan at habang ginagawa ng inyong team ang trabaho.</div>
            </div>
            <div style="background: rgba(255,255,255,0.06); padding: 6px 8.5px; border-radius: 5px; border: 1px solid rgba(255,255,255,0.1);">
              <div style="color: #38BDF8; font-weight: 800; font-size: 8.2px;">2. High-Res After Photos</div>
              <div style="font-size: 7.4px; color: #CBD5E1; margin-top: 2px;">Malinis at maayos na kuha ng natapos na resulta mula sa iba't ibang magagandang anggulo.</div>
            </div>
            <div style="background: rgba(255,255,255,0.06); padding: 6px 8.5px; border-radius: 5px; border: 1px solid rgba(255,255,255,0.1);">
              <div style="color: #34D399; font-weight: 800; font-size: 8.2px;">3. Customer Review & Video</div>
              <div style="font-size: 7.4px; color: #CBD5E1; margin-top: 2px;">Kunin ang maikling komento o genuine Google Review mula sa natuwang customer.</div>
            </div>
          </div>
        </div>

        <div style="font-size: 9.5px; font-weight: 800; color: #0A1F3F; margin-bottom: 2px;">Saan Natin I-re-distribute ang Bawat Bagong Asset?</div>
        <div class="grid-4">
          <div class="card" style="padding: 6px 7.5px; text-align: center;">
            <div class="tag-label blue" style="margin-bottom: 2px;">Facebook Organic</div>
            <div style="font-size: 7.4px; color: #475569;">Post na may location tag at breakdown ng ginawa.</div>
          </div>
          <div class="card" style="padding: 6px 7.5px; text-align: center;">
            <div class="tag-label orange" style="margin-bottom: 2px;">Facebook Ads</div>
            <div style="font-size: 7.4px; color: #475569;">Naka-target sa mga homeowners sa katabing subdivisions.</div>
          </div>
          <div class="card" style="padding: 6px 7.5px; text-align: center;">
            <div class="tag-label green" style="margin-bottom: 2px;">Google Profile</div>
            <div style="font-size: 7.4px; color: #475569;">Photo upload sa GBP para sa local search visibility.</div>
          </div>
          <div class="card" style="padding: 6px 7.5px; text-align: center;">
            <div class="tag-label cyan" style="margin-bottom: 2px;">Website Portfolio</div>
            <div style="font-size: 7.4px; color: #475569;">Idinadagdag sa permanent case studies sa website.</div>
          </div>
        </div>
      </div>

      <!-- STEP 6 -->
      <div style="display: flex; flex-direction: column; gap: 7px;">
        <div class="step-header">
          <div class="step-badge orange">6</div>
          <div>
            <div class="step-title-text">STEP 6: I-Boost Lamang ang mga Content na May Matibay na Patunay</div>
            <div class="step-title-sub">Gamitin ang mga format mula sa Step 2: maglaan lamang ng budget sa mga content na may matibay na patunay at dahilan para mag-inquire ang tao.</div>
          </div>
        </div>

        <div class="grid-2">
          <div class="card orange-accent">
            <div style="font-size: 9.2px; font-weight: 800; color: #0A1F3F; margin-bottom: 3px;">💎 ANG WINNING CRITERIA PARA SA PAID BOOSTING:</div>
            <ul class="clean-list">
              <li><span class="check-icon orange">✓</span> <strong>Malinaw na Before-and-After:</strong> Agad makikita ang halaga sa unang tingin pa lang (3-second scroll stop).</li>
              <li><span class="check-icon orange">✓</span> <strong>Specific Project Breakdown:</strong> May paliwanag kung paano nalutas ang problema ng customer.</li>
              <li><span class="check-icon orange">✓</span> <strong>Location Relatability:</strong> May pagbanggit sa bayan o siyudad para maging pamilyar sa target audience.</li>
              <li><span class="check-icon orange">✓</span> <strong>Direct Action CTA:</strong> Malinaw na call-to-action button: "Send Message for Free Estimate" o "Book a Consultation".</li>
            </ul>
          </div>

          <div class="card" style="background: #FFF7ED; border: 1px solid #FFEDD5;">
            <div style="font-size: 9.2px; font-weight: 800; color: #C2410C; margin-bottom: 3px;">🚫 HUWAG MAG-BOOST NG WALANG DAHILAN</div>
            <div style="font-size: 7.8px; color: #475569; line-height: 1.34; margin-bottom: 4px;">
              Ang paggastos sa mga generic na quotes, stock photos, o simpleng poster na walang patunay ay <strong>nagtatapon lamang ng pondo</strong>.
            </div>
            <div style="font-size: 7.8px; color: #475569; line-height: 1.34;">
              Bawat pisong ilalagay natin sa advertising ay dapat may dalawang layunin lamang: <strong>Ipakita ang inyong tunay na kakayahan at bigyan ng kumpiyansa ang customer na mag-inquire.</strong>
            </div>
          </div>
        </div>

        <!-- Budget Allocation Rule -->
        <div class="card cyan-accent">
          <div style="font-size: 8.8px; font-weight: 800; color: #0077B6; margin-bottom: 2px;">💰 ANG 70/20/10 AD BUDGET ALLOCATION RULE:</div>
          <div style="font-size: 7.8px; color: #334155; line-height: 1.34;">
            <strong>70%</strong> sa Proof-First Top Performing Ads (Lead Gen) • <strong>20%</strong> sa Retargeting & Case Studies (Nurturing) • <strong>10%</strong> sa Bagong Creative Testing.
          </div>
        </div>

        <!-- Retargeting Audience Matrix -->
        <div class="card" style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 6px 11px;">
          <div style="font-size: 8.5px; font-weight: 800; color: #0A1F3F; margin-bottom: 2px;">🎯 RETARGETING AUDIENCE BLUEPRINT:</div>
          <div style="font-size: 7.6px; color: #475569; line-height: 1.3;">
            I-target muli ang mga taong nag-click sa inyong website o nag-message sa Facebook sa nakalipas na 30–60 araw gamit ang bagong customer video testimonials at newly completed project case studies.
          </div>
        </div>
      </div>
    </div>

    <div class="page-footer">
      <div class="footer-left">We Forge Web • Client Growth Kit</div>
      <div class="footer-links">
        <span class="footer-contact">weforgeweb.com</span>
        <span class="dot">•</span>
        <span>+63 991 917 3652</span>
      </div>
      <div class="footer-page-num">Page 5 of 7</div>
    </div>
  </div>

  <!-- ================= PAGE 6: STEP 7 & STEP 8 ================= -->
  <div class="page">
    <div class="page-header">
      <div class="header-brand-wrap">
        <img class="header-logo" src="{logo_data_uri}" alt="Logo">
        <div>
          <div class="header-brand-title">WE FORGE <span>WEB</span></div>
          <div class="header-subtag">Phase 4: Nurturing & ROI</div>
        </div>
      </div>
      <div class="header-section-badge">Step 7 & Step 8</div>
    </div>

    <div class="page-content">
      <!-- STEP 7 -->
      <div style="display: flex; flex-direction: column; gap: 7px;">
        <div class="step-header">
          <div class="step-badge">7</div>
          <div>
            <div class="step-title-text">STEP 7: I-Follow Up ang mga Interested Pero Hindi Pa Ready (Value Nurturing)</div>
            <div class="step-title-sub">Hindi lahat magbo-book agad. May nagko-compare, nag-iipon ng budget, o naghihintay ng schedule. Huwag mangulit — magbigay ng halaga.</div>
          </div>
        </div>

        <div class="grid-2">
          <div class="card" style="border-left: 4px solid #EF4444; background: #FEF2F2;">
            <div style="font-size: 9.2px; font-weight: 800; color: #991B1B; margin-bottom: 2px;">❌ ANG MALING PARAAN (PURO KULIT):</div>
            <div style="background: #FFF; border: 1px solid #FECACA; border-radius: 5px; padding: 4.5px 6px; color: #7F1D1D; margin-bottom: 3px; font-size: 7.6px;">
              "Hi Ma'am/Sir, follow up lang po sa estimate ninyo kahapon. Kukunin nyo po ba?"
            </div>
            <div style="font-size: 7.4px; color: #7F1D1D; line-height: 1.3;">
              Nagdudulot ito ng pressure sa customer at kadalasang nagiging dahilan para i-seen o i-block ang inyong mensahe.
            </div>
          </div>

          <div class="card green-accent">
            <div style="font-size: 9.2px; font-weight: 800; color: #047857; margin-bottom: 2px;">✅ ANG TAMA AT VALUE-FIRST NA MENSAHE:</div>
            <div style="background: #FFF; border: 1px solid #BBF7D0; border-radius: 5px; padding: 4.5px 6px; color: #064E3B; margin-bottom: 3px; font-size: 7.6px;">
              "Hi [Name], may natapos po kaming katulad na project sa area ninyo kahapon. Naalala ko po yung concern ninyo sa [Problem], baka makatulong po itong video/photos kung paano namin ito naresolba."
            </div>
            <div style="font-size: 7.4px; color: #064E3B; line-height: 1.3;">
              Nakatutulong ito sa customer na makapag-desisyon nang may sapat na impormasyon kapag handa na sila.
            </div>
          </div>
        </div>

        <!-- 3 Follow Up Scripts Grid -->
        <div class="grid-3">
          <div class="card" style="padding: 6px 7.5px;">
            <div class="tag-label blue" style="margin-bottom: 2px;">Template A: Case Study</div>
            <div style="font-size: 7.4px; color: #475569; line-height: 1.3;">
              Ibahagi ang recent similar project na nagpapakita ng eksaktong solusyon sa kanilang issue.
            </div>
          </div>
          <div class="card" style="padding: 6px 7.5px;">
            <div class="tag-label green" style="margin-bottom: 2px;">Template B: Client Review</div>
            <div style="font-size: 7.4px; color: #475569; line-height: 1.3;">
              I-send ang screenshot ng feedback ng kliyenteng may parehong pag-aalinlangan noon.
            </div>
          </div>
          <div class="card" style="padding: 6px 7.5px;">
            <div class="tag-label orange" style="margin-bottom: 2px;">Template C: Schedule Update</div>
            <div style="font-size: 7.4px; color: #475569; line-height: 1.3;">
              Magbigay ng magalang na update ukol sa natitirang available installation / service slots.
            </div>
          </div>
        </div>
      </div>

      <!-- STEP 8 -->
      <div style="display: flex; flex-direction: column; gap: 7px;">
        <div class="step-header">
          <div class="step-badge orange">8</div>
          <div>
            <div class="step-title-text">STEP 8: I-Track Kung Saan Talaga Nanggagaling ang Magagandang Leads</div>
            <div class="step-title-sub">Hindi lahat ng inquiry ay pareho ang kalidad. Subaybayan ang buong funnel mula sa unang mensahe hanggang sa saradong kontrata.</div>
          </div>
        </div>

        <!-- 5 Stage Funnel Tracker -->
        <div class="funnel-container">
          <div class="funnel-row s1">
            <div>
              <span class="tag-label cyan">Stage 1</span> <strong>Total Inquiries Received</strong>
              <span style="font-size: 7.4px; color: #64748B; margin-left: 6px;">(Facebook Ads, Google Search, Website Form, Direct Calls)</span>
            </div>
            <div style="font-size: 7.8px; font-weight: 800; color: #0077B6;">Lahat ng Nag-Inquire</div>
          </div>

          <div class="funnel-row s2">
            <div>
              <span class="tag-label blue">Stage 2</span> <strong>Qualified Leads</strong>
              <span style="font-size: 7.4px; color: #64748B; margin-left: 6px;">(Nasa target service area, may budget, at may konkretong pangangailangan)</span>
            </div>
            <div style="font-size: 7.8px; font-weight: 800; color: #0284C7;">Na-filter na Kliyente</div>
          </div>

          <div class="funnel-row s3">
            <div>
              <span class="tag-label blue">Stage 3</span> <strong>Estimates / Proposals Sent</strong>
              <span style="font-size: 7.4px; color: #64748B; margin-left: 6px;">(Formal quote, site ocular inspection, o detailed pitch)</span>
            </div>
            <div style="font-size: 7.8px; font-weight: 800; color: #1D4ED8;">Aktibong Opportunity</div>
          </div>

          <div class="funnel-row s4">
            <div>
              <span class="tag-label orange">Stage 4</span> <strong>Booked & Closed Projects</strong>
              <span style="font-size: 7.4px; color: #64748B; margin-left: 6px;">(Pirma ng kontrata, downpayment received, schedule confirmed)</span>
            </div>
            <div style="font-size: 7.8px; font-weight: 800; color: #D97706;">Saradong Kliyente</div>
          </div>

          <div class="funnel-row s5">
            <div>
              <span class="tag-label green">Stage 5</span> <strong>Actual Revenue & Net Marketing ROI</strong>
            </div>
            <div style="font-size: 8.5px; font-weight: 800; color: #059669;">PROFITABLE GROWTH 🚀</div>
          </div>
        </div>

        <div class="card cyan-accent">
          <div style="font-size: 8.8px; font-weight: 800; color: #0077B6; margin-bottom: 2px;">
            📊 ANG DATA-DRIVEN STRATEGY DECISION:
          </div>
          <div style="font-size: 7.8px; color: #334155; line-height: 1.34;">
            Halimbawa, kung mapansin natin pagkatapos ng ilang linggo na ang Google Search ay nagbibigay ng mataas na closing rate sa high-ticket services, o ang Facebook Before-and-After Video Ads ang nagdadala ng pinakamababang cost-per-lead — <strong>doon natin ibubuhos ang mas malaking pondo upang ma-maximize ang inyong kita.</strong>
          </div>
        </div>
      </div>
    </div>

    <div class="page-footer">
      <div class="footer-left">We Forge Web • Client Growth Kit</div>
      <div class="footer-links">
        <span class="footer-contact">weforgeweb.com</span>
        <span class="dot">•</span>
        <span>+63 991 917 3652</span>
      </div>
      <div class="footer-page-num">Page 6 of 7</div>
    </div>
  </div>

  <!-- ================= PAGE 7: JOURNEY, ROADMAP & KICKOFF ================= -->
  <div class="page">
    <div class="page-header">
      <div class="header-brand-wrap">
        <img class="header-logo" src="{logo_data_uri}" alt="Logo">
        <div>
          <div class="header-brand-title">WE FORGE <span>WEB</span></div>
          <div class="header-subtag">Execution & Rollout</div>
        </div>
      </div>
      <div class="header-section-badge">Journey & 30-60-90 Roadmap</div>
    </div>

    <div class="page-content">
      <div>
        <div class="section-tag">Complete System Integration</div>
        <div class="page-title">Ang Buong Journey at 30-60-90 Day Action Plan</div>
        <div class="page-subtitle">Pagsamahin natin ang buong lead cycle, application sa inyong industriya, at kongkretong rollout steps.</div>
      </div>

      <!-- Full Customer Journey Flowchart -->
      <div class="card navy" style="padding: 9px 11px;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <div style="text-align: center; width: 18%;">
            <div style="background: #FF6B35; color: #FFF; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 10px; margin: 0 auto 2px auto;">1</div>
            <div style="font-size: 8.5px; font-weight: 700; color: #FFF;">Facebook / Ads</div>
            <div style="font-size: 7.2px; color: #94A3B8;">Mabilis na Reach</div>
          </div>
          <div style="color: #00B4D8; font-weight: 800; font-size: 11px;">➔</div>

          <div style="text-align: center; width: 18%;">
            <div style="background: #00B4D8; color: #FFF; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 10px; margin: 0 auto 2px auto;">2</div>
            <div style="font-size: 8.5px; font-weight: 700; color: #FFF;">Website & GBP</div>
            <div style="font-size: 7.2px; color: #94A3B8;">Proof & Deciding</div>
          </div>
          <div style="color: #00B4D8; font-weight: 800; font-size: 11px;">➔</div>

          <div style="text-align: center; width: 18%;">
            <div style="background: #3B82F6; color: #FFF; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 10px; margin: 0 auto 2px auto;">3</div>
            <div style="font-size: 8.5px; font-weight: 700; color: #FFF;">Direct Call / DM</div>
            <div style="font-size: 7.2px; color: #94A3B8;">Informed Inquiry</div>
          </div>
          <div style="color: #00B4D8; font-weight: 800; font-size: 11px;">➔</div>

          <div style="text-align: center; width: 18%;">
            <div style="background: #F59E0B; color: #FFF; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 10px; margin: 0 auto 2px auto;">4</div>
            <div style="font-size: 8.5px; font-weight: 700; color: #FFF;">Estimate / Quote</div>
            <div style="font-size: 7.2px; color: #94A3B8;">Closed Deal</div>
          </div>
          <div style="color: #00B4D8; font-weight: 800; font-size: 11px;">➔</div>

          <div style="text-align: center; width: 18%;">
            <div style="background: #10B981; color: #FFF; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 10px; margin: 0 auto 2px auto;">5</div>
            <div style="font-size: 8.5px; font-weight: 700; color: #FFF;">New Proof Asset</div>
            <div style="font-size: 7.2px; color: #94A3B8;">Review Flywheel</div>
          </div>
        </div>
      </div>

      <!-- 30-60-90 Roadmap Grid -->
      <div class="grid-3">
        <div class="card" style="border-top: 4px solid #00B4D8;">
          <div style="font-size: 9.5px; font-weight: 800; color: #0077B6; margin-bottom: 2px;">PHASE 1: DAYS 1 - 15</div>
          <div style="font-size: 10px; font-weight: 800; color: #0A1F3F; margin-bottom: 3px;">Foundation & Setup</div>
          <ul class="clean-list" style="font-size: 7.6px;">
            <li><span class="check-icon blue">✓</span> Ayusin ang Conversion Website & Landing Page.</li>
            <li><span class="check-icon blue">✓</span> I-optimize at i-verify ang Google Business Profile.</li>
            <li><span class="check-icon blue">✓</span> I-update ang Facebook branding & call buttons.</li>
            <li><span class="check-icon blue">✓</span> I-organisa ang initial batch ng past project proof.</li>
          </ul>
        </div>

        <div class="card" style="border-top: 4px solid #FF6B35;">
          <div style="font-size: 9.5px; font-weight: 800; color: #EA580C; margin-bottom: 2px;">PHASE 2: DAYS 16 - 30</div>
          <div style="font-size: 10px; font-weight: 800; color: #0A1F3F; margin-bottom: 3px;">Reach & Ad Launch</div>
          <ul class="clean-list" style="font-size: 7.6px;">
            <li><span class="check-icon orange">✓</span> I-launch ang Proof-Based Facebook Ad campaigns.</li>
            <li><span class="check-icon orange">✓</span> Hyper-local geotargeting sa exact service areas.</li>
            <li><span class="check-icon orange">✓</span> Seamless routing sa WhatsApp, Viber, at Phone.</li>
            <li><span class="check-icon orange">✓</span> Daily tracking ng leads at cost-per-estimate.</li>
          </ul>
        </div>

        <div class="card" style="border-top: 4px solid #10B981;">
          <div style="font-size: 9.5px; font-weight: 800; color: #059669; margin-bottom: 2px;">PHASE 3: DAYS 31 - 90+</div>
          <div style="font-size: 10px; font-weight: 800; color: #0A1F3F; margin-bottom: 3px;">Flywheel & Scale</div>
          <ul class="clean-list" style="font-size: 7.6px;">
            <li><span class="check-icon">✓</span> 5-Asset capture sa bawat bagong project.</li>
            <li><span class="check-icon">✓</span> Value-driven follow-ups sa previous inquiries.</li>
            <li><span class="check-icon">✓</span> I-scale ang budget sa highest-ROI ad campaigns.</li>
            <li><span class="check-icon">✓</span> Tuluy-tuloy na Google reviews collection.</li>
          </ul>
        </div>
      </div>

      <!-- Universal Cross-Industry Coverage -->
      <div class="card" style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 7px 11px;">
        <div style="font-size: 9.2px; font-weight: 800; color: #0A1F3F; margin-bottom: 2px;">🌐 INDUSTRY COMPATIBILITY MATRIX:</div>
        <div class="grid-3" style="gap: 6px; font-size: 7.8px; color: #334155;">
          <div>• <strong>Contractors / Trades:</strong> Before/after transformations, ocular quote booking.</div>
          <div>• <strong>Clinics / Health:</strong> Doctor credentials, direct consultation slot reservation.</div>
          <div>• <strong>Professional B2B / Law:</strong> Case studies, 1-on-1 discovery call bookings.</div>
        </div>
      </div>

      <!-- Official Partnership & Kickoff Banner -->
      <div class="card navy" style="padding: 11px 15px; position: relative;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <div style="max-width: 125mm;">
            <div style="font-size: 8.2px; font-weight: 800; color: #FF8A50; letter-spacing: 0.8px; text-transform: uppercase;">Handa Ka Na Bang Simulan ang Sistema Mo?</div>
            <div style="font-family: 'Outfit', sans-serif; font-size: 14px; font-weight: 800; color: #FFFFFF; margin: 2px 0;">
              WE FORGE WEB • YOUR CLIENT GROWTH PARTNER
            </div>
            <div style="font-size: 8.2px; color: #CBD5E1; line-height: 1.36;">
              Huwag nang ubusin ang oras at pondo sa trial-and-error. Buuin natin ang inyong automated website, Google Business setup, at proof-first advertising system para sa tuluy-tuloy na agos ng mga kwalipikadong kliyente.
            </div>
          </div>
          <div style="text-align: right; border-left: 1px solid rgba(255,255,255,0.15); padding-left: 15px; flex-shrink: 0;">
            <div style="font-size: 7.5px; color: #94A3B8; text-transform: uppercase; font-weight: 700;">Direct Consultation</div>
            <div style="font-size: 12px; font-weight: 800; color: #38BDF8; margin: 1px 0;">+63 991 917 3652</div>
            <div style="font-size: 8.2px; color: #FFFFFF;">hello@weforgeweb.com</div>
            <div style="font-size: 8.2px; color: #38BDF8; font-weight: 700; margin-top: 2px;">weforgeweb.com</div>
          </div>
        </div>
      </div>

      <!-- Motto -->
      <div style="text-align: center; margin-top: 2px; font-size: 7.8px; color: #64748B;">
        <em>"Build the foundation. Palakasin ang reach. Ipakita ang proof. Generate inquiries. Track what works. Then scale."</em>
      </div>
    </div>

    <div class="page-footer">
      <div class="footer-left">We Forge Web • Client Growth Kit</div>
      <div class="footer-links">
        <span class="footer-contact">weforgeweb.com</span>
        <span class="dot">•</span>
        <span>+63 991 917 3652</span>
      </div>
      <div class="footer-page-num">Page 7 of 7</div>
    </div>
  </div>

</body>
</html>
"""

TEXT_POLISH_REPLACEMENTS = {
    "⚡ ": "",
    "🎯 ": "",
    "🌐 ": "",
    "⚙️ ": "",
    "🔄 ": "",
    "🛠️ ": "",
    "🎨 ": "",
    "📞 ": "",
    "✉️ ": "",
    "🔍 ": "",
    "📌 ": "",
    "🏆 ": "",
    "📈 ": "",
    "📊 ": "",
    "💡 ": "",
    "✅ ": "",
    "❌ ": "",
    "🚀": "",
    "✓": "",
    "➔": "->",
    "→": "->",
    "–": "-",
    "—": "-",
    "‑": "-",
    "“": '"',
    "”": '"',
    "’": "'",
    "•": "-",
}


def polish_html(html):
    """Keep the strategy content, but remove symbol noise for a premium PDF."""
    for old, new in TEXT_POLISH_REPLACEMENTS.items():
        html = html.replace(old, new)
    html = "".join(ch for ch in html if ch in "\n\r\t" or 32 <= ord(ch) <= 126)
    return html


def generate_pdf():
    html_path = os.path.join(SCRIPT_DIR, "growth_kit.html")
    pdf_path = os.path.join(SCRIPT_DIR, "WeForgeWeb_Client_Growth_Kit_System.pdf")
    
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(polish_html(HTML_CONTENT))
    print(f"Wrote HTML to {html_path}")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file:///{html_path.replace(os.sep, '/')}", wait_until="load")
        page.wait_for_timeout(1000)
        
        page.pdf(
            path=pdf_path,
            format="A4",
            print_background=True,
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
            prefer_css_page_size=True
        )
        browser.close()
        print(f"Generated PDF at {pdf_path}")

    # Verify pages and generate previews
    doc = fitz.open(pdf_path)
    print(f"Total PDF pages: {len(doc)}")
    
    preview_dir = os.path.join(SCRIPT_DIR, "pdf_previews")
    os.makedirs(preview_dir, exist_ok=True)
    
    # Remove old preview files
    for old_f in os.listdir(preview_dir):
        if old_f.endswith(".png"):
            os.remove(os.path.join(preview_dir, old_f))
            
    for i, page_obj in enumerate(doc):
        pix = page_obj.get_pixmap(dpi=150)
        img_path = os.path.join(preview_dir, f"page_{i+1}.png")
        pix.save(img_path)
        print(f"Saved preview: {img_path}")

if __name__ == "__main__":
    generate_pdf()
