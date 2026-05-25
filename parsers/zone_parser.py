"""
Purpose:
    Transform zone data.

Responsibilities:
    - Parse zone information
    - Normalize devices
    - Normalize cloud folders

Input:
    Collected zone object

Output:
    Parsed dictionary

Notes:
    Pure transformation only.
"""
def parse_zone(collected_zone):
    """
    Parse zone object.

    Parse everything useful once.
    Display decides what to show.
    """
    zone = collected_zone["zone"]

    try:

        # ---------------------------------------
        # Top Devices
        # ---------------------------------------
        top_devices = getattr(
            zone,
            "topDevices",
            []
        )

        device_names = [
            device.get("name")
            for device in top_devices
        ]

        device_types = [
            device.get("deviceType")
            for device in top_devices
        ]

        device_owners = [
            device.get("owner")
            for device in top_devices
        ]

        # ---------------------------------------
        # Zone Statistics
        # ---------------------------------------
        zone_stats = getattr(
            zone,
            "zoneStatistics",
            {}
        )

        parsed_zone = {

            # ---------------------------------------
            # Identity
            # ---------------------------------------
            "name":
                getattr(
                    zone,
                    "name",
                    None
                ),

            "zone_id":
                getattr(
                    zone,
                    "zoneId",
                    None
                ),

            "description":
                getattr(
                    zone,
                    "description",
                    None
                ),
            "cloud_drive_folders":
                ", ".join(
                    collected_zone[
                        "cloud_drive_folders"
                    ]
                ),

            # ---------------------------------------
            # Zone Config
            # ---------------------------------------
            "devices_count":
                getattr(
                    zone,
                    "devicesCount",
                    0
                ),

            "is_default":
                getattr(
                    zone,
                    "isDefault",
                    False
                ),

            # ---------------------------------------
            # Devices
            # ---------------------------------------
            "device_names":
                ", ".join(
                    device_names
                ),

            "device_types":
                ", ".join(
                    device_types
                ),

            "device_owners":
                ", ".join(
                    device_owners
                ),

            # ---------------------------------------
            # Statistics
            # ---------------------------------------
            "total_files":
                zone_stats.get(
                    "totalFiles",
                    0
                ),

            "total_folders":
                zone_stats.get(
                    "totalFolders",
                    0
                ),

            "total_size":
                round(
                    zone_stats.get(
                        "totalSize",
                        0
                    ) / 1024 / 1024,
                    2
                )
        }

        return parsed_zone

    except Exception as e:

        print(
            f"❌ Failed parsing "
            f"zone: {e}"
        )

        return None