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
