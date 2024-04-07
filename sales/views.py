from rest_framework.exceptions import NotFound
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .firebase_client import FirebaseClient
from .serializers import SalesSummarySerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.template.loader import render_to_string
from django.http import HttpResponse

def generate_sales_summary_html(sales_summary):
    """
    Generate HTML content for the sales summary.
    """
    context = {
            'net_sales': sales_summary.get('net_sales', ''),
            'gross_sales': sales_summary.get('gross_sales', ''),
            'total_product_sales': sales_summary.get('total_product_sales', ''),
            'taxable_sales': sales_summary.get('taxable_sales', ''),
            'non_taxable_sales': sales_summary.get('non_taxable_sales', ''),
            'crv_charges': sales_summary.get('crv_charges', ''),
            'total_service_fees': sales_summary.get('total_service_fees', ''),
            'taxable_service_fee': sales_summary.get('taxable_service_fee', ''),
            'non_taxable_service_fees': sales_summary.get('non_taxable_service_fees', ''),
            'shipping_and_handling': sales_summary.get('shipping_and_handling', ''),
            'total_discounts': sales_summary.get('total_discounts', ''),
            'item_discounts': sales_summary.get('item_discounts', ''),
            'order_discounts': sales_summary.get('order_discounts', ''),
            'total_tax_and_surcharges': sales_summary.get('total_tax_and_surcharges', ''),
            'sales_tax': sales_summary.get('sales_tax', ''),
            'prevailing_tax': sales_summary.get('prevailing_tax', ''),
            'tax_rounding_variance': sales_summary.get('tax_rounding_variance', ''),
            'pass_through_fee_tax': sales_summary.get('pass_through_fee_tax', ''),
            'surcharges': sales_summary.get('surcharges', ''),
            'crv_charges_liabilities': sales_summary.get('crv_charges_liabilities', ''),
            'house_account': sales_summary.get('house_account', ''),
            'payments_against_house_account': sales_summary.get('payments_against_house_account', ''),
            'payments_with_house_account': sales_summary.get('payments_with_house_account', ''),
            'gift_cards': sales_summary.get('gift_cards', ''),
            'sold_value': sales_summary.get('sold_value', ''),
            'redeemed_value': sales_summary.get('redeemed_value', ''),
            'store_credit_accrued': sales_summary.get('store_credit_accrued', ''),
            'store_credit_redeemed': sales_summary.get('store_credit_redeemed', ''),
            'deposits': sales_summary.get('deposits', ''),
            'deposit_payments': sales_summary.get('deposit_payments', ''),
            'applied_deposits': sales_summary.get('applied_deposits', ''),
        }

    html_content = render_to_string('sales_summary_template.html', context)
    return html_content


class SalesSummaryViewSet(viewsets.ViewSet):
    client = FirebaseClient()
    """
    API view to list and create sales summaries.
    """

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'net_sales': openapi.Schema(type=openapi.TYPE_NUMBER),
                'gross_sales': openapi.Schema(type=openapi.TYPE_NUMBER),
                'total_product_sales': openapi.Schema(type=openapi.TYPE_NUMBER),
                'taxable_sales': openapi.Schema(type=openapi.TYPE_NUMBER),
                'non_taxable_sales': openapi.Schema(type=openapi.TYPE_NUMBER),
                'crv_charges': openapi.Schema(type=openapi.TYPE_NUMBER),
                'total_service_fees': openapi.Schema(type=openapi.TYPE_NUMBER),
                'taxable_service_fee': openapi.Schema(type=openapi.TYPE_NUMBER),
                'non_taxable_service_fees': openapi.Schema(type=openapi.TYPE_NUMBER),
                'shipping_and_handling': openapi.Schema(type=openapi.TYPE_NUMBER),
                'total_discounts': openapi.Schema(type=openapi.TYPE_NUMBER),
                'item_discounts': openapi.Schema(type=openapi.TYPE_NUMBER),
                'order_discounts': openapi.Schema(type=openapi.TYPE_NUMBER),
                'total_tax_and_surcharges': openapi.Schema(type=openapi.TYPE_NUMBER),
                'sales_tax': openapi.Schema(type=openapi.TYPE_NUMBER),
                'prevailing_tax': openapi.Schema(type=openapi.TYPE_NUMBER),
                'tax_rounding_variance': openapi.Schema(type=openapi.TYPE_NUMBER),
                'pass_through_fee_tax': openapi.Schema(type=openapi.TYPE_NUMBER),
                'surcharges': openapi.Schema(type=openapi.TYPE_NUMBER),
                'crv_charges_liabilities': openapi.Schema(type=openapi.TYPE_NUMBER),
                'house_account': openapi.Schema(type=openapi.TYPE_NUMBER),
                'payments_against_house_account': openapi.Schema(type=openapi.TYPE_NUMBER),
                'payments_with_house_account': openapi.Schema(type=openapi.TYPE_NUMBER),
                'gift_cards': openapi.Schema(type=openapi.TYPE_NUMBER),
                'sold_value': openapi.Schema(type=openapi.TYPE_NUMBER),
                'redeemed_value': openapi.Schema(type=openapi.TYPE_NUMBER),
                'store_credit_accrued': openapi.Schema(type=openapi.TYPE_NUMBER),
                'store_credit_redeemed': openapi.Schema(type=openapi.TYPE_NUMBER),
                'deposits': openapi.Schema(type=openapi.TYPE_NUMBER),
                'deposit_payments': openapi.Schema(type=openapi.TYPE_NUMBER),
                'applied_deposits': openapi.Schema(type=openapi.TYPE_NUMBER),
            },
        ),
        responses={200: SalesSummarySerializer}  # Specify response schema
    )

    def create(self, request, *args, **kwargs):
        serializer = SalesSummarySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.client.create(serializer.data)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    def list(self, request):
        # Get all sales summaries
        sales_summary_data = self.client.all()

        if sales_summary_data:
            serializer = SalesSummarySerializer(sales_summary_data, many=True)
            return Response(serializer.data)
        else:
            return Response("No sales summaries found.", status=status.HTTP_404_NOT_FOUND)
        
    def retrieve(self, request, pk=None):
        sales_summary = self.client.get_by_id(pk)

        if sales_summary:
            serializer = SalesSummarySerializer(sales_summary)
            sales_summary_html = generate_sales_summary_html(serializer.data)
            return HttpResponse(sales_summary_html)

        raise NotFound(detail="Sales Summary Not Found", code=404)

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.client.delete_by_id(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        serializer = SalesSummarySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.client.update(pk, serializer.data)

        return Response(serializer.data)
