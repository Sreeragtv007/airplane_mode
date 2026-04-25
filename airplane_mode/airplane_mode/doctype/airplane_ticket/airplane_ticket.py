# Copyright (c) 2026, sreerag and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class AirplaneTicket(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		departure_date: DF.Date
		departure_time: DF.Time | None
		destination_airport: DF.Link
		destination_airport_code: DF.Link
		duration_of_flight: DF.Duration
		flight: DF.Link
		passenger: DF.Link
		source_airport: DF.Link
		source_airport_code: DF.Link
	# end: auto-generated types

	pass
