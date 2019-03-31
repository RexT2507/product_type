# -*- coding: utf-8 -*-

from odoo import models, fields

# insertion de type produit pas les articles
class ProductTemplate(models.Model):
    _inherit = 'product.template'

# Sans les valeurs prédéfinies
# pb : si on utilise product.type dans la vue impossible de voir le module dans le menu
#    test = fields.Many2one(comodel_name='product.product.type',string='Type de produit')
#    fields.Selection(man,'Mes types de produits', required=True)

# Test avec des valeurs prédéfinies
    typeprod = fields.Many2one(comodel_name='typeproduct.typeproduct',string='Type de produit')


# Base créer avec scaffold
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
