# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ClientQualification(models.Model):
#---------------------------------------------------------
# Client Qualifications Tab                              -
#---------------------------------------------------------
    __name = 'crm.qualification'
    _inherit = 'res.partner'
    client_qualification = fields.One2many('crm.lead', 'partner_id')