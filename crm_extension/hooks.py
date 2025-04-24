app_name = "crm_extension"
app_title = "CRM Extension"
app_publisher = "intent code"
app_description = "This Application Helps In Connecting TO CRM"
app_email = "mohammedanas18025@gmail.com"
app_license = "mit"

# Apps
# ------------------
after_install = "crm_extension.api.custom_fields.create_custom_fields"
before_uninstall = "crm_extension.api.custom_fields.delete_custom_fields"

required_apps = ["erpnext"]

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "crm_extension",
# 		"logo": "/assets/crm_extension/logo.png",
# 		"title": "CRM Extension",
# 		"route": "/crm_extension",
# 		"has_permission": "crm_extension.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/crm_extension/css/crm_extension.css"
# app_include_js = "/assets/crm_extension/js/crm_extension.js"

# include js, css files in header of web template
# web_include_css = "/assets/crm_extension/css/crm_extension.css"
# web_include_js = "/assets/crm_extension/js/crm_extension.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "crm_extension/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "crm_extension/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "crm_extension.utils.jinja_methods",
# 	"filters": "crm_extension.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "crm_extension.install.before_install"
# after_install = "crm_extension.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "crm_extension.uninstall.before_uninstall"
# after_uninstall = "crm_extension.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "crm_extension.utils.before_app_install"
# after_app_install = "crm_extension.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "crm_extension.utils.before_app_uninstall"
# after_app_uninstall = "crm_extension.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "crm_extension.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }
doc_events = {
    "Lead": {
        "after_insert": "crm_extension.api.lead_assign.assign_lead_to_group_users"
    }
}


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"crm_extension.tasks.all"
# 	],
# 	"daily": [
# 		"crm_extension.tasks.daily"
# 	],
# 	"hourly": [
# 		"crm_extension.tasks.hourly"
# 	],
# 	"weekly": [
# 		"crm_extension.tasks.weekly"
# 	],
# 	"monthly": [
# 		"crm_extension.tasks.monthly"
# 	],
# }

scheduler_events = {
    "cron": {
        "*/1 * * * *": [  
            "crm_extension.api.lead_connector.sync_leads_from_external_api"
        ]
    }
}


# Testing
# -------

# before_tests = "crm_extension.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "crm_extension.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "crm_extension.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["crm_extension.utils.before_request"]
# after_request = ["crm_extension.utils.after_request"]

# Job Events
# ----------
# before_job = ["crm_extension.utils.before_job"]
# after_job = ["crm_extension.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"crm_extension.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

