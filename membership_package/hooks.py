# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "membership_package"
app_title = "Membership Package"
app_publisher = "taher"
app_description = "packages for membership "
app_icon = "octicon octicon-file-directory"
app_color = "green"
app_email = "taherkhalil52@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/membership_package/css/membership_package.css"
# app_include_js = "/assets/membership_package/js/membership_package.js"

# include js, css files in header of web template
# web_include_css = "/assets/membership_package/css/membership_package.css"
# web_include_js = "/assets/membership_package/js/membership_package.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "membership_package.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "membership_package.install.before_install"
# after_install = "membership_package.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "membership_package.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	# "*": {
	# 	"on_update": "method",
	# 	"on_cancel": "method",
	# 	"on_trash": "method"
	# }
	"Sales Invoice" : {
		"on_submit": "membership_package.membership_package.doctype.membership_package.membership_package.package_buy"
	}
}
# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"membership_package.tasks.all"
# 	],
# 	"daily": [
# 		"membership_package.tasks.daily"
# 	],
# 	"hourly": [
# 		"membership_package.tasks.hourly"
# 	],
# 	"weekly": [
# 		"membership_package.tasks.weekly"
# 	]
# 	"monthly": [
# 		"membership_package.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "membership_package.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "membership_package.event.get_events"
# }

