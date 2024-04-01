# utils.py
from weasyprint import HTML
from io import BytesIO

class PDFConverter:
    @staticmethod
    def html_to_pdf(html_content, output_file):
        """
        Convert HTML content to PDF.

        :param html_content: HTML content to convert.
        :param output_file: File-like object to write the PDF output.
        """
        html = HTML(string=html_content)
        html.write_pdf(output_file)
