from . import models
from odoo import api, SUPERUSER_ID

def create_sequences(cr, registry):

    env = api.Environment(cr, SUPERUSER_ID, {})
    env["res.company"].create_all_sequence_in_companies()

