# -*- coding: utf-8 -*-

from odoo import models, fields, api

class crm_reminder(models.Model):
#---------------------------------------------------------
# Reminder date field                                    -
#---------------------------------------------------------
   _inherit = 'crm.lead'
   reminder_date = fields.Date()

