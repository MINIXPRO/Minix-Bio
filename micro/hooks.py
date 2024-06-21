

from . import __version__ as app_version

app_name = "micro"
app_title = "Minix"
app_publisher = "Nikhil"
app_description = "Minix Biometric Integration"
app_email = "-"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/micro/css/micro.css"
# app_include_js = "/assets/micro/js/micro.js"

# include js, css files in header of web template
# web_include_css = "/assets/micro/css/micro.css"
# web_include_js = "/assets/micro/js/micro.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "micro/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    			"Biometric Integration" : "public/api.js",
				"Purchase Invoice" : "public/js/purchase_invoice.js"
               
			   }
doctype_list_js = {
    "Asset" : "public/js/list/asset.js"
}
# doctype_js = {"Biometric Integration" : "public/js/biometric.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
doctype_calendar_js = {"Attendance" : "public/attendance_calander.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "micro.utils.jinja_methods",
#	"filters": "micro.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "micro.install.before_install"
# after_install = "micro.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "micro.uninstall.before_uninstall"
# after_uninstall = "micro.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "micro.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways
calendars = ["Total Calander"]
# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Purchase Invoice": "micro.micro.overrides.purchase_invoice.CustomPurchaseInvoice"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"Biometric Integration": {
# 		"on_update": "micro.api.generate",
# # # 		# "on_cancel": "method",
# # # 		# "on_trash": "method"
# 	}
# }
# doc_events = {
# 	"Attendance": {
# 		"before_save":"micro.query.attendance_duration"
# 	}
# }
doc_events = {
	"Leave Application": {
		"on_update":"micro.leave.leave_application"
	},
    "Supplier": {
		"before_save": "micro.micro.overrides.supplier.before_save",
	}
	# "Attendance": {
	# 	"before_save":"micro.query.attendance_duration"
	# }
}

# Scheduled Tasks
# ---------------

scheduler_events = {
#	"all": [
#		"micro.tasks.all"
	# ],
	# "daily": [
	# 	"micro.api.generate"
	# ],
	"hourly": [
		"micro.api.generate"
	],
#	"weekly": [
#		"micro.tasks.weekly"
#	],
#	"monthly": [
#		"micro.tasks.monthly"
#	],
	"cron": {
		"30 5 * * *": [
			"micro.mark_attendence.swarm",
		],
		}

}

# Testing
# -------

# before_tests = "micro.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "micro.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "micro.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["micro.utils.before_request"]
# after_request = ["micro.utils.after_request"]

# Job Events
# ----------
# before_job = ["micro.utils.before_job"]
# after_job = ["micro.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"micro.auth.validate"
# ]

fixtures = [
    {"dt": "Property Setter", "filters": [["module", "in", [app_title]]]},
    {"dt": "Custom Field", "filters": [["module", "=", app_title]]},
]