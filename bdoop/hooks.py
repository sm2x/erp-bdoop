# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "bdoop"
app_title = "Bdoop"
app_publisher = "vinhbk2000"
app_description = "Script for bdoop Company"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "vinhbk2000@gmail.com"
app_license = "MIT"

doctype_js = {
    "Journal Entry": "custom_scripts/journal_entry_custom.js",
    "Payment Entry": "custom_scripts/payment_entry_custom.js",
    "Purchase Invoice": "custom_scripts/purchase_invoice_custom.js",
    "Sales Order": "custom_scripts/sales_order_custom.js",
    "Item": "custom_scripts/item_custom.js"
}

fixtures = [
     {
	    "doctype": "DocType",
        "filters": { "custom" : ["=", "1"] }
    }, 
    "Custom Field",
    "Custom Script",
    "Property Setter",
    "Print Format"
]

website_context = {
	"favicon": 	"/assets/bdtheme/images/bp-ico-32.png",
	"splash_image": "/assets/bdtheme/images/logo_bdoop.png"
}

email_brand_image = "assets/bdtheme/images/logo_bdoop.png"

default_mail_footer = """
	<span>
		Sent via
		<a class="text-muted" href="https://bdoop.com" target="_blank">
			Bdoop Erp
		</a>
	</span>
"""

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/bdoop/css/bdoop.css"
# app_include_js = "/assets/bdoop/js/bdoop.js"

# include js, css files in header of web template
# web_include_css = "/assets/bdoop/css/bdoop.css"
# web_include_js = "/assets/bdoop/js/bdoop.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "bdoop.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "bdoop.install.before_install"
# after_install = "bdoop.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "bdoop.notifications.get_notification_config"

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

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"bdoop.tasks.all"
# 	],
# 	"daily": [
# 		"bdoop.tasks.daily"
# 	],
# 	"hourly": [
# 		"bdoop.tasks.hourly"
# 	],
# 	"weekly": [
# 		"bdoop.tasks.weekly"
# 	]
# 	"monthly": [
# 		"bdoop.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "bdoop.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "bdoop.event.get_events"
# }

