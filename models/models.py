# -*- coding: utf-8 -*-

from odoo import models, fields

# insertion de type produit pas les articles
class ProductTemplate(models.Model):
    _inherit = 'product.template'

    typeprod = fields.Many2one(comodel_name='typeproduct.typeproduct',string='Type de produit')
