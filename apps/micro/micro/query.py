import frappe
import datetime as dt

@frappe.whitelist()
def get_employee_details(user_id):
  full_name, doc_name = frappe.db.get_value('Employee', {'user_id':user_id}, ['employee_name','name'])
  url = frappe.db.get_value("File",{'attached_to_doctype':"Employee",'attached_to_name':doc_name},"file_url")
  image_url = "None"
  if url:
    url = url.replace(" ","%")
    image_url = url

  return image_url, full_name, doc_name

def attendance_duration(self,method):
  duration = (dt.strptime(self.out_time,"%Y-%m-%d %H:%M:%S") - dt.strptime(self.in_time,"%Y-%m-%d %H:%M:%S")).total_seconds()
  self.custom_total_working_duration = duration

@frappe.whitelist()
def get_events():
	"""Returns events for Gantt / Calendar view rendering.
	"""
	
	data = frappe.db.sql("""
SELECT IF(weekly_off, "Weekly Off", "Holiday") as Status, holiday_date as Date from `tabHoliday` WHERE year(holiday_date) = YEAR(CURDATE()) UNION ALL SELECT status as Status,attendance_date as Date from `tabAttendance` WHERE year(attendance_date) = YEAR(CURDATE())
		""", as_dict=True)
	return data
