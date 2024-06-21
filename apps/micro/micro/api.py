

import frappe
import re
import json
import traceback
import urllib
from urllib.request import urlopen
import requests
import datetime


@frappe.whitelist()
def generate():
    doct = frappe.get_doc('Biometric Integration','Microcrispr')
    data = doct.url.format(frappe.utils.get_url())
    s = doct.from_date
    url = data + "&frm=" + str(s)
    headerInfo = {'content-type': 'application/json'}
    r = requests.get(url, headers=headerInfo)
    req = json.loads(r.text)
    reqs = json.loads(req)
    le = len(reqs)
    print(reqs)
    for i in range(0,le):
        id = reqs[i]["EmpCode"]
        datetime = reqs[i]["OFFICEPUNCH"]
        string_date = str(datetime)
        date = string_date.split(' ')[0]
        time = string_date.split(' ')[1]
        if frappe.db.exists({"doctype": "Employee Checkin", "employee": id,"time":date + " " + time}):
            pass
        else:
            doc = frappe.get_doc(dict(
                doctype = "Employee Checkin",
                employee = id,
                time = date + " " + time,
                device_id = "OFFICEPUNCH",
                skip_auto_attendance = '0'
            )).insert(ignore_permissions = False)
        frappe.db.commit()


@frappe.whitelist()
def manual(nam):
    doc = frappe.get_doc('Biometric Integration',nam)
    data = doc.url.format(frappe.utils.get_url())
    s = doc.from_date
    url = data + "&frm=" + str(s)
    print(nam)
    print(url)
    headerInfo = {'content-type': 'application/json'}
    r = requests.get(url, headers=headerInfo)
    req = json.loads(r.text)
    reqs = json.loads(req)
    le = len(reqs)
    print(reqs)
    for i in range(0,le):
        id = reqs[i]["EmpCode"]
        datetime = reqs[i]["OFFICEPUNCH"]
        string_date = str(datetime)
        date = string_date.split(' ')[0]
        time = string_date.split(' ')[1]
        # employee_nam = frappe.db.get_value('Employee',id,'employee_name')
        # or frappe.db.exists({"doctype": "Shift Assignment", "employee": id + ":" + employee_nam}):
        if frappe.db.exists({"doctype": "Employee Checkin", "employee": id,"time":date + " " + time}):
            pass
        else:
            doc = frappe.get_doc(dict(
                doctype = "Employee Checkin",
                employee = id,
                time = date + " " + time,
                device_id = "OFFICEPUNCH",
                skip_auto_attendance = '0'
            )).insert(ignore_permissions = False)
        frappe.db.commit()