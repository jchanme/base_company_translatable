from odoo import fields, models


class CompanyInfo(models.Model):
    _inherit = 'res.partner'

    company_name = fields.Char(translate=True)
    name = fields.Char(translate=True)
    city = fields.Char(translate=True)
    street = fields.Char(translate=True)
    street2 = fields.Char(translate=True)
