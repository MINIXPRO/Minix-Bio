frappe.ui.form.on('Biometric Integration', {
        start:function(frm) {
        frappe.call({
            method :"micro.api.manual",
            args: {
                nam : frm.doc.name,
            },
        });
    }
});