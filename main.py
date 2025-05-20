from utils.pdf_utils import extract_chapters
from utils.chunker import chunk_text
from utils.translator import translate_to_hindi
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
import re

def save_translation_as_pdf(chapter_title, translations):
    # Register Devanagari font
    font_path = "fonts/NotoSansDevanagari-Regular.ttf"
    pdfmetrics.registerFont(TTFont("NotoHindi", font_path))

    filename = f"translated_{chapter_title}.pdf"
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=40, leftMargin=40,
        topMargin=60, bottomMargin=60
    )

    styles = getSampleStyleSheet()

    # Custom Styles
    title_style = ParagraphStyle(
        name="Title",
        fontName="NotoHindi",
        fontSize=18,
        alignment=TA_CENTER,
        spaceAfter=24,
        leading=22
    )

    quote_style = ParagraphStyle(
        name="Quote",
        fontName="NotoHindi",
        fontSize=14,
        italic=True,
        alignment=TA_CENTER,
        spaceBefore=12,
        spaceAfter=6,
        leading=20
    )

    author_style = ParagraphStyle(
        name="Author",
        fontName="NotoHindi",
        fontSize=12,
        alignment=TA_CENTER,
        spaceAfter=20
    )

    body_style = ParagraphStyle(
        name="Body",
        fontName="NotoHindi",
        fontSize=12,
        leading=18,
        alignment=TA_JUSTIFY,
        spaceAfter=12
    )

    story = []

    # Add Chapter Title
    story.append(Paragraph(f"<b>{chapter_title}</b>", title_style))
    story.append(Spacer(1, 12))

    # Parse and style chunks
    for chunk in translations:
        for line in chunk.splitlines():
            line = line.strip()
            if not line:
                continue

            line = re.sub(r"[*_`•]+", "", line)  # Remove markdown artifacts

            if "चोग्याम" in line:
                story.append(Paragraph(f"<b>{line}</b>", author_style))
            elif re.search(r"मनन|अनुभव|ध्यान|यात्रा", line) and len(line) < 200:
                story.append(Paragraph(line, quote_style))
            else:
                story.append(Paragraph(line, body_style))

    doc.build(story)
    print(f"✅ Saved beautifully styled PDF: {filename}")



def run_test(pdf_path):
    chapters = extract_chapters(pdf_path)

    print("Chapters found:")
    for ch in list(chapters.keys())[:5]:
        print(f"- {ch}")

    # Translate the very first chapter (e.g., "Introduction")
    first_chapter_title = list(chapters.keys())[0]
    text = chapters[first_chapter_title]

    print(f"\n🔹 Translating full chapter: {first_chapter_title}")
    chunks = chunk_text(text)  # No limit

    translations = []
    for idx, chunk in enumerate(chunks):
        print(f"\nTranslating chunk {idx + 1}/{len(chunks)}...")
        translation = translate_to_hindi(chunk)
        translations.append(translation)

    save_translation_as_pdf(first_chapter_title, translations)



if __name__ == "__main__":
    run_test("how_to_meditate.pdf")  # Make sure the file is in your project root
