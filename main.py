import sys
from pathlib import Path
from display.terminal import display_filers
from services.cloud_sync_service import show_cloud_sync_status


# ---------------------------------------------------------
# Allow imports from project folders
# ---------------------------------------------------------
sys.path.append(str(Path(__file__).parent))

# ---------------------------------------------------------
# Imports
# ---------------------------------------------------------
from core.connection import connect_to_portal
from services.monitoring_service import (
    show_filer_monitoring
)


def main():

    # ---------------------------------------------------------
    # TEMP HARD-CODED VALUES (DEV ONLY)
    # ---------------------------------------------------------
    portal = "hcpae.lab.local"
    username = "globaladmin"
    password = "Gddchyd@1234"

    # ---------------------------------------------------------
    # Connect to Portal
    # ---------------------------------------------------------
    admin = connect_to_portal(
        portal,
        username,
        password
    )

    if not admin:
        print("Login failed")
        return

    print("Login successful")

    # ---------------------------------------------------------
    # Monitoring
    # ---------------------------------------------------------
    show_filer_monitoring(admin)
    show_cloud_sync_status(admin)
  
     
    # ---------------------------------------------------------
    # Logout / Cleanup
    # ---------------------------------------------------------
    admin.logout()

    print("\nLogged out successfully")

    


if __name__ == "__main__":
    main()