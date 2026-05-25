"""
Purpose:
    Transform cloud sync data.

Responsibilities:
    - Parse sync status
    - Apply sync business logic

Input:
    Raw sync object

Output:
    Parsed dictionary

Notes:
    Hide details for
    Synced/Off states.
"""

def parse_cloud_sync_status(collected_sync):
    """
    Parse cloud sync status.

    PURE TRANSFORMATION ONLY.
    No SDK/API calls here.
    """

    try:

        sync_status = (
            collected_sync["sync_status"]
        )

        # --------------------------------------------------
        # Business Logic
        # --------------------------------------------------
        sync_state = sync_status.get("id")

        show_details = (
            sync_state not in [
                "Off",
                "Synced"
            ]
        )

        # --------------------------------------------------
        # Parsed Output
        # --------------------------------------------------
        parsed_sync = {

            # --------------------------------------------------
            # Identity
            # --------------------------------------------------
            "name":
                collected_sync["name"],

            # --------------------------------------------------
            # Sync Status
            # --------------------------------------------------
            "sync_status":
                sync_state,

            "last_failed_scan_time":
                sync_status.get(
                    "lastFailedScanTime"
                ) if show_details else None,
            
            "last_failed_upload_file":
                (
                    sync_status
                    .get("lastFailedUploadFile", {})
                    .get("name")
                )
                if (
                    show_details
                    and sync_status.get(
                        "lastFailedUploadFile"
                    )
                )
                else None,

            "last_upload_delete_file":
                (
                    sync_status
                    .get("lastUploadDeleteFile", {})
                    .get("name")
                )
                if (
                    show_details
                    and sync_status.get(
                        "lastUploadDeleteFile"
                    )
                )
                else None,

            "last_upload_file":
                (
                    sync_status
                    .get("lastUploadFile", {})
                    .get("name")
                )
                if (
                    show_details
                    and sync_status.get(
                        "lastUploadFile"
                    )
                )
                else None,

            "read_sync_knowledge":
                sync_status.get(
                    "readSyncKnowledge"
                ) if show_details else None,

            # --------------------------------------------------
            # Counters
            # --------------------------------------------------
            "uploading_files":
                sync_status.get(
                    "uploadingFiles"
                ),

            "downloading_files":
                sync_status.get(
                    "downloadingFiles"
                ),

            "streaming_files":
                sync_status.get(
                    "streamingFiles"
                ),

            "on_demand_files":
                sync_status.get(
                    "onDemandFiles"
                ),

            "files_failed_upload":
                sync_status.get(
                    "filesFailedToUpload"
                ),

            # --------------------------------------------------
            # Activity
            # --------------------------------------------------
            "last_successful_scan":
                sync_status.get(
                    "lastSuccessfulScanTime"
                ),

            "scanning_files":
                sync_status.get(
                    "scanningFiles"
                ),

            "scanning_stubs":
                sync_status.get(
                    "scanningStubs"
                ),

            "partial_scanning":
                sync_status.get(
                    "partialScanning"
                ),

            "is_full_scan":
                sync_status.get(
                    "isInFullScan"
                )
        }

        return parsed_sync

    except Exception as e:

        print(
            f"Failed parsing "
            f"sync status: {e}"
        )

        return None