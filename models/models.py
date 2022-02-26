# -*- coding: utf-8 -*-

from odoo import models, fields, api

class crm_darbtech(models.Model):
#     Reminder Form Adjustement
   _inherit = 'crm.lead'
   reminder_date = fields.Date()