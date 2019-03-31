# -*- coding: utf-8 -*-

from odoo import models, fields

# Sans les valeurs prédéfinies
class ProductProductType(models.Model):
    _name= 'product.type'

    name = fields.Char(name='Type de produit', translate=True)



# insertion de type produit pas les articles
class ProductTemplate(models.Model):
    _inherit = 'product.template'

# Sans les valeurs prédéfinies
# pb : si on utilise product.type dans la vue impossible de voir le module dans le menu
#    test = fields.Many2one(comodel_name='product.product.type',string='Type de produit')

# Test avec des valeurs prédéfinies
    typeprod = fields.Selection([('s','Sucré'),('ts','Très sucrée'), ('S','Salée'),('tS','Très salée'),('a','Alcool'),
                        ('m','Mortel !!')],'Mes types de produits', required=True)


# Base créer avec scaffold
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
