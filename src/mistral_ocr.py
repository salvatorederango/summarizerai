from mistralai import Mistral


def extract_pages(api_key, signed_url):
    client = Mistral(api_key=api_key)
    
    ocr_response = client.ocr.process(
        model="mistral-ocr-latest",
        document={
            "type": "document_url",
            "document_url": signed_url, 
        }
    )
    return ocr_response.pages


def extract_header(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            candidate_headers = []

            for page in pdf.pages:
                text = page.extract_text()
                lines = text.split("\n") if text else []
                if lines:
                    # Prendiamo solo la prima riga della pagina, che dovrebbe essere l'intestazione
                    candidate_headers.append(lines[0].strip())

            # Trova l'intestazione più frequente
            if candidate_headers:
                from collections import Counter
                most_common = Counter(candidate_headers).most_common(1)
                if most_common:
                    return most_common[0][0]

    except Exception as e:
        print(f"⚠️ Errore nell'estrazione dell'intestazione da {pdf_path}: {e}")
    
    return "Riassunto del documento"
