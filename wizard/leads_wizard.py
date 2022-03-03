# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CreateNewLeadWizard(models.TransientModel):
#----------------------------------------------------------------
# Wizard form (two section)                                     -
#----------------------------------------------------------------
    _name = 'crm.create.newlead.wizard'
    
    state = fields.Selection([('init', 'Initial'), ('final', 'Final')],
                             default='init')
    name = fields.Char('Opportunity', required=True, index=True)
    partner_id = fields.Many2one('res.partner', string='Customer', track_visibility='onchange', track_sequence=1, index=True)
    partner_name = fields.Char(string='Company name',track_visibility='onchange', track_sequence=1, index=True)
    team_id = fields.Many2one('crm.team', string='Sales Team', oldname='section_id', index=True, track_visibility='onchange')
    user_id = fields.Many2one('res.users', string='Salesperson', index=True, track_visibility='onchange')

    reminder_date = fields.Date()


    @api.multi
    def previous(self):
        self.ensure_one()
        self.state = 'init'
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': self._name,
            'res_id': self[0].id,
            'target': 'new'
        }

    @api.multi
    def next(self):
        self.ensure_one()
        self.state = 'final'
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': self._name,
            'res_id': self[0].id,
            'target': 'new'
        }

    @api.multi
    def create_lead(self):
        self.ensure_one()
        values = self.get_values()
        values.update({'type': 'lead'})
        self.env['crm.lead'].create(values)

    def get_values(self):
        self.ensure_one()
        return {
            'name': self.name,
            'partner_id': self.partner_id.id,
            'partner_name': self.partner_id.company_name,
            'user_id': self.user_id.id,
            'team_id': self.team_id.id,
            'contact_name': self.partner_id.name,
            'title': self.partner_id.title.id,     
            'reminder_date': self.reminder_date

        }
