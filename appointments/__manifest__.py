# -*- coding: utf-8 -*-
{
    'name': "Appointments",
    'summary': "Módulo de citas",
    'description': "Permite a los pacientes pedir citas en el hospital",
    'author': "HospitalTIC",
    'website': "http://www.hospitaltic.com",
    'category': 'Healthcare',
    'version': '1.0',
    'installable': True,
    'application': True,
    'auto_install': False,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/medical_appointment_views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
