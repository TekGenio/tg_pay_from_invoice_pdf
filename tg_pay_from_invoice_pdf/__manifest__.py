{
    'name': "Tekgenio Pay From Invoice",
    'version': '17.0.0.1',
    'description': '''
       Adding option to pay from Invoice Pdf 
    ''',
    'author': "TekGenio",
    'website': "https://tekgenio.com",
    'images': ['static/description/banner.png'],
    'currency':'USD',
    'price':10,
    'depends': ['base', 'contacts','account'],
    'data': [
        'views/account_move.xml',
        'views/invoice_report.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    

}
