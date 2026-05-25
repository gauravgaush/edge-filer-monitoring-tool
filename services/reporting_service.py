"""
Purpose:
    Reporting menu.

Responsibilities:
    - Export filer reports
    - Export sync reports
    - Export zone reports

Input:
    User selection

Output:
    CSV reports

Notes:
    Report orchestration layer.
"""
from collectors.filer_collector import (
    collect_all_filers
)

from collectors.zone_collector import (
    collect_all_zones
)

from parsers.filer_parser import (
    parse_filer
)

from parsers.zone_parser import (
    parse_zone
)

from parsers.sync_parser import (
    parse_cloud_sync_status
)

from services.cloud_sync_service import (
    collect_cloud_sync_status
)

from reporting.csv_exporter import (
    export_csv
)


def report_menu(admin):
    """
    Report menu
    """

    while True:

        print("\n" + "=" * 60)

        print("REPORT MENU")

        print("=" * 60)

        print("1. Export Filer Monitoring Report")
        print("2. Export Zone Report")
        print("3. Export Cloud Sync Report")
        print("0. Back")

        choice = input(
            "\nEnter choice: "
        ).strip()

        # -----------------------------------
        # Filer Monitoring
        # -----------------------------------
        if choice == "1":

            export_filer_report(
                admin
            )

        # -----------------------------------
        # Zone Report
        # -----------------------------------
        elif choice == "2":

            export_zone_report(
                admin
            )

        # -----------------------------------
        # Cloud Sync Report
        # -----------------------------------
        elif choice == "3":

            export_sync_report(
                admin
            )

        # -----------------------------------
        # Back
        # -----------------------------------
        elif choice == "0":

            return

        else:

            print(
                "\n❌ Invalid choice"
            )


def export_filer_report(admin):
    """
    Export filer report
    """

    filers = collect_all_filers(
        admin
    )

    parsed_filers = []

    for filer in filers:

        parsed = parse_filer(
            filer
        )

        if parsed:
            parsed_filers.append(
                parsed
            )

    export_csv(
        parsed_filers,
        "filer_monitoring"
    )


def export_zone_report(admin):
    """
    Export zone report
    """

    zones = collect_all_zones(
        admin
    )

    parsed_zones = []

    for zone in zones:

        parsed = parse_zone(
            zone
        )

        if parsed:
            parsed_zones.append(
                parsed
            )

    export_csv(
        parsed_zones,
        "zone_monitoring"
    )


def export_sync_report(admin):
    """
    Export sync report
    """

    syncs = collect_cloud_sync_status(
        admin
    )

    parsed_syncs = []

    for sync in syncs:

        parsed = parse_cloud_sync_status(
            sync
        )

        if parsed:
            parsed_syncs.append(
                parsed
            )

    export_csv(
        parsed_syncs,
        "cloud_sync"
    )