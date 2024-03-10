# OCR Project for Yape and Plin Screenshots

## Overview

This project utilizes Pytesseract OCR to extract information from screenshots related to Yape and Plin. The extracted data includes name, amount, date, time, and destination.

## Project Structure

- **data/:** Directory to store sample data or any necessary data.
- **docs/:** Documentation files.
  - **images/:** Images for documentation.
  - **requirements.md:** Project requirements.
  - **design.md:** Design and architecture documentation.
- **src/:** Source code.
  - **ocr_project/:** Main project code.
    - **utils/:** Utility functions.
    - **ocr_processor.py:** OCR processing module.
  - **tests/:** Unit tests.
  - **main.py:** Entry point for the application.
- **.gitignore:** Git ignore file.
- **LICENSE:** Project license.
- **README.md:** Project readme file.
- **requirements.txt:** Python dependencies.
- **.git/:** Git configuration and data.

## Usage

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the main script:
    ```bash
    python src/main.py /path/to/image.jpg
    ```

## Contributing

If you want to contribute to this project, please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

