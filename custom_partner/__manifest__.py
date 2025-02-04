# -*- coding: utf-8 -*-
{
    'name': "Modulo Personalizado",

    'summary': "Modulo Personalizado Optimizado para Odoo17",

    'description': """
En este modulo se creo con scaffold para windows, integra Vistas, modelos, herencias, accones de servidor y segudidad.
    """,

    'author': "Julio Cesar Lazcano Cruz",
    'website': "https://www.juliocesarlazcanocruz.com",

    'category': 'Demo',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'auth_signup'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/inherited.xml',
        'views/action_server.xml',
    ],

}

