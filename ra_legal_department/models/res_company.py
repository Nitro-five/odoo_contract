from odoo import models, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    def action_open_new_protocol_form(self):
        """Открывает форму для создания нового Протокола."""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Новий Протокол',
            'res_model': 'ra_legal_department.document',
            'view_mode': 'form',
            'view_id': self.env.ref('ra_legal_department.internal_document_protocol').id,
            'context': {
                'default_type_of_internal_document': 'protocol',
                'default_type_of_document': 'internal',
            },
            'target': 'new',
        }

    def action_open_new_order_form(self):
        """Открывает форму для создания нового Приказа."""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Новий Наказ',
            'res_model': 'ra_legal_department.document',
            'view_mode': 'form',
            'view_id': self.env.ref('ra_legal_department.internal_document_protocol').id,  # Замените module_name и view_order_form
            'context': {
                'default_type': 'protocol',
                'default_type_of_internal_document': 'order',
            },
            'target': 'new',
        }
