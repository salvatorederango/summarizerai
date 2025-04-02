# 🧠 PdfSummarizerAI

**PdfSummarizerAI** è un progetto Python che riceve un file PDF e, sfruttando le API di **Mistral AI**, esegue il riconoscimento del testo (OCR) e restituisce un riassunto del contenuto.

---

## 🚀 Funzionalità

- Carica un file PDF (tramite API Mistral)
- Ottiene un URL firmato dal file caricato
- Richiede il riassunto del documento tramite OCR
- Restituisce il testo estratto e riassunto

---

## 🗂️ Struttura del progetto

PdfSummarizerAI/ ├── data/ │ └── input/ # Inserisci qui i file PDF da elaborare ├── src/ │ ├── mistral_uploader.py # Upload dei file PDF │ ├── mistral_ocr.py # Richiesta OCR e riassunto ├── main.py # Punto di ingresso principale ├── .gitignore # Esclusione file da Git ├── requirements.txt # Dipendenze Python └── README.md # Questo file


---

## ⚙️ Requisiti

- Python 3.8 o superiore
- Chiave API di Mistral: [https://mistral.ai](https://mistral.ai)
- Libreria `mistralai` installata (SDK ufficiale)

---

## 🧪 Installazione

1. **Crea un ambiente virtuale (opzionale ma consigliato):**

```bash
python3 -m venv .venv
source .venv/bin/activate   # Su Windows: .venv\Scripts\activate


Installa le dipendenze:

pip install -r requirements.txt

pip freeze > requirements.txt


Esporta la tua API key Mistral:

export MISTRAL_API_KEY=la_tua_api_key

Su Windows: set MISTRAL_API_KEY=la_tua_api_key


Esegui il programma:

python main.py


Utilizzo
Inserisci un file PDF nella cartella data/input/ (es: 1.pdf)

Avvia main.py

Otterrai un riassunto stampato in console
