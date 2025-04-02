import os
from mistralai import Mistral

#client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])

def upload_pdf(api_key,pdf_path):
    client = Mistral(api_key=api_key)
    with open(pdf_path, "rb") as f:
        uploaded_pdf = client.files.upload(
            file={
                "file_name": os.path.basename(pdf_path),
                "content": f,
            },
            purpose="ocr"
        )
    print("✅ File caricato, ID:", uploaded_pdf.id)
    signed_url = client.files.get_signed_url(file_id=uploaded_pdf.id)
    return uploaded_pdf.id, signed_url.url
