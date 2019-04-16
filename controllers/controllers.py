# -*- coding: utf-8 -*-
from odoo import http

# class /opt/odoo/odooFuturo/moduloIngenieria(http.Controller):
#     @http.route('//opt/odoo/odoo_futuro/modulo_ingenieria//opt/odoo/odoo_futuro/modulo_ingenieria/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//opt/odoo/odoo_futuro/modulo_ingenieria//opt/odoo/odoo_futuro/modulo_ingenieria/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/opt/odoo/odoo_futuro/modulo_ingenieria.listing', {
#             'root': '//opt/odoo/odoo_futuro/modulo_ingenieria//opt/odoo/odoo_futuro/modulo_ingenieria',
#             'objects': http.request.env['/opt/odoo/odoo_futuro/modulo_ingenieria./opt/odoo/odoo_futuro/modulo_ingenieria'].search([]),
#         })

#     @http.route('//opt/odoo/odoo_futuro/modulo_ingenieria//opt/odoo/odoo_futuro/modulo_ingenieria/objects/<model("/opt/odoo/odoo_futuro/modulo_ingenieria./opt/odoo/odoo_futuro/modulo_ingenieria"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/opt/odoo/odoo_futuro/modulo_ingenieria.object', {
#             'object': obj
#         })