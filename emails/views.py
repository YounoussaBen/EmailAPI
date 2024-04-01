from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMessage
from .utils import convert_html_to_pdf

class SendEmailView(APIView):
    def post(self, request):
        data = request.data

        recipients = data.get('recipients', [])  # Handle list of recipients
        title = data.get('title')
        body = data.get('body')
        attachments = request.FILES.getlist('attachments', [])  # Handle multiple attachments

        message = EmailMessage(
            title,
            body,
            'younoussaabdourhaman@gmail.com',  # Replace with your sender email
            recipients,
            attachments=[
                (attachment.name, attachment.read(), attachment.content_type)
                for attachment in attachments
            ],
            html_message=body,
        )

        try:
            for attachment in attachments:
                if attachment.content_type.startswith('text/html'):
                    pdf_attachment = convert_html_to_pdf(attachment.read().decode())
                    message.attach(f'{attachment.name}.pdf', pdf_attachment, 'application/pdf')

            message.send()
            return Response({'message': 'Email sent successfully!'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
