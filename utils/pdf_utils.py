import fitz  # PyMuPDF

def extract_chapters(pdf_path):
    doc = fitz.open(pdf_path)
    chapters = {}
    current_chapter = "Introduction"
    chapter_text = []

    for page in doc:
        text = page.get_text()
        lines = text.splitlines()
        for line in lines:
            if line.strip().lower().startswith("chapter"):
                if chapter_text:
                    chapters[current_chapter] = "\n".join(chapter_text)
                    chapter_text = []
                current_chapter = line.strip()
        chapter_text.append(text)

    chapters[current_chapter] = "\n".join(chapter_text)
    return chapters
