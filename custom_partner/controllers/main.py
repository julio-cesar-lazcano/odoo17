from odoo import http
from odoo.http import request


class CustomRobotsController(http.Controller):

    @http.route('/robots.txt', type='http', auth="public")
    def robots_txt(self, **kwargs):
        custom_content = """
        User-agent: *
        Disallow: /private
        Allow: /

        Sitemap: {}/sitemap.xml
        """.format(request.httprequest.host_url)

        return request.make_response(custom_content, [('Content-Type', 'text/plain')])
