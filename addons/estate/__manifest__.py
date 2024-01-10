{
    'name': 'Estate Module',
    'version': '1.0',
    'summary': 'Real Estate Module',
    'sequence': 10,
    'description': 'Manage Real Estate Properties',
    'category': 'Property Management',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_menus.xml',
         ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
 
