from odoo import models, fields



class FinancialAssistanceContract(models.Model):
    _name = 'financial.assistance.contracts'
    _description = 'Фінансова допомога'

    # name = fields.Char(string='Назва договору', required=True)
    partner_id = fields.Many2one('res.partner', string='Контрагент', required=True)
    date_start = fields.Date(string='Дата початку', required=True)
    date_end = fields.Date(string='Дата закінчення')
    amount = fields.Float(string='Сума фінансової допомоги', required=True)
    penalty = fields.Float(string='Штраф (%)', help="Штраф за порушення строків повернення")
    terms = fields.Text(string='Умови договору', help="Текстові умови договору")
    status = fields.Selection([
        ('draft', 'Чернетка'),
        ('active', 'Активний'),
        ('closed', 'Закритий'),
    ], string='Статус', default='draft')

    def activate_contract(self):
        self.status = 'active'

    def close_contract(self):
        self.status = 'closed'


