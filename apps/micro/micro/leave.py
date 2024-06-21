import frappe
import re
import json
import traceback
import urllib
from urllib.request import urlopen
import requests
import datetime
import pandas as pd
from datetime import date
from datetime import datetime


@frappe.whitelist()
def leave_application(self,method):
	doc = frappe.get_doc('Developer Settings','Datalist')
	today = date.today()
	posting_date  = pd.to_datetime(self.posting_date).date()
	frm_date  = pd.to_datetime(self.from_date).date()
	leave_appilcation_date  = pd.to_datetime(doc.leave_appilcation_date).date()
	if today <= doc.leave_appilcation_date:
		pass
	elif today > doc.leave_appilcation_date:
		if posting_date > doc.leave_appilcation_date:
			if frm_date < doc.leave_appilcation_date:
				frappe.throw("Leave application date has passed,leave application is not possible,please contact HR")
