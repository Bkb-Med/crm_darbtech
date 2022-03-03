# -*- coding: utf-8 -*-
{
    'name': "CRM Qualification [Darbtech_test]",

    'summary': """
       CRM Qualification extensions _Darbtech test
       """,

    'description': """
        
        CRM extensions 
       Adj1: Autocomplete field
       Adj2: Reminder Date
       Adj3: Notification (Qualifications)
       Adj4: Qualifications
       Adj5: Wizard 
    """,

    'author': "Boukbab M'hamed",
    'website': "http://www.boukbab.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'CRM',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','crm'],
    
    # always loaded
    'data': [
        #security
        'security/ir.model.access.csv',
        #wizard
        'wizard/leads_template_wizard.xml',
        #views
        'views/crm_reminder_autocomplete.xml',
        'views/crm_systray_templates.xml',
        'views/crm_qualification.xml',
        'views/crm_action_leads_wizard.xml',
        
        
    ],
    # only loaded in demonstration mode
    "qweb": [
      "static/xml/systray.xml",
        ],
    
}