from odoo import fields, models, api, _
from odoo.exceptions import UserError
import urllib.parse
from odoo.http import request


class Document(models.Model):
    _name = 'ra_legal_department.document'

    ######################################## Поля и Настройки документа ##################################################
    document_have_registration = fields.Boolean()
    show_document_have_registration = fields.Boolean()
    document = fields.Many2one('ir.attachment', string='Related attachment', required=True, ondelete='cascade')
    filename = fields.Char(string="Filename")
    name = fields.Char()
    examination_id = fields.Many2one('ra_legal_department.examination')
    consultation_id = fields.Many2one('ra_legal_department.consultation')
    state = fields.Char()
    date_of_document = fields.Date()
    responsible_user_id = fields.Many2one("res.users")

    type_of_document = fields.Selection([
        ('incoming', 'Вхідний'),
        ('outgoing', 'Вихідний'),
        ('internal', 'Внутрішній')],
        string="Вид документу", default="outgoing", required=True)
    type_of_internal_document = fields.Selection([('protocol', 'Протокол'), ('order', 'Наказ')], string="Вид документу")

    type_of_legal_document = fields.Selection([
        ('application', 'Заява'),
        ('complaint', 'Скарга'),
        ('letter', 'Лист'),
        ('claim', 'Претензія'),
        ('request', 'Запит'),
        ('power_of_attorney', 'Довіреність'),
        ('certificate', 'Довідка'),
        ('other', 'Інше')], string="Юридичний тип документу", default="application")

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

    internal_number_of_document = fields.Char(string="Внутрішній номер")

    document_attachment = fields.Many2many('ir.attachment', string="Прикріпити документ")
    company_id = fields.Many2one("res.company", string="Company")

    def publish_document(self):
        pass

    def mark_as_draft(self):
        pass

    def cancel(self):
        pass

    def cancel_document_registration(self):
        pass
