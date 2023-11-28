# Copyright 2023 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Services Based Organization - Install',
    'description': 'Services Based Organization - Install',
    'category': 'Technical Settings',
    'version': '16.0.1.0.0',
    'author': 'Onestein',
    'website': 'https://www.onestein.nl',
    'license': 'AGPL-3',
    'depends': [
        'account_configuration',
        'container_install_standard',

        # Base
        'account',
        'account_edi',
        'account_edi_ubl_cii',
        'account_payment',
        #'sale_timesheet',
        'account_qr_code_sepa',
        'analytic',
        'attachment_indexation',
        'auth_signup',
        'auth_totp',
        'auth_totp_mail',
        'auth_totp_portal',
        'barcodes',
        'base_address_extended',
        'base_automation',
        'base_geolocalize',
        'base_iban',
        'base_import',
        'base_setup',
        'base_vat',
        'board',
        'calendar',
        'calendar_sms',
        'contacts',
        'contract',
        'contract_payment_mode',
        'crm',
        'crm_sms',
        'google_recaptcha',
        'helpdesk_mgmt',
        'helpdesk_mgmt_project',
        'hr',
        'hr_contract',
        'hr_expense',
        'hr_holidays',
        'hr_org_chart',
        'hr_timesheet',
        'http_routing',
        'l10n_multilang',
        'l10n_nl',
        'link_tracker',
        'mail',
        'mail_bot',
        'mail_bot_hr',
        'mass_mailing',
        'mass_mailing_crm',
        'mass_mailing_sale',
        'mis_builder',
        'mis_builder_budget',
        'payment',
        'payment_custom',
        'phone_validation',
        'portal',
        'portal_rating',
        'product',
        'product_margin',
        'project',
        'project_timesheet_holidays',
        'project_hr_expense',
        'project_purchase',
        'purchase',
        'purchase_stock',
        'rating',
        #'report_xlsx',
        'resource',
        'sale',
        'sale_loyalty',
        'sale_crm',
        'sale_expense',
        'sale_management',
        'sale_project',
        'sale_purchase',
        'sale_purchase_stock',
        'sale_sms',
        'sale_stock',
        'sales_team',
        'sale_timesheet',
        'sms',
        'snailmail',
        'snailmail_account',
        'social_media',
        'stock',
        'stock_sms',
        'uom',
        'utm',
        'web_editor',
        'web_kanban_gauge',
        'web_tour',
        'web_unsplash',
        'website',
        'website_blog',
        'website_crm',
        'website_crm_partner_assign',
        'website_crm_sms',
        'website_customer',
        'website_google_map',
        'website_mail',
        'website_mass_mailing',
        'website_partner',
        'website_payment',
        'website_sale',
        'website_sale_loyalty',
        'website_sale_stock',
        'website_sms',

        # Community
        "account_invoice_overdue_reminder",
        'account_reconcile_oca',
        'account_usability',
        'account_financial_report',
        'account_asset_management',
        'account_spread_cost_revenue',
        'account_banking_sepa_credit_transfer',
        'account_banking_sepa_direct_debit',
        'account_fiscal_position_vat_check',
        'account_invoice_constraint_chronology',
        'account_journal_lock_date',
        'account_lock_date_update',
        'account_move_line_purchase_info',
        'account_move_line_sale_info',
        'account_move_line_tax_editable',
        'account_move_print',
        'base_vat_optional_vies',
        'account_move_tier_validation',
        'account_statement_import_online_paypal',
        'website_analytics_matomo',
        'account_statement_import_file_reconcile_oca',
        'account_statement_import_camt',
        'account_statement_import_online',
        'account_statement_import_online_ponto',
        'auditlog',
        'project_role',
        'currency_rate_update',
        'date_range',
        'disable_odoo_online',
        'hr_timesheet_sheet',
        'l10n_nl_bank',
        'l10n_nl_bsn',
        'l10n_nl_postcode',
        'l10n_nl_tax_statement',
        'l10n_nl_tax_statement_date_range',
        'l10n_nl_tax_statement_icp',
        'l10n_nl_xaf_auditfile_export',
        'mail_tracking',
        'mass_mailing_partner',
        'partner_external_map',
        'project_timeline',
        'report_qr',
        'report_qweb_parameter',
        'report_wkhtmltopdf_param',
        'report_xlsx',
        'report_xlsx_helper',
        'remove_odoo_enterprise',
        'web_responsive',
        'web_no_bubble',
        'web_search_with_and',
        'web_widget_x2many_2d_matrix',
        'web_timeline',
        'website_odoo_debranding',
        'hr_expense_remove_mobile_link',

        # Onestein
        'mass_mailing_help',

        # 3rd-Party
        'mollie_account_sync',
        'mollie_subscription_ept',
        'payment_mollie_official',
        'l10n_nl_rgs',
        'l10n_nl_rgs_account_financial_report',
        'l10n_nl_rgs_asset',
        'l10n_nl_rgs_mis_report',
        #'nextcloud_odoo_sync',
    ],
    'data': [],
}
