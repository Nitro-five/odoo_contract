import base64
import io
from odoo.modules.module import get_module_path
from docxtpl import DocxTemplate
from odoo import models, fields, _
from odoo.exceptions import UserError


class Contract(models.Model):
    """
    Модель для работы с договорами.
    """

    _name = 'contract.contract'
    _description = 'Договір'

    name = fields.Char(string="Номер договору", required=True)
    contract_type = fields.Selection([
        ('sale', 'Купівля-продаж'),
        ('rent', 'Оренда'),
        ('other', 'Інший'),
    ], string="Тип договору", default='sale', required=True)
    date = fields.Date(string="Дата договору", default=fields.Date.context_today)
    partner_id = fields.Many2one('res.partner', string="Контрагент")
    amount = fields.Float(string="Сума договору")
    state = fields.Selection([
        ('draft', 'Чернетка'),
        ('confirmed', 'Підтверджено'),
        ('cancel', 'Відмінено')
    ], string="Статус", default='draft')

    city = fields.Char(string="Місто")
    seller_name = fields.Char(string="Продавець")
    seller_representative = fields.Char(string="Представник продавця")
    buyer_name = fields.Char(string="Покупець")
    buyer_representative = fields.Char(string="Представник покупця")
    vehicle_brand = fields.Char(string="Марка транспортного засобу")
    vehicle_model = fields.Char(string="Модель транспортного засобу")
    vehicle_year = fields.Char(string="Рік випуску")
    vehicle_color = fields.Char(string="Колір")
    vehicle_vin = fields.Char(string="Номер кузова")
    vehicle_reg = fields.Char(string="Свідоцтво про реєстрацію")
    total_price = fields.Char(string="Загальна ціна")
    product_quantity = fields.Float(string="Кількість товару", default=1.0)
    product_price = fields.Float(string="Ціна товару", required=True)
    vat = fields.Char(string="ПДВ")
    seller_address = fields.Char(string="Адреса продавця")
    seller_account = fields.Char(string="Р/Р продавця")
    seller_bank = fields.Char(string="Банк продавця")
    seller_mfo = fields.Char(string="МФО продавця")
    seller_edrpou = fields.Char(string="ЄДРПОУ продавця")
    seller_phone = fields.Char(string="Телефон продавця")
    seller_email = fields.Char(string="Email продавця")
    buyer_address = fields.Char(string="Адреса покупця")
    buyer_account = fields.Char(string="Р/Р покупця")
    buyer_bank = fields.Char(string="Банк покупця")
    buyer_mfo = fields.Char(string="МФО покупця")
    buyer_edrpou = fields.Char(string="ЄДРПОУ покупця")
    buyer_phone = fields.Char(string="Телефон покупця")

    def generate_docx(self):
        """
        Генерация документа DOCX на основе шаблона.
        Возвращает сгенерированный файл в формате base64.
        """

        self.ensure_one()
        module_path = get_module_path('contract')
        template_path = module_path + '/static/templates/Dogovir.docx'

        try:
            doc = DocxTemplate(template_path)
        except Exception as e:
            raise UserError(_('Не вдалося завантажити шаблон: %s') % e)

        context = {
            'contract_number': self.name,
            'contract_date': self.date.strftime('%d %B %Y') if self.date else '',
            'city': self.city,
            'seller_name': self.seller_name,
            'seller_representative': self.seller_representative,
            'buyer_name': self.buyer_name,
            'buyer_representative': self.buyer_representative,
            'vehicle_brand': self.vehicle_brand,
            'vehicle_model': self.vehicle_model,
            'vehicle_year': self.vehicle_year,
            'vehicle_color': self.vehicle_color,
            'vehicle_vin': self.vehicle_vin,
            'vehicle_reg': self.vehicle_reg,
            'total_price': self.total_price,
            'vat': self.vat,
            'items': [
                {
                    'item_no': 1,
                    'description': (
                            self.vehicle_brand + " " + self.vehicle_model).strip(),
                    'quantity': self.product_quantity,
                    'unit': 'шт.',
                    'price': "{:,.2f} грн".format(self.product_price) if self.product_price else '',
                },
            ],
            'seller_address': self.seller_address,
            'seller_account': self.seller_account,
            'seller_bank': self.seller_bank,
            'seller_mfo': self.seller_mfo,
            'seller_edrpou': self.seller_edrpou,
            'seller_phone': self.seller_phone,
            'seller_email': self.seller_email,
            'buyer_address': self.buyer_address,
            'buyer_account': self.buyer_account,
            'buyer_bank': self.buyer_bank,
            'buyer_mfo': self.buyer_mfo,
            'buyer_edrpou': self.buyer_edrpou,
            'buyer_phone': self.buyer_phone,
        }

        try:
            doc.render(context)
        except Exception as e:
            raise UserError(_('Помилка при заповненні шаблону: %s') % e)

        output_stream = io.BytesIO()
        doc.save(output_stream)
        output_stream.seek(0)
        return base64.b64encode(output_stream.read())

    def action_generate_docx(self):
        """
        Метод для вызова с кнопки "Завантажити DOCX".
        Генерирует и возвращает ссылку для скачивания документа.
        """

        self.ensure_one()
        try:
            file_data = self.generate_docx()
        except Exception as e:
            raise UserError(_('Помилка при генерації документа: %s') % e)

        attachment = self.env['ir.attachment'].create({
            'name': f'{self.name}.docx',
            'type': 'binary',
            'datas': file_data,
            'res_model': self._name,
            'res_id': self.id,
        })
        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/%s?download=true' % (attachment.id),
            'target': 'self',
        }

    def print_contract(self):
        """
        Метод для печати договора через alnas.
        Вызывает отчет для печати договора.
        """

        self.ensure_one()
        return self.env.ref('contract.action_print_contract').report_action(self)
