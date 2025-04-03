# 🧠 SUMMARIZERAI

**SummarizerAI** è un progetto Python che riceve uno o più file PDF e, sfruttando le API di **Mistral AI**, esegue il riconoscimento del testo (OCR) e genera un riassunto in formato PDF del contenuto.

---

## 🚀 Funzionalità

- Caricamento di file PDF tramite API di Mistral
- Estrazione del testo tramite OCR
- Generazione del riassunto del contenuto
- Salvataggio del riassunto in PDF con:
  - Font **Times New Roman**
  - Paragrafi giustificati
  - Interlinea doppia
  - Titolo estratto dall’intestazione del PDF originale

---

## 🗂️ Struttura del progetto

```
summarizerai/
├── data/
│   ├── input/              # Inserisci qui i file PDF da elaborare
│   └── output/             # Verranno generati qui i file PDF riassunti
├── src/
│   ├── mistral_uploader.py # Upload dei file PDF su Mistral
│   ├── mistral_ocr.py      # OCR e estrazione testo dalle immagini
│   ├── summarizer.py       # Generazione del riassunto
│   └── pdf_writer.py       # Creazione dei file PDF di output
├── main.py                 # Punto di ingresso dell'applicazione
├── requirements.txt        # Dipendenze Python
├── .env                    # File da escludere da Git
├── .gitignore              # File da escludere da Git
└── README.md               # Documentazione del progetto
```

---

## ⚙️ Requisiti

- Python **3.8** o superiore
- Chiave API **Mistral** → [https://mistral.ai](https://mistral.ai)
- Librerie Python:
  - `mistralai`
  - `reportlab`
  - `pdfplumber`
  - `python-dotenv`

---

## 🧪 Installazione

1. **Crea un ambiente virtuale:**

```bash
python3 -m venv .venv
source .venv/bin/activate         # Su Windows: .venv\Scripts\activate

```

2. **Installa le dipendenze**

```bash
pip install -r requirements.txt
```

3. **Crea un file .env nella root del progetto con:**
```bash
MISTRAL_API_KEY=la_tua_api_key
FILE_INPUT_DIR=data/input
FILE_OUTPUT_DIR=data/output
```

## Utilizzo

1. Inserisci uno o più file PDF nella cartella data/input/
Puoi anche creare sottocartelle per organizzare i file: la struttura verrà replicata in output.

2. Esegui lo script principale:

```bash
python main.py
```

3. Esegui lo script principale:
I file riassunti saranno salvati in data/output/ con lo stesso nome (e struttura) del file di origine.

## Output

I PDF generati conterranno:

    -Titolo preso automaticamente dall’intestazione del documento

    -Riassunto generato con Mistral AI

Se il testo contiene una sezione "Bibliografia", questa verrà esclusa dal riassunto finale.-