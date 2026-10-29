# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models


class HrContract(models.Model):
    _inherit = "hr.version"

    analytic_account_id = fields.Many2one(
        "account.analytic.account", "Analytic Account", tracking=True
    )
    journal_id = fields.Many2one("account.journal", "Salary Journal", tracking=True)

    @api.model
    def _get_whitelist_fields_from_template(self):
        whitelist = super()._get_whitelist_fields_from_template()
        for field_name in ("analytic_account_id", "journal_id"):
            if field_name not in whitelist:
                whitelist.append(field_name)
        return whitelist
