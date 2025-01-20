from odoo import models, fields, api
from mimetypes import guess_type 


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
    is_image = fields.Boolean(string='Is Image', compute='_compute_is_image', store=True)

    @api.depends('type')
    def _compute_is_image(self):
        for record in self:
            record.is_image = record.type == 'image'
                    
