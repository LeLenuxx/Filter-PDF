from pathlib import Path
from pypdf import PdfReader

pdf_file_path = "./article data/pdf/Data one (500) with duplicates.PDF"

def extract_text_from_pdf():
    reader = PdfReader(pdf_file_path)
    text = ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text() + "\n"
    return text  

extracted_text = extract_text_from_pdf()

output_file = Path(pdf_file_path).stem + ".txt"
with open(output_file, "w", encoding="utf-8") as file:
    file.write(extracted_text)

print(f"text to {output_file}")

