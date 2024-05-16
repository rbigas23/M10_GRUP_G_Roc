# -*- coding: utf-8 -*-
{
    'name': "Marketing",

    'summary': "Módulo de marketing",

    'description': "Este es el módulo de marketing.",

    'author': "HospitalTIC",
    'website': "http://www.hospitaltic.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Marketing',
    'version': '1.0',

    'installable': True,
    'application': True,
    'auto_install': False,

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/marketing_menu_views.xml',
        'views/marketing_campaign_views.xml',
        'views/marketing_email_views.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
