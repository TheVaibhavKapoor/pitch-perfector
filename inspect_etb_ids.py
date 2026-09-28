import os, re


def get_content(fpath):
    try:
        return open(fpath, "r", encoding="utf-16").read()
    except Exception:
        return open(fpath, "r", encoding="utf-8", errors="ignore").read()


def save_content(fpath, content):
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)


# Targeted fix for customer_overview_solitaire.html:
# The existing modals are fine (send-deck and create-lead-modal exist),
# but the Disposition modal needs openDispositionModal() to read
# the correct DOM fields from the ETB page.
# The ETB page has: cust-name, cust-phone, cust-email or similar

def fix_etb_file(fpath):
    content = get_content(fpath)

    # Find name/phone/email elements IDs in the ETB file
    name_ids = re.findall(r'id=["\']([^"\']*(?:name|cust)[^"\']*)["\']', content, re.IGNORECASE)
    phone_ids = re.findall(r'id=["\']([^"\']*(?:phone|mobile)[^"\']*)["\']', content, re.IGNORECASE)
    email_ids = re.findall(r'id=["\']([^"\']*(?:email)[^"\']*)["\']', content, re.IGNORECASE)
    print("Name-like IDs found:", list(set(name_ids))[:10])
    print("Phone-like IDs found:", list(set(phone_ids))[:10])
    print("Email-like IDs found:", list(set(email_ids))[:10])

fix_etb_file("customer_overview_solitaire.html")
