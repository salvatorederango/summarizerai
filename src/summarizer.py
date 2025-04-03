from mistralai import Mistral

def summarize_text(api_key, pages):
    client = Mistral(api_key=api_key)

    # Uniamo il markdown delle pagine in un unico prompt
    full_text = "\n\n".join([p.markdown for p in pages])

    model = "mistral-large-latest"

    # Chiamata al modello di chat
    response = client.chat.complete(
    model= model,
    messages = [
            {
                "role": "user",
                "content": "Fai il riassunto del seguente testo per ogni paragrafo che trovi? Non deve essere brevissimo, e deve contenere tutti i concetti principali. Dovrò rispondere ad una batteria di domande: "+full_text,
                #"content": "Fai il riassunto del seguente testo per ogni paragrafo che trovi e mi fai un elenco puntato di tutti i concetti da ricordare che possono chiedermi sempre per ogni paragrafo "+full_text,
                #"content": " mi fai un elenco puntato di tutti i concetti da ricordare che possono chiedermi per ogni paragrafo che trovi nel seguente testo: "+full_text,
                #"content": "Fai un riassunto per ogni paragrafo facendo un elenco puntato delle cose da ricordare, dovrò rispondere a delle domande: "+full_text,
                
                #"content": "Mi riassumi per paragrafo questo testo? non deve essere troppo corto: "+full_text,

            },
        ]
    )
    summary = response.choices[0].message.content
    return summary

