import os
import argparse
import pytesseract
import sys
from src.utils import process_images_in_folder
from src.utils import export_data_to_csv

def check_tesseract_installation(tesseract_cmd):
    if not os.path.exists(tesseract_cmd):
        print(f"Tesseract executable not found at {tesseract_cmd}.\n")
        print("To install Tesseract OCR, please follow these steps:\n")
        print("1. Download the Tesseract installer from the official repository:")
        print("   https://github.com/tesseract-ocr/tesseract")
        print("2. Run the installer and follow the instructions.")
        print("3. By default, Tesseract will be installed to:")
        print("   C:\\Program Files\\Tesseract-OCR\\tesseract.exe (Windows)\n")
        print("4. If you installed Tesseract in a different location,")
        print("   specify the path using the --tesseract argument when running this script.")
        print("\nAfter installing, rerun this script.")
        sys.exit(1)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Process yape screenshots and exports info to CSV.")
    
    parser.add_argument(
        '--input', '-i',
        type=str,
        required=True,
        help="Path to the folder containing the screenshots."
    )
    
    parser.add_argument(
        '--output', '-o',
        type=str,
        required=True,
        help="Path to save the output CSV file."
    )
    
    parser.add_argument(
        '--tesseract', '-t',
        type=str,
        default=r"C:\Program Files\Tesseract-OCR\tesseract.exe",  # Default path
        help="Path to the Tesseract OCR executable."
    )
    
    args = parser.parse_args()

    # Check if Tesseract is installed at the specified path
    check_tesseract_installation(args.tesseract)

    # Set Tesseract command path
    pytesseract.pytesseract.tesseract_cmd = args.tesseract

    # Process images in the folder and extract data
    extracted_data = process_images_in_folder(args.input)
    
    # Export the extracted data to CSV
    export_data_to_csv(extracted_data, args.output)
    
    print(f"Data successfully exported to {args.output}")

if __name__ == "__main__":
    main()
