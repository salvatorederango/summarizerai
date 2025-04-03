from src.mistral_uploader import upload_pdf
from src.mistral_ocr import extract_pages, extract_header
from src.pdf_writer import save_summary_as_pdf
from src.summarizer import summarize_text
from dotenv import load_dotenv
import os
import pdfplumber
import re
from collections import Counter
import warnings

warnings.filterwarnings("ignore", message="CropBox missing from /Page")

def extract_header(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            candidate_headers = []

            for page in pdf.pages:
                text = page.extract_text()
                lines = text.split("\n") if text else []
                if lines:
                    candidate_headers.append(lines[0].strip())

            if candidate_headers:
                most_common = Counter(candidate_headers).most_common(1)
                if most_common:
                    return most_common[0][0]

    except Exception as e:
        print(f"⚠️ Errore nell'estrazione dell'intestazione da {pdf_path}: {e}")
    
    return "Riassunto del documento"

def main():
    load_dotenv()

    api_key = os.getenv("MISTRAL_API_KEY")
    input_root = os.getenv("FILE_INPUT_DIR", "data/input")
    output_root = os.getenv("FILE_OUTPUT_DIR", "data/output")

    for root, dirs, files in os.walk(input_root):
        for filename in files:
            if not filename.lower().endswith(".pdf"):
                continue

            pdf_path = os.path.join(root, filename)
            print(f"📄 Elaboro il file: {pdf_path}")

            try:
                file_id, signed_url = upload_pdf(api_key, pdf_path)
                pages = extract_pages(api_key, signed_url)
                header_text = extract_header(pdf_path)

                # Percorso output mantenendo la struttura
                relative_path = os.path.relpath(root, input_root)
                output_dir = os.path.join(output_root, relative_path)
                os.makedirs(output_dir, exist_ok=True)

                basename = os.path.splitext(filename)[0]
                output_summary_pdf = os.path.join(output_dir, f"{basename}_riassunto.pdf")

                summary = summarize_text(api_key, pages)

                # Rimuove eventuale sezione "Bibliografia"
                if "bibliografia" in summary.lower():
                    summary = summary[:summary.lower().index("bibliografia")]

                save_summary_as_pdf(summary, output_summary_pdf, header_text)

                print(f"✅ File completato: {filename}\n")

            except Exception as e:
                print(f"❌ Errore con {filename}: {e}")

if __name__ == "__main__":
    main()
