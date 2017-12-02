cur_frm.add_fetch('item_group','default_warehouse','default_warehouse');
cur_frm.add_fetch('item_group','default_cost_center','selling_cost_center');
cur_frm.add_fetch('item_group','default_cost_center','buying_cost_center');
cur_frm.add_fetch('item_group','default_income_account','income_account');
cur_frm.add_fetch('item_group','default_expense_account','expense_account');
cur_frm.add_fetch('item_group','is_stock_item','is_stock_item');
cur_frm.add_fetch('item_group','has_batch_no','has_batch_no');
cur_frm.add_fetch('item_group','has_serial_no','has_serial_no');

frappe.ui.form.on("Item", {
    onload:  function(frm) {
        cur_frm.set_query("item_group", function() {
            return {
                "filters": {
                    "is_group": 0
                }
            };
        });
        if(frm.doc.__islocal){
            cur_frm.set_value('item_group', '');
            cur_frm.set_value('default_warehouse', '');
        }
    }
});