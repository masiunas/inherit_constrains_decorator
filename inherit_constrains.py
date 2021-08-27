import logging
from odoo import api

_logger = logging.getLogger(__name__)


def constrains(*args):
    _logger.warning('*' * 100)
    _logger.warning('Triggered custom constrain')
    _logger.warning('*' * 100)
    return api.attrsetter('_constrains', args)


api.constrains = constrains
