import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_field

def create_custom_fields():
    custom_fields = {
        "Lead": [
            {
                "fieldname": "lead_product",
                "fieldtype": "Link",
                "label": "Lead Product",
                "options": "Lead Product",
                "insert_after": "source",
                "in_list_view": 1,
                "reqd": 0,
            },
            {
                "fieldname": "user_group",
                "fieldtype": "Read Only",
                "label": "Lead Assigned Group",
                "fetch_from": "lead_product.user_group",  
                "insert_after": "lead_product",
                "in_list_view": 1,
                "reqd": 0,
            }
        ],
    }

    for doctype, fields in custom_fields.items():
        for field in fields:
            if not frappe.db.exists("Custom Field", {"dt": doctype, "fieldname": field["fieldname"]}):
                create_custom_field(doctype, field)

def delete_custom_fields():
    custom_fields_to_delete = {
        "Lead": ["lead_product", "user_group"],
    }

    for doctype, fields in custom_fields_to_delete.items():
        for field_name in fields:
            if frappe.db.exists("Custom Field", {"dt": doctype, "fieldname": field_name}):
                frappe.delete_doc("Custom Field", f"{doctype}-{field_name}", ignore_missing=True)

    frappe.db.commit()
