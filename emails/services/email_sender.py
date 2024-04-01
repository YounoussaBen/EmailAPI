# utils/email_sender.py

import requests
from .pdf_converter import PDFConverter
from io import BytesIO
from settings import base


def send_email(sender, recipients, subject, text, attachments=[]):
    
    
    email_data = {
        "from": sender,
        "to": recipients,
        "subject": subject,
        "text": text
    }

    files = prepare_attachments(attachments)
    response = requests.post(base.MAILGUN_API_URL, auth=("api", base.MAILGUN_API_KEY), data=email_data, files=files)
    response.raise_for_status()
    return response


def prepare_attachments(attachments):
    files = []
    for attachment in attachments:
        if attachment['filename'].endswith('.html'):
            pdf_output = BytesIO()
            PDFConverter.html_to_pdf(attachment['content'], pdf_output)
            files.append(('attachment', (attachment['filename'][:-5] + '.pdf', pdf_output.getvalue())))
        else:
            files.append(('attachment', (attachment['filename'], attachment['content'])))
    return files
