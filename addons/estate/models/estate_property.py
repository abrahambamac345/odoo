# archivo: estate_property.py dentro de tu directorio models/

from odoo import models, fields

class EstateProperty(models.Model):
    _name = 'estate.property'  # Nombre técnico del modelo, debe ser único
    _description = 'Estate Property'  # Descripción del modelo para la interfaz de usuario

    # Aquí se definen los campos del modelo
    name = fields.Char("Property Name", required=True)  # Un campo de texto, marcado como requerido
    description = fields.Text("Description")  # Un campo de texto largo para descripciones
    postcode = fields.Char("Postcode")  # Un campo de texto para el código postal
    date_availability = fields.Date("Availability Date")  # Un campo de fecha para la disponibilidad
    expected_price = fields.Float("Expected Price", digits=(16, 2),required=True)  # Un campo flotante para el precio esperado
    selling_price = fields.Float("Selling Price", digits=(16, 2))  # Un campo flotante para el precio de venta
    bedrooms = fields.Integer("Bedrooms")  # Un campo entero para el número de habitaciones
    living_area = fields.Integer("Living Area (sqm)")  # Un campo entero para el área habitable
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer("Garden Area")
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ], "Garden Orientation")

    # ... y así sucesivamente para otros campos que quieras añadir

    # También puedes añadir métodos para lógica de negocio específica
    def some_method(self):
        # Código del método aquí
        pass
