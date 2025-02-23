{
    'name': 'Договір',
    'version': '1.0',
    'summary': 'Модуль для создания и печати договоров',
    'description': 'Модуль реализует модель "Договор" с интеграцией печати через alnas.',
    'category': 'Contract',
    'author': 'Max',
    'assets': {
        'web.assets_backend': [
            'contract/static/src/css/custom.css',
        ],
    },
    'depends': ['base', 'alnas_docx'],
    'data': [
        'security/ir.model.access.csv',
        'views/contract_view.xml',
        'views/menu.xml',
        'views/inherit_print_button.xml',
        'static/templates/contract_report.xml',

    ],
    'installable': True,
    'application': True,
}
