# models.py
from django.db import models

class SalesSummary(models.Model):

    net_sales = models.DecimalField(max_digits=10, decimal_places=2)
    gross_sales = models.DecimalField(max_digits=10, decimal_places=2)
    total_product_sales = models.DecimalField(max_digits=10, decimal_places=2)
    taxable_sales = models.DecimalField(max_digits=10, decimal_places=2)
    non_taxable_sales = models.DecimalField(max_digits=10, decimal_places=2)
    crv_charges = models.DecimalField(max_digits=10, decimal_places=2)
    total_service_fees = models.DecimalField(max_digits=10, decimal_places=2)
    taxable_service_fee = models.DecimalField(max_digits=10, decimal_places=2)
    non_taxable_service_fees = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_and_handling = models.DecimalField(max_digits=10, decimal_places=2)
    total_discounts = models.DecimalField(max_digits=10, decimal_places=2)
    item_discounts = models.DecimalField(max_digits=10, decimal_places=2)
    order_discounts = models.DecimalField(max_digits=10, decimal_places=2)
    total_tax_and_surcharges = models.DecimalField(max_digits=10, decimal_places=2)
    sales_tax = models.DecimalField(max_digits=10, decimal_places=2)
    prevailing_tax = models.DecimalField(max_digits=10, decimal_places=2)
    tax_rounding_variance = models.DecimalField(max_digits=10, decimal_places=2)
    pass_through_fee_tax = models.DecimalField(max_digits=10, decimal_places=2)
    surcharges = models.DecimalField(max_digits=10, decimal_places=2)
    crv_charges_liabilities = models.DecimalField(max_digits=10, decimal_places=2)
    house_account = models.DecimalField(max_digits=10, decimal_places=2)
    payments_against_house_account = models.DecimalField(max_digits=10, decimal_places=2)
    payments_with_house_account = models.DecimalField(max_digits=10, decimal_places=2)
    gift_cards = models.DecimalField(max_digits=10, decimal_places=2)
    sold_value = models.DecimalField(max_digits=10, decimal_places=2)
    redeemed_value = models.DecimalField(max_digits=10, decimal_places=2)
    store_credit_accrued = models.DecimalField(max_digits=10, decimal_places=2)
    store_credit_redeemed = models.DecimalField(max_digits=10, decimal_places=2)
    deposits = models.DecimalField(max_digits=10, decimal_places=2)
    deposit_payments = models.DecimalField(max_digits=10, decimal_places=2)
    applied_deposits = models.DecimalField(max_digits=10, decimal_places=2)


