import requests
import frappe
import json
from frappe import _, throw
from typing import Dict, Any

@frappe.whitelist()
def sync_leads_from_external_api() -> Dict[str, Any]:
    try:
        api_settings = frappe.get_single("Lead APIs")
        url = api_settings.api_url
        token = api_settings.token
        auth_type = api_settings.authentication_type

        headers = _build_auth_headers(auth_type, token)

        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        leads = _parse_api_response(response)
        results = _process_leads(leads)

        return {
            "status": "Success",
            "message": _("Lead import completed"),
            "details": results
        }

    except requests.exceptions.RequestException as e:
        return {"status": "Failed", "error": _("API request failed: {}").format(str(e))}

    except Exception as e:
        frappe.log_error(title="Lead Import Error", message=str(e))
        return {"status": "Failed", "error": _("Unexpected Error: {}").format(str(e))}


def _build_auth_headers(auth_type: str, token: str) -> Dict[str, str]:
    headers = {}
    if auth_type == "Bearer Token":
        headers["Authorization"] = f"Bearer {token}"
    elif auth_type == "Basic Auth":
        headers["Authorization"] = f"Basic {token}"
    return headers


def _parse_api_response(response: requests.Response) -> list:
    try:
        data = response.json()
        leads = data.get("data", [])
        if not isinstance(leads, list):
            raise ValueError(_("Invalid format: 'data' is not a list"))
        return leads
    except json.JSONDecodeError:
        raise ValueError(_("Invalid JSON response from API"))


def _process_leads(leads: list) -> Dict[str, int]:
    results = {"total": len(leads), "created": 0, "failed": 0, "skipped": 0}
    
    for lead in leads:
        if not isinstance(lead, dict):
            results["failed"] += 1
            continue

        try:
            email = lead.get("email", "").strip().lower()
            phone = lead.get("phone", "").strip()
            lead_product = lead.get("product_name", "").strip()

            if not email:
                results["failed"] += 1
                continue

            if frappe.db.exists("Lead", {
                "email_id": email,
                "mobile_no": phone,
                "lead_product": lead_product
            }):
                results["skipped"] += 1
                continue

            lead_doc = _create_lead_doc(lead)
            lead_doc.insert(ignore_permissions=True)
            results["created"] += 1

        except Exception as e:
            results["failed"] += 1
            frappe.log_error(_("Lead Import Error"), f"{str(e)}\nPayload: {json.dumps(lead)}")

    return results


def _create_lead_doc(lead: Dict[str, Any]) -> frappe.model.document.Document:
    source = lead.get("source_platform", "").strip()
    if source and not frappe.db.exists("Lead Source", source):
        source = None

    return frappe.get_doc({
        "doctype": "Lead",
        "email_id": lead.get("email", "").strip().lower(),
        "first_name": lead.get("first_name", ""),
        "last_name": lead.get("last_name", ""),
        "company_name": lead.get("company_name", ""),
        "mobile_no": lead.get("phone", "").strip(),
        "job_title": lead.get("job_title", ""),
        "source": source,
        "message": lead.get("message", ""),
        "status": "Lead",
        "lead_product": lead.get("product_name", "").strip()
    })
