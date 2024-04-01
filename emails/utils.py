from weasyprint import HTML

def convert_html_to_pdf(html_content):
    pdf_document = HTML(string=html_content).write_pdf()
    return pdf_document.getvalue()
