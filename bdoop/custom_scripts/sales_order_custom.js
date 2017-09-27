frappe.ui.form.on("Sales Order", {
    onload:  function(frm) {
        if(frm.doc.delivery_date=='' || frm.doc.delivery_date == undefined)
            setDeliveryDate(frm);
    },
    transaction_date: function(frm, cdt, cdn){
        setDeliveryDate(frm);
    }
});

var setDeliveryDate= function(frm){
    cur_frm.set_value('delivery_date', frappe.datetime.add_months(frm.doc.transaction_date, 6));
}