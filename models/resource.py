from odoo import models, fields, api


class Resource(models.Model):
    _name = 'dam.resource'
    _description = 'Digital Asset Management Resource'


    name = fields.Char(string='Name', required=True, help='Name of the resource')
    file = fields.Binary(string='File', required=True, help='File of the resource')
    type = fields.Selection([
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),
        ('document', 'Document'),
        ('other', 'Other')
    ], string='Type', required=True, help='Type of the resource')
    description = fields.Text(string='Description', help='Description of the resource')
    project_id = fields.Many2one('project.project', string='Project', help='Project the resource belongs to')