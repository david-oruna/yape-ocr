from PIL import Image
import pytesseract
import re
import cv2
pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_info(path):
    img = Image.open(path)
    text = pytesseract.image_to_string(img, lang='spa')
    # Regular expression to extract the amount (look for ¡Yapeaste! or !Te yapearon!)
    amount_match = re.search(r'(¡Yapeaste!|!Te yapearon!)\n\n(\d+)\n\n[A-Z][a-z]+', text)
    if amount_match:
        amount = amount_match.group(2)
    else:
        amount = ''
    # Regular expression to extract the name (the text immediately following the amount)
    name = re.search(r'(?<=\n)([A-Z][a-z]+ [A-Z][a-z]+(?: [A-Z][a-z]+)?)', text)
    name = name.group(1) if name else ''
    # Regular expression to extract the date and convert it to dd/mm/YYYY format
    date_match = re.search(r'(\d{2}) (\w{3})\.? (\d{4})', text)
    if date_match:
        # Map Spanish month abbreviations to numbers
        month_map = {
            'ene': '01', 'feb': '02', 'mar': '03', 'abr': '04',
            'may': '05', 'jun': '06', 'jul': '07', 'ago': '08',
            'sep': '09', 'oct': '10', 'nov': '11', 'dic': '12'
        }
        day, month_abbr, year = date_match.groups()
        month = month_map.get(month_abbr.lower(), '00')
        date = f"{day}/{month}/{year}"

    # Regular expression to extract time in 24-hour format
    time_match = re.search(r'(\d{2}):(\d{2})\s*([ap]m)', text)
    if time_match:
        hour, minute, period = time_match.groups()
        hour = int(hour)
        if period.lower() == 'pm' and hour != 12:
            hour += 12
        elif period.lower() == 'am' and hour == 12:
            hour = 0
        time = f"{hour:02}:{minute}"

    # Regular expression to extract the destination (following "Destino:")
    destination = re.search(r'Destino:\s*(\w+)', text)
    destination = destination.group(1) if destination else ''
    # Print extracted information for verification
    return {
        'Name': name,
        'Amount': amount,
       
        'Date': date,
        'Time': time,
        'Destination': destination
    }


def save_to_csv(folder_path, csv_file):
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['Name', 'Amount', 'Date', 'Time', 'Destination']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

    # Iterate through each image in the folder
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(folder_path, filename)
                extracted_data = extract_info(image_path)
                writer.writerow(extracted_data)

csv_file = 'yape_transactions.csv'
folder_path = r'C:\Users\DHO_d\Documents\GitHub\yape-ocr\folder'

save_to_csv(folder_path, csv_file)
print(f"Data successfully exported to {csv_file}")