# -*- coding: utf-8 -*-
from odoo import http

# class Ztest(http.Controller):
#     @http.route('/ztest/ztest/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ztest/ztest/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ztest.listing', {
#             'root': '/ztest/ztest',
#             'objects': http.request.env['ztest.ztest'].search([]),
#         })

#     @http.route('/ztest/ztest/objects/<model("ztest.ztest"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ztest.object', {
#             'object': obj
#         })