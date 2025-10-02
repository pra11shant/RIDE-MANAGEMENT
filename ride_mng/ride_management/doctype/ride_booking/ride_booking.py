# Copyright (c) 2025, Prashant K and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RideBooking(Document):
	def validate(self):
		total_amount = 0
		if self.vehicle:
			for row in self.services:
				if row.amount:
					total_amount += row.amount

			self.total_amount = (self.estimated_km * self.price_per_km) + total_amount
