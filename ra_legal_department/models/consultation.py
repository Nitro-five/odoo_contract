from odoo import models, fields, api


class Consultation(models.Model):
    _name = 'ra_legal_department.consultation'
    _description = 'Consultation'

    name = fields.Char(string='Назва', required=True)
    consultation_date = fields.Datetime(string='Дата консультації', required=True,
                                        default=lambda self: fields.Datetime.now())
    client_id = fields.Many2one('res.partner', string='Замовник')
    responsible_id = fields.Many2one('res.users', string='Відповідальний', default=lambda self: self.env.user,
                                     required=True)

    state = fields.Selection([
        ('draft', 'Чернетка'),
        ('published', 'Опубліковано'),
        ('cancel', 'Скасовано')
    ], string="Статус", readonly=True, default='draft')

    requested_information = fields.Text(string='Запитувана інформація')
    consultation_text = fields.Html(string='Текст консультації')
    document_ids = fields.One2many('ra_legal_department.document', 'consultation_id',
                                   string="Прикріпити документи")


    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'

    def action_publish(self):
        self.state = 'published'
    # todo Сделать Мейл темплейт

    def send_email_with_consultation(self):
        pass


