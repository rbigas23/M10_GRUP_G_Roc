# -*- coding: utf-8 -*-

from odoo import models, fields

class MedicalAppointment(models.Model):
    _name = 'medical.appointment'
    _description = 'Medical Appointment'

    name = fields.Char('Patient Name', required=True)
    appointment_date = fields.Datetime('Appointment Date', required=True)
    doctor_name = fields.Char('Doctor Name', required=True)
    reason = fields.Text('Reason for Appointment')
