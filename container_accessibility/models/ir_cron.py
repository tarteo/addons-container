from odoo import _, api, models
from odoo.exceptions import AccessError


class IrCron(models.Model):
    _inherit = "ir.cron"

    def write(self, vals):
        res = super().write(vals)
        if (
            not self.env.context.get("auditlog_allow_crud", False) and
            self.env.ref("auditlog.model_auditlog_autovacuum") in self.mapped("model_id")
        ):
            raise AccessError(_("Access Denied"))
        return res

    @api.model_create_multi
    def create(self, vals_list):
        res = super().create(vals_list)
        if (
            not self.env.context.get("auditlog_allow_crud", False) and
            self.env.ref("auditlog.model_auditlog_autovacuum") in self.mapped("model_id")
        ):
            raise AccessError(_("Access Denied"))
        return res

    def unlink(self):
        if (
            not self.env.context.get("auditlog_allow_crud", False) and
            self.env.ref("auditlog.model_auditlog_autovacuum") in self.mapped("model_id")
        ):
            raise AccessError(_("Access Denied"))
        return super().unlink()

    def method_direct_trigger(self):
        return super(IrCron, self.with_context(auditlog_allow_crud=True)).method_direct_trigger()
