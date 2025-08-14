import pdfplumber
import sys

def extract_pdf_text(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() or ""
            return text
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

if __name__ == "__main__":
    pdf_path = r"c:\Users\Meet\Desktop\Meet\Resume\Meet_Resume.pdf"
    text = extract_pdf_text(pdf_path)
    print(text)
