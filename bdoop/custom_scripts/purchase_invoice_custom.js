$('[data-fieldname="posting_yymm"]').hide();

var posting_yymm = function(frm){
	var ymd = frm.doc.posting_date;
	var yy = ymd.substring(2,4);
	var mm = ymd.substring(5,7);
	var ym = yy+""+mm;
	frm.set_value("posting_yymm", ym);
}

cur_frm.add_fetch('purchase_order','sales_order','sales_order');

frappe.ui.form.on("Purchase Invoice", "validate", function(frm) {
	posting_yymm(frm);
})

frappe.ui.form.on("Purchase Invoice", {
    onload:  function(frm) {
        var purchase_order_name = frm.doc.purchase_order;
        if(purchase_order_name){
            cur_frm.get_field("purchase_order").validate(cur_frm.doc.purchase_order);
        }
    },
    purchase_order: function(frm, cdt, cdn){
        cur_frm.get_field("purchase_order").validate(cur_frm.doc.purchase_order);
    }
});

var loadSalesOrder = function(frm){
    var purchase_order_name = frm.doc.purchase_order;

    if(purchase_order_name){
        frappe.call({
            method: "frappe.client.get",
            args: {
                doctype: "Purchase Order",
                name: purchase_order_name,
            },
            callback(r) {
                if(r.message) {
                    var purchase_order = r.message;
                    cur_frm.set_value('sales_order', purchase_order.sales_order);
                    loadCustomer(frm);
                }
            }
        });
    }
}
var loadCustomer = function(frm){
    var sales_order_name = frm.doc.sales_order;
    if(sales_order_name){
        frappe.call({
            method: "frappe.client.get",
            args: {
                doctype: "Sales Order",
                name: sales_order_name,
            },
            callback(r) {
                if(r.message) {
                    var sales_order = r.message;
                    cur_frm.set_value('customer', sales_order.customer);
                    cur_frm.get_field("customer").validate(cur_frm.doc.customer);
                }
            }
        });
    }
}