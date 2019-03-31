from odoo import models, fields

class TypeProduct(models.Model):
    _name = "typeproduct.typeproduct"

    name = fields.Char(string='Name', require=True)