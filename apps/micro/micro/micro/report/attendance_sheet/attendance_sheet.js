// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt


frappe.query_reports["Attendance Sheet"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"reqd": 1 ,
			"default":frappe.datetime.str_to_obj(frappe.datetime.get_today())
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"reqd": 1,
			"default":frappe.datetime.str_to_obj(frappe.datetime.get_today())
		},
		{
			"fieldname":"employee",
			"label": __("Employee"),
			"fieldtype": "Link",
			"options": "Employee",
			get_query: () => {
				var company = frappe.query_report.get_filter_value('company');
				return {
					filters: {
						'company': company
					}
				};
			}
		},
		{
			"fieldname":"company",
			"label": __("Company"),
			"fieldtype": "Link",
			"options": "Company",
			"default": frappe.defaults.get_user_default("Company"),
			"reqd": 1
		},
		{
			"fieldname":"group_by",
			"label": __("Group By"),
			"fieldtype": "Select",
			"options": ["","Branch","Grade","Department","Designation"]
		},
		
	],
	// onload: function() {
	// 	return  frappe.call({
	// 		method: "hrms.hr.report.monthly_attendance_sheet.monthly_attendance_sheet.get_attendance_years",
	// 		callback: function(r) {
	// 			var year_filter = frappe.query_report.get_filter('year');
	// 			year_filter.df.options = r.message;
	// 			year_filter.df.default = r.message.split("\n")[0];
	// 			year_filter.refresh();
	// 			year_filter.set_input(year_filter.df.default);
	// 		}
	// 	});
	// },
	formatter: function(value, row, column, data, default_formatter) {
		value = default_formatter(value, row, column, data);
		const summarized_view = frappe.query_report.get_filter_value('summarized_view');
		const group_by = frappe.query_report.get_filter_value('group_by');

		if (!summarized_view) {
			if ((group_by && column.colIndex > 3) || (!group_by && column.colIndex > 2)) {
				if (value == 'P' || value == 'WFH')
					value = "<span style='color:green'>" + value + "</span>";
				else if (value == 'A')
					value = "<span style='color:red'>" + value + "</span>";
				else if (value == 'HD')
					value = "<span style='color:orange'>" + value + "</span>";
				else if (value == 'L')
					value = "<span style='color:#318AD8'>" + value + "</span>";
			}
		}

		return value;
	}

}
