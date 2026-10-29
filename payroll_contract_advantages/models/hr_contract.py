# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class HrContract(models.Model):
    # Odoo 19+: contracts are employee versions (hr.version)
    _inherit = "hr.version"

    # copy=True: a new version of the employee keeps the contract advantages
    advantages_ids = fields.One2many(
        "hr.contract.advantage",
        "contract_id",
        string="Contract Advantages",
        copy=True,
    )
