from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER

def save_summary_as_pdf(text, output_path, header_text="Riassunto del documento"):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=72,
        rightMargin=72,
        topMargin=72,
        bottomMargin=72
    )

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name='DoubleSpaced',
        fontName='Times-Roman',
        fontSize=12,
        leading=24,
        alignment=TA_JUSTIFY
    ))
    styles.add(ParagraphStyle(
        name='TitleStyle',
        fontName='Times-Roman',
        fontSize=16,
        leading=28,
        alignment=TA_CENTER,
        spaceAfter=24
    ))

    elements = []

    # Titolo iniziale
    elements.append(Paragraph(f"<b>{header_text}</b>", styles['TitleStyle']))
    elements.append(Spacer(1, 24))

    # Corpo del testo
    paragraphs = text.split("\n")
    for para in paragraphs:
        if para.strip() == "":
            elements.append(Spacer(1, 12))
            continue
        if para.strip().startswith("#"):
            clean_title = para.lstrip("#").strip()
            elements.append(Paragraph(f"<b>{clean_title}</b>", styles['DoubleSpaced']))
        else:
            elements.append(Paragraph(para.strip(), styles['DoubleSpaced']))
        elements.append(Spacer(1, 12))

    doc.build(elements)
    print(f"📄 PDF salvato in: {output_path}")
