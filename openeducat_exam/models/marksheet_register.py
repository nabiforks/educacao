# -*- coding: utf-8 -*-
###############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech-Receptives(<http://www.techreceptives.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openerp import models, fields, api, _
from openerp.exceptions import ValidationError


class OpMarksheetRegister(models.Model):
    _name = 'op.marksheet.register'

    exam_session_id = fields.Many2one(
        'op.exam.session', 'Exam', required=True)
    marksheet_line = fields.One2many(
        'op.marksheet.line', 'marksheet_reg_id', 'Marksheets')
    generated_date = fields.Date(
        'Generated Date', required=True, default=fields.Date.today())
    generated_by = fields.Many2one(
        'res.users', 'Generated By',
        default=lambda self: self.env.uid, required=True)
    status = fields.Selection(
        [('draft', 'Draft'), ('validated', 'Validated'),
         ('cancelled', 'Cancelled')], 'Status', default="draft", required=True)
    total_pass = fields.Float('Total Pass')
    total_failed = fields.Float('Total Fail')
    name = fields.Char('Marksheet Register', size=256, required=True)

    @api.constrains('total_pass', 'total_failed')
    def _check_marks(self):
        if (self.total_pass < 0.0) or (self.total_failed < 0.0):
            raise ValidationError(_('Enter proper pass or fail!'))
