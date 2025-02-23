from odoo import models, fields


class Examination(models.Model):
    _name = 'ra_legal_department.examination'
    _description = 'Перевірки'

    name = fields.Char(string='Назва перевірки', required=True)
    date_planned = fields.Date(string='Дата початку', required=True)
    date_done = fields.Date(string='Дата завершення')
    state = fields.Selection([
        ('planned', 'Планується'),
        ('in_progress', 'В процесі'),
        ('completed', 'Завершена'),
        ('cancelled', 'Скасована'),
    ], string='Статус', default='planned')

    inspection_type = fields.Selection([
        ('scheduled', 'Планова'),
        ('unscheduled', 'Позапланова'),
        ('cameral', 'Камеральна'),
    ], string='Тип перевірки')

    responsible_id = fields.Many2one('res.users', string='Відповідальний', default=lambda self: self.env.user)
    state_organization_id = fields.Char()
    documents_ids = fields.One2many('ra_legal_department.document', 'examination_id', string='Документи')
    government_organization = fields.Char(string='Орган, що перевіряє')
    company_id = fields.Many2one('res.company', string='Компанія')

    def action_in_progress(self):
        self.state = 'in_progress'
        # Дополнительная логика, если необходимо

    def action_complete(self):
        self.state = 'completed'
        self.date_done = fields.Datetime.now()  # Установить дату завершения на текущее время

    def action_cancel(self):
        self.state = 'cancelled'
        # Дополнительная логика, если необходимо
