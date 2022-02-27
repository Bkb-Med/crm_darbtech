

from odoo import  api , models
from datetime import date
class Users(models.Model):
    _inherit = ['res.users']

    @api.model
    def getLeads(self):
        
        query = """SELECT t.id AS id , t.reminder_date AS reminder
                    FROM crm_lead AS t
                    WHERE t.type='lead' and t.reminder_date IS NOT NULL
                    """

        self._cr.execute(query)
        leads = self._cr.dictfetchall()
        today = date.today()
        _leads_counter = {
                 'name': 'CRM Qualifications',
                 'model': 'crm.lead',
                 'total': len(leads),
                 'today': len([d for d in leads if d['reminder'] == today]),
                 'outdated': len([d for d in leads if d['reminder'] < today]),
                 'upcoming': len([d for d in leads if d['reminder'] > today])
                }
        return _leads_counter
