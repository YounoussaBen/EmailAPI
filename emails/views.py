from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services.email_sender import send_email
from sales.views import generate_sales_summary_html
import base64
class SendEmailAPIView(APIView):
    def post(self, request):
        try:
            data = request.data
            sender = data.get('from')
            recipients = data.get('to', [])
            subject = data.get('subject', '')
            text = data.get('text', '')
            attachments = data.get('attachments', [])

            # Generate HTML content for the sales summary report
            html_content = generate_sales_summary_html()

            # Convert HTML content to base64
            html_content_base64 = base64.b64encode(html_content.encode()).decode()

            # Prepare email payload with HTML content as attachment
            attachments.append({
                'filename': 'sales_summary_report.html',
                'content': html_content_base64
            })

            # Send email with sales summary report as attachment
            send_email(sender, recipients, subject, text, attachments)
            
            return Response({"message": "Email sent successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
