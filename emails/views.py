# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services.email_sender import send_email


class SendEmailAPIView(APIView):
    def post(self, request):
        try:
            data = request.data
            sender = data.get('from')
            recipients = data.get('to', [])
            subject = data.get('subject', '')
            text = data.get('text', '')
            attachments = data.get('attachments', [])

            send_email(sender, recipients, subject, text, attachments)
            
            return Response({"message": "Email sent successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
