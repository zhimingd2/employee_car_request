# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CarRequest(models.Model):
    _name = "car.request" #Table in DB
    _inherit = ['mail.thread']
    _description = "Car Request"

    name = fields.Char(string="Request", request=True)
    date_from = fields.Datetime(string="Staring Date", default=fields.Datetime.now())
    date_to = fields.Datetime(string="End Date", required=False)

    employee_id = fields.Many2one(comodel_name="hr.employee", string="Employee", required=True)
    car_id= fields.Many2one(comodel_name="fleet.vehicle", string="Car", required=True)

    state = fields.Selection(string="Status", selection=[('draft','Draft'),('confirm','Confirm'),('validate','Validated'),
                            ('refuse','Refulse'),('approved','Approved')],default="draft", track_visibility='onchange')

    @api.multi
    def confirm_request(self):
        self.state = 'confirm'

    @api.multi
    def validate_request(self):
        self.state = 'validate'

    @api.multi
    def refuse_request(self):
        self.state = 'refuse'

    @api.multi
    def approve_request(self):
        self.state = 'approved'

