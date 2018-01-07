# -*- coding: utf-8 -*-
# Copyright (c) 2018, taher and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import today,getdate
from datetime import datetime, timedelta, date   
from frappe.utils import cint, flt

class Membershippackage(Document):
	def validate(self):
		package = self.package_name
		cost = self.package_cost
		# income_account =self.income_account
		# selling_cost_center= self.selling_cost_center
		# frappe.errprint("in py")
		item_doctype = frappe.db.sql("select name from tabItem", as_list=1)
		i_d = [x[0] for x in item_doctype]
		# frappe.errprint(i_d)
		if not package in i_d:
			# frappe.errprint("creating new package item") 
			it = frappe.new_doc("Item")
			it.item_code = package
			it.item_group = "Packages"
			it.standard_rate = cost
			it.is_stock_item =0
			# it.income_account = income_account
			# it.selling_cost_center = selling_cost_center
			it.insert(ignore_permissions=True)
			it.save()

def package_buy(doc, method):
	customer = doc.customer
	tday= today()
	flag =False
	pacakage_list =frappe.db.sql("select package_name from `tabMembership package`",as_list=1)
	pl= [x[0] for x in pacakage_list]
	for p in doc.get("items"):
		if p.item_code in pl:
			mem = frappe.get_doc("Membership package", p.item_code)
			if mem.is_enabled:
				flag=True
				cv = frappe.new_doc("Customer validity")
				cv.customer =customer
				cv.package = p.item_code
				cv.valid_from = datetime.strptime(tday, "%Y-%m-%d")
				cv.valid_to = cv.valid_from + timedelta(days = mem.validity)
				cv.insert(ignore_permissions=True)
				cv.save()