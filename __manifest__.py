# -*- coding: utf-8 -*-
{
    'name': "Clinic Management System",

    'summary': """""",

    'description': """ Afghanistan Clinic Management System""",

    'author': "Rahmatullah Nazary",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Health',
    'version': '',
    'installable':True,
    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
            'views/hospital_menu.xml',
            'views/reception.xml',
            'views/doctor.xml',
            'views/patient.xml',
            'views/staff.xml',
            'reports/patient_reports.xml',
            'reports/staff_reports.xml',
            'reports/doctor_reports.xml',
            'views/wizard.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
