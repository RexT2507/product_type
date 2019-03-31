# -*- coding: utf-8 -*-
from odoo import http

# class ProductType(http.Controller):
#     @http.route('/product_type/product_type/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_type/product_type/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_type.listing', {
#             'root': '/product_type/product_type',
#             'objects': http.request.env['product_type.product_type'].search([]),
#         })

#     @http.route('/product_type/product_type/objects/<model("product_type.product_type"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_type.object', {
#             'object': obj
#         })