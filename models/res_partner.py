import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    test_field = fields.Char(string='Test')

    @api.constrains('test_field')
    def check_test_field(self):
        _logger.warning('*' * 100)
        _logger.warning('Triggered check_test_field')
        _logger.warning('*' * 100)
