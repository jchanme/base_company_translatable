# © initOS GmbH 2017
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HrEmpolyee(models.Model):
    _inherit = 'hr.employee'

    name = fields.Char(translate=True)
    work_location = fields.Char(translate=True)
