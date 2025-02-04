# -*- coding: utf-8 -*-
from addons.web.controllers.main import home as hom
from odoo import http
from odoo.http import serialize_exception, route


class Extension_Home(hom.Home):  # Inherit in your custom class

    @http.route(['/robots2.txt'], type='http', auth="none")
    def robots3(self, **kwargs):
        return "XXX User-agent: *\nDisallow: /\n"

    @http.route('/robots.txt', auth='public', type='http', methods=['POST'], csrf=False)
    def robots(self, **kwargs):
        # Aquí sobreescribes el método o lógica que deseas cambiar
        return 'Método sobrescrito con éxito'