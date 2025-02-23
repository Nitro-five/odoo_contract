{
    "name": "My Legal Department",
    "version": "15.0",
    "depends": ['base', 'mail', 'alnas_docx'],
    "data": [
        'security/ir.model.access.csv',
        'data/report_consultation.xml',
        # 'data/mail_template.xml',
        'views/legal_dispute.xml',
        'views/consultation.xml',
        'views/examination.xml',
        'views/document_legal_order.xml',
        'views/document_protocol.xml',
        'views/contract.xml',
        'views/documents.xml',
        'views/menu_item_legal_department.xml',

    ],

    "application": True,
    "installable": True,
}
