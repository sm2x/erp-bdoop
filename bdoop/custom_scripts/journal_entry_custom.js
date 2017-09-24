$('[data-fieldname="posting_yymm"]').hide();
var posting_yymm = function(frm){
	var ymd = frm.doc.posting_date;
	var yy = ymd.substring(2,4);
	var mm = ymd.substring(5,7);
	var ym = yy+""+mm;
	frm.set_value("posting_yymm", ym);
}

frappe.ui.form.on("Journal Entry", "validate", function(frm) {
	posting_yymm(frm);
})
frappe.ui.form.on("Journal Entry", {
    onload: function(frm) {
	var payment_type = frm.doc.payment_type;
	//frm.set_value("naming_series", "PEDE-.YY..MM..####");
    }
});