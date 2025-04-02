from fpdf import FPDF
import os

def save_markdown_as_pdf(pages, output_path):
    """
    Salva il contenuto Markdown delle pagine OCR in un file PDF.
    """
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    for page in pages:
        pdf.add_page()
        # Converti Markdown in testo semplice (puoi anche usare markdown2 se vuoi renderlo meglio)
        clean_text = page.markdown.replace("#", "").strip()
        for line in clean_text.split("\n"):
            pdf.multi_cell(0, 10, line)

    # Assicurati che la cartella esista
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    pdf.output(output_path)

    print(f"📄 PDF salvato in: {output_path}")
