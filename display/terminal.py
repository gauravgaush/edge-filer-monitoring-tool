"""
Purpose:
    Display parsed data.

Responsibilities:
    - Render terminal tables
    - Support dynamic columns

Input:
    Parsed dictionaries

Output:
    Console output

Notes:
    Display only.
    No API calls.
"""

def display_filers(parsed_filers, columns):
    """
    Dynamic filer table display
    Auto-adjust column widths
    """

    if not parsed_filers:
        print("\nNo filers found")
        return

    # ---------------------------------------------------
    # Friendly column names
    # ---------------------------------------------------
    column_headers = {
        "name": "Name",
        "connected": "Connected",
        "public_ip": "Public IP",
        "private_ip": "Private IP",
        "firmware": "Firmware",
        "storage_state": "Storage",
        "used_volume_space": "Used (GB)",
        "free_volume_space": "Free (GB)",
        "location": "Location",
        "license_status": "License",
        "hostname": "Hostname",
        "owner": "Owner",
        "hardware_model": "Model",
        "platform": "Platform",
        "uptime": "Uptime",
        "backup_status": "Backup",
        "last_sync_result": "Last Sync",

        # Cloud Sync
        "sync_status": "Sync Status",
        "last_failed_scan_time": "Last Failed Scan",
        "last_failed_upload_file": "Failed Upload",
        "last_upload_delete_file": "Deleted File",
        "last_upload_file": "Last Upload",
        "read_sync_knowledge": "Sync Knowledge",
        "uploading_files": "Uploading",
        "downloading_files": "Downloading",
        "streaming_files": "Streaming",
        "on_demand_files": "On Demand",
        "files_failed_upload": "Failed Files",
        "last_successful_scan": "Last Scan",
        "scanning_files": "Scanning",
        "scanning_stubs": "Stubs",
        "partial_scanning": "Partial Scan",
        "is_full_scan": "Full Scan",

        # Zones 
        "zone_id": "Zone ID",
        "description": "Description",
        "devices_count": "Devices",
        "is_default": "Default",
        "device_names": "Edge Filers",
        "device_types": "Device Type",
        "device_owners": "Owner",
        "total_files": "Files",
        "total_folders": "Folders",
        "total_size": "Size (MB)",
        "cloud_drive_folders": "Cloud Drive Folders",
        
    }

    # ---------------------------------------------------
    # Auto column width
    # ---------------------------------------------------
    column_widths = {}

    for column in columns:

        header = column_headers.get(
            column,
            column
        )

        max_width = len(header)

        for filer in parsed_filers:

            value = filer.get(column, "N/A")

            # Convert MB → GB for display
            if column in [
                "used_volume_space",
                "free_volume_space",
                "total_volume_space"
            ]:
                if value is not None:
                    value = round(value / 1024, 2)

            value_length = len(str(value))

            if value_length > max_width:
                max_width = value_length

        # Padding
        column_widths[column] = max_width + 4

    # ---------------------------------------------------
    # Table width
    # ---------------------------------------------------
    total_width = sum(column_widths.values())

    print("\n" + "=" * total_width)

    # ---------------------------------------------------
    # Headers
    # ---------------------------------------------------
    for column in columns:

        header = column_headers.get(
            column,
            column
        )

        print(
            f"{header:<{column_widths[column]}}",
            end=""
        )

    print()

    print("=" * total_width)

    # ---------------------------------------------------
    # Rows
    # ---------------------------------------------------
    for filer in parsed_filers:

        for column in columns:

            value = filer.get(column, "N/A")

            # Convert MB → GB
            if column in [
                "used_volume_space",
                "free_volume_space",
                "total_volume_space"
            ]:
                if value is not None:
                    value = round(value / 1024, 2)

            print(
                f"{str(value):<{column_widths[column]}}",
                end=""
            )

        print()

    print("=" * total_width)

    print(
        f"\nTotal Filers: "
        f"{len(parsed_filers)}"
    )