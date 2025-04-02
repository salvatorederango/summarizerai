from src.mistral_uploader import upload_pdf
from src.mistral_ocr import extract_pages
from src.pdf_writer import save_markdown_as_pdf
from src.summarizer import summarize_text
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    api_key = os.getenv("MISTRAL_API_KEY")
    pdf_path = os.getenv("FILE_INPUT_PATH")

    file_id, signed_url = upload_pdf(api_key, pdf_path)
    pages = extract_pages(api_key, signed_url)

    output_pdf_path = os.getenv("FILE_OUTPUT_PATH")
    
    save_markdown_as_pdf(pages, output_pdf_path)

    summary = summarize_text(api_key, pages)
    print("\n🧠 Riassunto:\n")
    print(summary)

    # Salviamo anche il riassunto in un file
    with open("data/output/riassunto.txt", "w", encoding="utf-8") as f:
        f.write(summary)

if __name__ == "__main__":
    main()

