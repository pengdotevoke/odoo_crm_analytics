from odoo import api, fields, models

class OdooCrmAnalytics(models.Model):
    _name = 'crm.dashboard'
    _description = 'Odoo CRM Analytics'
    _inherit=['mail','mail.thread', 'mail.mixin']


    name = fields.Char(string='Name', required=True, tracking=True)