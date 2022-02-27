# -*- coding: utf-8 -*-

from odoo import models, fields, api


class crm_qualification(models.Model):
    """ Darbtech CRM partner adaptations """

    _inherit = 'res.partner'

    leads_qualification = fields.One2many('crm.lead', 'partner_id')