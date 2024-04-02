from django.template.loader import render_to_string
from django.http import HttpResponse
from rest_framework import generics
from .models import SalesSummary
from .serializers import SalesSummarySerializer

def generate_sales_summary_html():
    # Fetch sales summary data from the database
    sales_summary = SalesSummary.objects.last()

    # Prepare context for rendering HTML template
    context = {
        'net_sales': sales_summary.net_sales,
        'gross_sales': sales_summary.gross_sales,
        'total_product_sales': sales_summary.total_product_sales,
        'taxable_sales': sales_summary.taxable_sales,
        'non_taxable_sales': sales_summary.non_taxable_sales,
        'crv_charges': sales_summary.crv_charges,
        'total_service_fees': sales_summary.total_service_fees,
        'taxable_service_fee': sales_summary.taxable_service_fee,
        'non_taxable_service_fees': sales_summary.non_taxable_service_fees,
        'shipping_and_handling': sales_summary.shipping_and_handling,
        'total_discounts': sales_summary.total_discounts,
        'item_discounts': sales_summary.item_discounts,
        'order_discounts': sales_summary.order_discounts,
        'total_tax_and_surcharges': sales_summary.total_tax_and_surcharges,
        'sales_tax': sales_summary.sales_tax,
        'prevailing_tax': sales_summary.prevailing_tax,
        'tax_rounding_variance': sales_summary.tax_rounding_variance,
        'pass_through_fee_tax': sales_summary.pass_through_fee_tax,
        'surcharges': sales_summary.surcharges,
        'crv_charges_liabilities': sales_summary.crv_charges_liabilities,
        'house_account': sales_summary.house_account,
        'payments_against_house_account': sales_summary.payments_against_house_account,
        'payments_with_house_account': sales_summary.payments_with_house_account,
        'gift_cards': sales_summary.gift_cards,
        'sold_value': sales_summary.sold_value,
        'redeemed_value': sales_summary.redeemed_value,
        'store_credit_accrued': sales_summary.store_credit_accrued,
        'store_credit_redeemed': sales_summary.store_credit_redeemed,
        'deposits': sales_summary.deposits,
        'deposit_payments': sales_summary.deposit_payments,
        'applied_deposits': sales_summary.applied_deposits,
    }

    # Render HTML template with populated data
    html_content = render_to_string('sales_summary_template.html', context)
    return html_content

class SalesSummaryAPIView(generics.ListCreateAPIView):
    queryset = SalesSummary.objects.all()
    serializer_class = SalesSummarySerializer

    def get(self, request, *args, **kwargs):
        # Generate HTML content with populated sales summary data
        html_content = generate_sales_summary_html()

        # Return HTML content as HTTP response
        return HttpResponse(html_content)
