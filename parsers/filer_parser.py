"""
Purpose:
    Transform filer objects.

Responsibilities:
    - Parse raw SDK filer data
    - Normalize fields

Input:
    Raw filer SDK object

Output:
    Parsed dictionary

Notes:
    Pure transformation only.
    No API calls.
"""

def parse_filer(filer):
    """
    Parse raw filer object into normalized dictionary.

    Parse EVERYTHING useful once.
    Display layer decides what to print.
    """

    try:

        connection = filer.deviceConnectionStatus
        reported = filer.deviceReportedStatus

        device_status = reported["status"]["device"]
        storage_summary = reported["status"]["storage"]["summary"]

        device_config = reported["config"]["device"]

        proc_storage = reported["proc"]["storage"]["summary"]

        backup_status = (
            reported["proc"]["backup"]["backupStatus"]
        )

        sync_status = (
            backup_status["backupHistory"]
            ["syncLastStatus"]
        )

        device_time = (
            backup_status["deviceTime"]
        )

        parsed_filer = {

            # --------------------------------------------------
            # Identity
            # --------------------------------------------------
            "name": filer.name,
            "owner": filer.owner,
            "hostname": device_config.get("hostname"),
            "location": device_config.get("location"),
            "device_type": filer.deviceType,
            "hardware_model":
                device_status.get("hardwareModel"),
            "platform":
                device_status.get("platform"),

            # --------------------------------------------------
            # Connectivity
            # --------------------------------------------------
            "connected":
                connection.get("connected"),

            "private_ip":
                connection.get("privateIP"),

            "public_ip":
                connection.get("publicIP"),

            "update_time":
                connection.get("updateTime"),

            # --------------------------------------------------
            # Firmware / License
            # --------------------------------------------------
            "firmware":
                device_status.get(
                    "runningFirmware"
                ),

            "license_status":
                device_status.get(
                    "licenseStatus"
                ),

            "reboot_required":
                device_status.get(
                    "rebootRequired"
                ),

            "serial_number":
                device_status.get(
                    "SerialNumber"
                ),

            "mac_address":
                device_status.get(
                    "MacAddress"
                ),

            # --------------------------------------------------
            # Storage Summary
            # --------------------------------------------------
            "storage_state":
                storage_summary.get(
                    "state"
                ),

            "physical_drive_space":
                storage_summary.get(
                    "physicalDriveSpace"
                ),

            "logical_drive_space":
                storage_summary.get(
                    "logicalDriveSpace"
                ),

            "allocated_drive_space":
                storage_summary.get(
                    "allocatedDriveSpace"
                ),

            "available_drive_space":
                storage_summary.get(
                    "availableDriveSpace"
                ),

            "total_drive_count":
                storage_summary.get(
                    "totalDriveCount"
                ),

            "total_volume_count":
                storage_summary.get(
                    "totalVolumeCount"
                ),

            # --------------------------------------------------
            # Volume Usage
            # --------------------------------------------------
            "total_volume_space":
                proc_storage.get(
                    "totalVolumeSpace"
                ),

            "used_volume_space":
                proc_storage.get(
                    "usedVolumeSpace"
                ),

            "free_volume_space":
                proc_storage.get(
                    "freeVolumeSpace"
                ),

            # --------------------------------------------------
            # Backup / Sync
            # --------------------------------------------------
            "backup_status":
                backup_status["serviceStatus"]
                .get("id"),

            "backup_description":
                backup_status["serviceStatus"]
                .get("desc"),

            "last_sync_result":
                sync_status.get(
                    "lastSyncResult"
                ),

            "last_sync_rc":
                sync_status.get(
                    "lastSyncRC"
                ),

            "last_started_sync":
                sync_status.get(
                    "lastStartedSync"
                ),

            "last_ended_sync":
                sync_status.get(
                    "lastEndedSync"
                ),

            "next_start_time":
                backup_status.get(
                    "nextStartTime"
                ),

            "seeding_enabled":
                backup_status.get(
                    "seedingEnabled"
                ),

            "backup_disabled":
                backup_status.get(
                    "isDisabled"
                ),

            # --------------------------------------------------
            # Time / Uptime
            # --------------------------------------------------
            "gmt_time":
                device_time.get("TimeGMT"),

            "local_time":
                device_time.get("LocalTime"),

            "uptime":
                device_time.get("uptime")
        }

        return parsed_filer

    except Exception as e:

        print(
            f"Failed to parse filer "
            f"{filer.name}: {e}"
        )

        return None