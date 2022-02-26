# -*- coding: utf-8 -*-
from odoo import http

# class CrmDarbtech(http.Controller):
#     @http.route('/crm_darbtech/crm_darbtech/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crm_darbtech/crm_darbtech/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm_darbtech.listing', {
#             'root': '/crm_darbtech/crm_darbtech',
#             'objects': http.request.env['crm_darbtech.crm_darbtech'].search([]),
#         })

#     @http.route('/crm_darbtech/crm_darbtech/objects/<model("crm_darbtech.crm_darbtech"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm_darbtech.object', {
#             'object': obj
#         })