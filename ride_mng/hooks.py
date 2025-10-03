app_name = "ride_mng"
app_title = "Ride Management"
app_publisher = "Prashant K"
app_description = "Ride Management"
app_email = "kambleprashant@outlook.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "ride_mng",
# 		"logo": "/assets/ride_mng/logo.png",
# 		"title": "Ride Management",
# 		"route": "/ride_mng",
# 		"has_permission": "ride_mng.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ride_mng/css/ride_mng.css"
# app_include_js = "/assets/ride_mng/js/ride_mng.js"

# include js, css files in header of web template
# web_include_css = "/assets/ride_mng/css/ride_mng.css"
# web_include_js = "/assets/ride_mng/js/ride_mng.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ride_mng/public/scss/website"

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
# app_include_icons = "ride_mng/public/icons.svg"

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
# 	"methods": "ride_mng.utils.jinja_methods",
# 	"filters": "ride_mng.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "ride_mng.install.before_install"
# after_install = "ride_mng.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ride_mng.uninstall.before_uninstall"
# after_uninstall = "ride_mng.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "ride_mng.utils.before_app_install"
# after_app_install = "ride_mng.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "ride_mng.utils.before_app_uninstall"
# after_app_uninstall = "ride_mng.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ride_mng.notifications.get_notification_config"

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

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ride_mng.tasks.all"
# 	],
# 	"daily": [
# 		"ride_mng.tasks.daily"
# 	],
# 	"hourly": [
# 		"ride_mng.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ride_mng.tasks.weekly"
# 	],
# 	"monthly": [
# 		"ride_mng.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "ride_mng.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ride_mng.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "ride_mng.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["ride_mng.utils.before_request"]
# after_request = ["ride_mng.utils.after_request"]

# Job Events
# ----------
# before_job = ["ride_mng.utils.before_job"]
# after_job = ["ride_mng.utils.after_job"]

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
# 	"ride_mng.auth.validate"
# ]
fixtures = [
	{"dt": "Item", "filters": [["item_group", "=", "Services"]]},
	{"dt": "Customer", "filters": [["customer_group", "=", "Commercial"]]},
	{"dt": "Vehicle Ride"},
	{"dt": "Ride Booking"},
]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }
