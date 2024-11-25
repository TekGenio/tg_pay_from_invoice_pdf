from odoo import models, fields, api, _
from datetime import datetime
from werkzeug import urls
from odoo.addons.payment import utils as payment_utils

class AccountMove(models.Model):
    _inherit = 'account.move'

    payment_link = fields.Char(string="Payment Link")

    def action_post(self):
        res = super().action_post()
        self._compute_link()
        return res

    def _get_additional_link_values(self):
        """ Return the additional values to append to the payment link.

        Note: self.ensure_one()

        :return: The additional payment link values.
        :rtype: dict
        """
        self.ensure_one()
        return {
            'currency_id': self.currency_id.id,
            'partner_id': self.partner_id.id,
            'company_id': self.company_id.id,
        }

    def _get_access_token(self):
        self.ensure_one()
        return payment_utils.generate_access_token(
            self.partner_id.id, self.amount_total, self.currency_id.id
        )

    @api.depends('amount_total', 'currency_id', 'partner_id', 'company_id')
    def _compute_link(self):
        for rec in self:
            related_document = rec
            base_url = related_document.get_base_url()  # Don't generate links for the wrong website
            url_params = {
                'amount': self.amount_total,
                'access_token': self._get_access_token(),
                'invoice_id' : self.id,
                'company_id': self.env.company.id,
            }
            rec.payment_link = f'{base_url}/payment/pay?{urls.url_encode(url_params)}'


