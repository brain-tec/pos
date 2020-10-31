# Copyright (C) 2020 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    max_meal_voucher_amount = fields.Monetary(
        string="Meal Voucher Amount",
        currency_field="currency_id",
    )

    meal_voucher_display_product_screen = fields.Boolean(
        string="Display icon before products on screen",
        default=True)
