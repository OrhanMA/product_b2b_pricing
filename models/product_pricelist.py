from odoo import fields, models


class ProductPricelist(models.Model):
    _inherit = "product.pricelist"

    product_b2b_pricelist = fields.Boolean(
        string="B2B Pricelist",
        index=True,
        copy=True,
    )
