import os, re, json
from pathlib import Path
import fitz

pdf_path = r'C:\Users\Administrator\Documents\Client Growth Kit\Client Growth Kit\WeForgeWeb_Client_Growth_Kit_System.pdf'
out_dir = Path(r'C:\Users\Administrator\Documents\Client Growth Kit\Client Growth Kit\01-analysis')
preview_dir = Path(r'C:\Users\Administrator\Documents\Client Growth Kit\Client Growth Kit\pdf_previews\step37_visual_audit')
out_dir.mkdir(parents=True, exist_ok=True)
preview_dir.mkdir(parents=True, exist_ok=True)

doc = fitz.open(pdf_path)
total = doc.page_count

# Render each page to PNG
for i in range(total):
    page = doc.load_page(i)
    pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0))
    img_path = preview_dir / f'page_{i+1:03d}.png'
    pix.save(str(img_path))

# Build structured summaries from PDF blocks + drawings
summaries = []
for i in range(total):
    page = doc.load_page(i)
    text = page.get_text('text')
    blocks = page.get_text('blocks')
    images = page.get_images(full=True)
    fonts = {}
    font_sizes = []
    for b in blocks:
        # PyMuPDF block tuple: (x0,y0,x1,y1,text,block_no,block_type)
        # font details via get_text("dict")
        pass
    # Font analysis via dict
    try:
        page_dict = page.get_text('dict')
        for block in page_dict.get('blocks', []):
            if block.get('type') == 0:
                for line in block.get('lines', []):
                    for span in line.get('spans', []):
                        font = span.get('font', 'unknown')
                        size = span.get('size', 0)
                        fonts.setdefault(font, set()).add(round(size, 2))
                        font_sizes.append(size)
    except Exception as e:
        fonts = {'_error': str(e)}
    # Summary metrics
    font_info = {}
    for f, sizes in fonts.items():
        try:
            font_info[f] = sorted(sizes)[:6]
        except Exception:
            font_info[f] = []
    try:
        avg_font_size = round(sum(font_sizes)/len(font_sizes),2) if font_sizes else 0
        min_font_size = round(min(font_sizes),2) if font_sizes else 0
        max_font_size = round(max(font_sizes),2) if font_sizes else 0
    except Exception:
        avg_font_size = min_font_size = max_font_size = 0
    summaries.append({
        'page': i+1,
        'text_length': len(text),
        'image_count': len(images),
        'block_count': len(blocks),
        'avg_font_size': avg_font_size,
        'min_font_size': min_font_size,
        'max_font_size': max_font_size,
        'fonts_sample': dict(list(font_info.items())[:10]),
        'text_preview': text[:700].replace('\n', ' | ')
    })

with open(preview_dir / 'page_summaries.json', 'w', encoding='utf-8') as f:
    json.dump({'page_count': total, 'pages': summaries}, f, indent=2, ensure_ascii=False)

# Export a one-page plain-text block dump for quick scan
lines = []
lines.append(f'WeForgeWeb_Client_Growth_Kit_System.pdf — pages: {total}')
lines.append('')
for s in summaries:
    lines.append('---')
    lines.append(f"Page {s['page']}")
    lines.append(f"  text_length={s['text_length']} images={s['image_count']} blocks={s['block_count']}")
    lines.append(f"  font sizes avg={s['avg_font_size']} min={s['min_font_size']} max={s['max_font_size']}")
    lines.append(f"  fonts_sample={s['fonts_sample']}")
    lines.append(f"  preview: {s['text_preview']}")
    lines.append('')

(preview_dir / 'page_summaries.txt').write_text('\n'.join(lines), encoding='utf-8')

print('Done. Total pages:', total)
print('Rendered images:', total)
print('Summary files:', preview_dir / 'page_summaries.json')
print('Summary txt:', preview_dir / 'page_summaries.txt')
