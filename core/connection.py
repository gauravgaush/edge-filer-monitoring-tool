"""
Purpose:
    Handle connection to CTERA portal.

Responsibilities:
    - Login to portal
    - Return authenticated admin session

Input:
    portal, username, password

Output:
    Logged-in admin object

Notes:
    Shared by all services.
"""
import cterasdk.settings
from cterasdk import ServicesPortal, GlobalAdmin


def connect_to_portal(portal, username, password):
    """
    Connect to CTERA Portal and return admin session
    """

    try:
        cterasdk.settings.core.syn.settings.connector.ssl = False

        admin = GlobalAdmin(portal)
        admin.login(username, password)

        print(f"\n✅ Connected to portal: {portal}")

        return admin

    except Exception as e:
        print(f"\n❌ Failed to connect: {e}")
        return None