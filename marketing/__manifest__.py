# -*- coding: utf-8 -*-
{
    'name': "Marketing",
    'summary': "Módulo de marketing",
    'description': "Este es el módulo de marketing.",
    'author': "HospitalTIC",
    'website': "http://www.hospitaltic.com",
    'category': 'Marketing',
    'version': '1.0',
    'installable': True,
    'application': True,
    'auto_install': False,
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/marketing_menu_views.xml',
        'views/marketing_campaign_views.xml',
        'views/marketing_email_views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
