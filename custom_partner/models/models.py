from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    autipe = fields.Selection([('type1', 'Type 1'), ('type2', 'Type 2'), ], string='Type', default='type1')

    def action_copy_phone_to_mobile(self):
        for record in self:
            if record.phone and not record.mobile:
                record.write({'mobile': record.phone})


class custom_partner(models.Model):
    _name = 'custom_partner.custom_partner'
    _description = 'custom_partner.custom_partner'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
