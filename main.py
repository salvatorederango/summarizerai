from src.mistral_uploader import upload_pdf
from src.mistral_ocr import extract_pages
from src.pdf_writer import save_markdown_as_pdf
from src.summarizer import summarize_text
from dotenv import load_dotenv
import os

def main():
    load_dotenv()

    api_key = os.getenv("MISTRAL_API_KEY")
    input_dir = os.getenv("FILE_INPUT_DIR", "data/input")
    output_dir = os.getenv("FILE_OUTPUT_DIR", "data/output")

    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if not filename.lower().endswith(".pdf"):
            continue

        pdf_path = os.path.join(input_dir, filename)
        print(f"Elaboro il file: {pdf_path}")

        try:
            file_id, signed_url = upload_pdf(api_key, pdf_path)
            pages = extract_pages(api_key, signed_url)

            basename = os.path.splitext(filename)[0]
            #output_pdf_path = os.path.join(output_dir, f"{basename}_estratto.md")
            output_summary_path = os.path.join(output_dir, f"{basename}_riassunto.txt")

            #save_markdown_as_pdf(pages, output_pdf_path)

            summary = summarize_text(api_key, pages)
            print(f"\n🧠 Riassunto per {filename}:\n")
            print(summary)

            with open(output_summary_path, "w", encoding="utf-8") as f:
                f.write(summary)

            print(f"✅ File completato: {filename}\n")

        except Exception as e:
            print(f"❌ Errore con {filename}: {e}")

if __name__ == "__main__":
    main()


