# Yape & Plin OCR Processing 💸

Extracts transaction details from Yape and Plin screenshots and exports them to a CSV file using Tesseract OCR.

## Requirements

- Python 3.9+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed at `C:\Program Files\Tesseract-OCR\tesseract.exe` or specify a custom path.

## Setup

```bash
git clone https://github.com/david-oruna/yape-ocr.git
cd yape-ocr
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
