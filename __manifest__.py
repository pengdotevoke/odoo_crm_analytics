{
    'name':'Odoo CRM Analytics',
    'author':'James Oginga',
    'depends':['crm','mail'],
    'version':'1.0',
    'description':'This module provides CRM analytics tools',
    'data':[
        'security/ir.model.access.csv',
        'views/crm_dashboard_view.xml',
        'views/menu.xml'
        ],
    'license':'LGPL-3',
    'category':'Sales & Marketing',
    'installable':True,
    'auto_install':False,
    'application':True,

}