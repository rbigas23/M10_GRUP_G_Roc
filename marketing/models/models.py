# -*- coding: utf-8 -*-
from odoo import models, fields


class MarketingCampaign(models.Model):
    _name = 'marketing.campaign'
    _description = 'Marketing Campaign'

    name = fields.Char('Name', required=True)
    email_template_id = fields.Many2one('mail.template', 'Email Template')

class MarketingEmail(models.Model):
    _name = 'marketing.email'
    _description = 'Marketing Email'

    name = fields.Char('Subject', required=True)
    recipient_ids = fields.Many2many('res.partner', string='Recipients')
    campaign_id = fields.Many2one('marketing.campaign', 'Campaign')
    state = fields.Selection([('draft', 'Draft'), ('sent', 'Sent')], default='draft')

    def send_email(self):
        self.write({'state': 'sent'})
        