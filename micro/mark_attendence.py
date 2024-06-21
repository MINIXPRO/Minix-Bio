import frappe
import re
import json
import traceback
import urllib
from urllib.request import urlopen
import requests
import datetime
import hrms
import time


import itertools
from datetime import datetime, timedelta
from hrms.hr.doctype.shift_type.shift_type import ShiftType
from frappe.model.document import Document
from frappe.utils import cint, get_datetime, get_time, getdate
from erpnext.setup.doctype.employee.employee import get_holiday_list_for_employee
from erpnext.setup.doctype.holiday_list.holiday_list import is_holiday
from hrms.hr.doctype.attendance.attendance import mark_attendance
from hrms.hr.doctype.employee_checkin.employee_checkin import (
	calculate_working_hours,
	mark_attendance_and_link_log,
)
from hrms.hr.doctype.shift_assignment.shift_assignment import get_employee_shift, get_shift_details
from hrms.utils import get_date_range
from hrms.utils.holiday_list import get_holiday_dates_between


@frappe.whitelist()
def dt():
	shift_list = frappe.db.get_list('Shift Type',ignore_permissions=True)
	for i in range(0,len(shift_list)):
		doc = frappe.get_doc('Shift Type',shift_list[i])
		doc.last_sync_of_checkin = datetime.now()
		frappe.db.commit()
		doc.save()

@frappe.whitelist()
def swarm():
	dt()
	doc1 = frappe.get_doc('Shift Type',"Shift- A1")
	doc2 = frappe.get_doc('Shift Type',"G Shift")
	doc3 = frappe.get_doc('Shift Type',"Shift - G1")
	ShiftType.process_auto_attendance(doc1)
	frappe.db.commit()
	doc1.save()
	ShiftType.process_auto_attendance(doc2)
	frappe.db.commit()
	doc2.save()
	ShiftType.process_auto_attendance(doc3)
	frappe.db.commit()
	doc3.save()
