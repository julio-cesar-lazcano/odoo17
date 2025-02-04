from odoo import models, _
from odoo.exceptions import AccessDenied

ALLOWED_DOMAIN = "tutum.com,mx"  # Cambia esto por el dominio permitido

class RestrictLogin(models.Model):
    _inherit = "res.users"

    @classmethod
    def _login(cls, db, login, password, user_agent_env):
        """Reescribe la autenticación para validar el dominio del email"""
        if "@" in login:
            domain = login.split("@")[-1]
            if domain != ALLOWED_DOMAIN:
                raise AccessDenied(_("Solo los correos de @%s pueden acceder." % ALLOWED_DOMAIN))

        return super()._login(db, login, password, user_agent_env)