from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    product_b2b_base_price = fields.Monetary(string="B2B Base Price")
    product_b2b_distributor_price = fields.Monetary(string="Distributor Price")
    product_b2b_preorder = fields.Boolean(string="B2B Preorder", index=True)
    product_b2b_enabled = fields.Boolean(string="B2B Product", index=True)
