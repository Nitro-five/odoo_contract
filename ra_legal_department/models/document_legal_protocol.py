from odoo import models, fields, api


class ProtocolDocument(models.Model):
    _inherit = 'ra_legal_department.document'

    # Участники собрания:
    legal_protocol_quality_of_questions = fields.Char(string='Голова зборів')
    legal_protocol_head_of_protocol = fields.Char(string='Голова зборів')
    legal_protocol_secretary_of_protocol = fields.Char(string='Секретар зборів')

    legal_protocol_quality_ids = fields.Many2many("res.partner")
    legal_protocol_members_ids = fields.Many2many("ra_res_company.founders")

    # Подписи:
    legal_protocol_chairman_sign = fields.Char(string='Підпис голови зборів')
    legal_protocol_secretary_sign = fields.Char(string='Підпис секретаря')


    # Текст протокола
    description = fields.Html(string="Текст Протоколу", help="Основний текст протоколу")
