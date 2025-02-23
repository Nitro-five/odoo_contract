from odoo import models, fields

class GospodarskaSprava(models.Model):
    _name = 'ra_legal_department.legal_dispute'
    _description = 'Юридичні спори'

    # Основные поля
    name = fields.Char(string='Назва', required=True)  # Название спора
    responsible_id = fields.Many2one('res.users', string='Відповідальний')
    claimant_id = fields.Many2one('res.partner', string='Позивач')
    defendant_id = fields.Many2one('res.partner', string='Відповідач')
    start_date = fields.Date(string='Дата початку')
    statute_of_limitations = fields.Date(string='Строки давності')
    end_date = fields.Date(string='Дата завершення')

    # Поле типа спора (например, гражданский, административный и т.д.)
    dispute_type = fields.Selection([
        ('civil', 'Цивільний'),
        ('commercial', 'Господарський'),
        ('administrative', 'Адміністративний')
    ], string='Тип спору', required=True)

    # Поле текущего статуса спора
    current_status = fields.Selection([
        ('dosudove', 'Досудове'),
        ('persha_instancia', 'Перша інстанція'),
        ('apelyaciya', 'Апеляційна інстанція'),
        ('kasaciya', 'Касаційна інстанція'),
        ('vykonavche', 'Виконавче провадження')
    ], string='Поточний стан', default='dosudove')

    # Поле для прикрепления документов
    document_ids = fields.Many2many('ir.attachment', string='Документи')

    # Поле адвоката
    lawyer_id = fields.Many2one('res.partner', string='Адвокат')

    # Поля для вкладки "Перша інстанція"
    court_name = fields.Char(string='Назва суду')
    unique_case_number = fields.Char(string='Єдиний унікальний номер справи')
    proceeding_number = fields.Char(string='Номер провадження')
    case_received_date = fields.Date(string='Дата надходження справи')
    judge_name = fields.Char(string='Склад суду')
    party_details = fields.Text(string='Сторони спору')
    claim_type = fields.Text(string='Предмет позову')
    hearing_stage = fields.Char(string='Стадія розгляду')
    hearing_date = fields.Date(string='Дата розгляду')
    hearing_notes = fields.Text(string='Примітки до розгляду')


    def compute_report_vals(self):

        self.report_value = 1

    # Методы действий
    def end_disput(self):
        """Метод завершения спора"""
        pass

    def zvernuty_za_konsultaciieyu(self):
        """Метод обращения за консультацией"""
        pass

    def napysaty_lysta(self):
        """Метод для написания письма"""
        pass

    def vidpravyty_pretenziyu(self):
        """Метод для отправки претензии"""
        pass

    def podaty_pozovnu_zayavu(self):
        """Метод для подачи искового заявления"""
        pass

    def podaty_klopotannya(self):
        """Метод для подачи ходатайства"""
        pass

    def podaty_vidziv_na_pozovnu_zayavu(self):
        """Метод для подачи отзыва на исковое заявление"""
        pass

    def podaty_zaperechennya_na_vidziv(self):
        """Метод для подачи возражения на отзыв"""
        pass

    def podaty_mirovu_ugodu(self):
        """Метод для подачи мирового соглашения"""
        pass

    def podaty_apelyaciynu_skargu(self):
        """Метод для подачи апелляционной жалобы"""
        pass
