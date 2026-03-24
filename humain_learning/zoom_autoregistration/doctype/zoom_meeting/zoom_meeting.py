# Copyright (c) 2026, Raghav Kaul and contributors
# For license information, please see license.txt

from frappe.model.document import Document
import frappe
from humain_learning.zoom_autoregistration.api import fetch_webinar
class ZoomMeeting(Document):
	
	def validate(self):
		if not self.id:
			frappe.throw("Webinar ID is required.")

	def on_save(self):
		res = fetch_webinar(self.id)
		self.topic = res.get("topic")
		self.start_time = res.get("start_time")
		self.created_at = res.get("created_at")
		self.host_email = res.get("host_email")