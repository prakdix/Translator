# Hindi Book Translator

This project uses GPT-4o and ReportLab to translate English PDFs into Hindi and output them as styled PDFs. Initially built to translate *How to Meditate* by Pema Chödrön for family.

### Features
- Chapter-wise extraction and translation
- Custom Hindi font support
- Clean PDF output with quotes and formatting

### Setup

```bash
git clone https://github.com/your-username/translator.git
cd translator
pip install -r requirements.txt
cp .env.example .env  # Add your OpenAI API key here
