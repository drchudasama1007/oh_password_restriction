# Copyright 2022 Odoo Helper
# See LICENSE file for full copyright and licensing details.
#
##############################################################################
{
    'name': "Website Password Restriction",
    'version': "13.0.1",
    'summary': """Website Password Restriction""",
    'description': """Website Password Restriction""",
    'author': "Odoo Helper",
    'license': 'AGPL-3',
    'category': 'website',
    'depends': ['website','auth_signup'],
    'data': [
        'views/assets.xml',
    ],
    'images': ['images/OdooHelper.jpg'],
    'price': 18.23,
    'currency': 'USD',
    'installable': True,
    'application': False
}
