# Currently not exposed in main menu. Used for debugging, development and future UI.
# Orchestration layer only.
"""
Purpose:
    Zone monitoring service.

Responsibilities:
    - Collect zone data
    - Parse zone information
    - Display zone monitoring

Input:
    Authenticated admin object

Output:
    Terminal zone monitoring

Notes:
    Currently not exposed
    in main menu.

    Used for debugging,
    development and future UI.

    Orchestration layer only.
"""

from collectors.zone_collector import (
    collect_all_zones
)

from parsers.zone_parser import (
    parse_zone
)

from display.terminal import (
    display_filers
)


def show_zone_monitoring(admin):
    """
    Show zone monitoring
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

    print(
        f"\n✅ Successfully "
        f"parsed "
        f"{len(parsed_zones)} "
        f"zone(s)"
    )

    # ---------------------------------------
    # Display view
    # ---------------------------------------
    display_columns = [
        "name",
        "devices_count",
        "device_names",
        "cloud_drive_folders",
        "total_files",
        "total_folders",
        "total_size"
    ]

    display_filers(
        parsed_zones,
        display_columns
    )