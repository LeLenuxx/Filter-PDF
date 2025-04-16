from pypdf import PdfReader

def extract_text_from_pdf():
    reader = PdfReader("./article data/Data two - ohne Duplikate.pdf")
    text = ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text() + "\n"
    return text  

extracted_text = extract_text_from_pdf()

output_file = "extract_text.txt"
with open(output_file, "w", encoding="utf-8") as file:
    file.write(extracted_text)

print(f"text to {output_file}")

