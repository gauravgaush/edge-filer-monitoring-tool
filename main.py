"""
Purpose:
    Main entry point for EF Tool.

Responsibilities:
    - Show menu
    - Route user actions
    - Initialize portal session
    - Cleanup logout

Input:
    User menu selections

Output:
    Monitoring, actions, reports

Notes:
    Keep business logic out of main.py
"""

import sys
from pathlib import Path
from services.reporting_service import report_menu

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

from services.cloud_sync_service import (
    show_cloud_sync_status
)

from services.sync_action_service import (
    suspend_cloud_sync
)

from services.sync_action_service import (
    un_suspend_cloud_sync
)


def show_menu():
    """
    Display application menu
    """

    print("\n" + "=" * 40)
    print("Edge Filer Management Tool")
    print("=" * 40)

    print("1. Filer Monitoring")
    print("2. Cloud Sync Status")
    print("3. Suspend Cloud Sync")
    print("4. Unsuspend Cloud Sync")
    print("5. Reports")
    print("0. Exit")
    

    return input(
        "\nSelect option: "
    ).strip()


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
    # Menu Loop
    # ---------------------------------------------------------
    while True:

        choice = show_menu()

        # -------------------------------------------------
        # Filer Monitoring
        # -------------------------------------------------
        if choice == "1":

            show_filer_monitoring(admin)

        # -------------------------------------------------
        # Cloud Sync Status
        # -------------------------------------------------
        elif choice == "2":

            show_cloud_sync_status(admin)

        # -------------------------------------------------
        # Suspend Cloud Sync
        # -------------------------------------------------
        elif choice == "3":

            suspend_cloud_sync(admin)
        
        # -------------------------------------------------
        # Suspend Cloud Sync
        # -------------------------------------------------       
        elif choice == "4":

            un_suspend_cloud_sync(admin)     
      
        # -------------------------------------------------
        # Reports
        # -------------------------------------------------       
        elif choice == "5":

             report_menu(admin)

        # -------------------------------------------------
        # Exit
        # -------------------------------------------------
        elif choice == "0":

            print(
                "\nLogging out..."
            )

            admin.logout()

            print(
                "Logged out successfully"
            )

            break

        # -------------------------------------------------
        # Invalid Choice
        # -------------------------------------------------
        else:

            print(
                "\n❌ Invalid option."
            )

            print(
                "Please choose 1-5."
            )


if __name__ == "__main__":
    main()