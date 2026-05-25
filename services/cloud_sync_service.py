"""
Purpose:
    Cloud sync monitoring.

Responsibilities:
    - Collect sync data
    - Parse sync status
    - Display sync information

Input:
    Authenticated admin object

Output:
    Cloud sync monitoring

Notes:
    Orchestration layer.
"""
from collectors.cloud_sync_collector import (
    collect_cloud_sync_status
)

from parsers.sync_parser import (
    parse_cloud_sync_status
)

from display.terminal import (
    display_filers
)


def show_cloud_sync_status(admin):
    """
    Show cloud sync status
    for all Edge Filers
    """

    # ---------------------------------------------------
    # Collect raw sync data
    # ---------------------------------------------------
    collected_sync = (
        collect_cloud_sync_status(admin)
    )

    # ---------------------------------------------------
    # Parse sync data
    # ---------------------------------------------------
    parsed_syncs = []

    for sync in collected_sync:

        parsed = parse_cloud_sync_status(
            sync
        )

        if parsed:
            parsed_syncs.append(parsed)

    print(
        f"\n✅ Successfully parsed "
        f"{len(parsed_syncs)} "
        f"sync status object(s)"
    )

    print(
        f"\n✅ Device Status Summary: "
    )

    # ---------------------------------------------------
    # Display columns
    # ---------------------------------------------------
    display_columns = [
        "name",
        "sync_status",
        "last_failed_scan_time",
        "last_failed_upload_file",
        "last_upload_delete_file",
        "last_upload_file",
        "read_sync_knowledge"
    ]

    # ---------------------------------------------------
    # Display
    # ---------------------------------------------------
    display_filers(
        parsed_syncs,
        display_columns
    )