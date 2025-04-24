import frappe
from frappe.utils import get_url_to_form, nowdate

def assign_lead_to_group_users(doc, method):
    if not doc.user_group:
        return

    # Get users from the user group
    user_entries = frappe.get_all(
        "User Group Member",
        filters={"parent": doc.user_group},
        fields=["user"]
    )

    if not user_entries:
        return

    for entry in user_entries:
        user_id = entry.user

        # Create ToDo for the user
        frappe.get_doc({
            "doctype": "ToDo",
            "allocated_to": user_id,
            "reference_type": "Lead",
            "reference_name": doc.name,
            "description": f"You have been assigned a new Lead: {doc.name}",
            "date": nowdate(),
        }).insert(ignore_permissions=True)

        # Send email notification
        send_lead_assignment_email(user_id, doc)


def send_lead_assignment_email(user_id, lead_doc):
    user = frappe.get_doc("User", user_id)
    email = user.email
    names = user.full_name

    if not email:
        return

    lead_link = get_url_to_form("Lead", lead_doc.name)
    subject = f"New Lead Assigned: {lead_doc.name}"
    message = f"""
        <p>Hello {names},</p>
        <p>You have been assigned a new lead: <b>{lead_doc.name}</b></p>
        <p>Click here to view the lead: <a href="{lead_link}">{lead_doc.name}</a></p>
        <br>
        <p>Regards,<br>Your CRM System</p>
    """

    frappe.sendmail(
        recipients=[email],
        subject=subject,
        message=message,
    )
