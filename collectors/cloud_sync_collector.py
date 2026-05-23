def collect_cloud_sync_status(admin):
    """
    Collect cloud sync status
    for all Edge Filers
    """

    try:

        filers = list(
            admin.devices.filers()
        )

        collected_sync = []

        for filer in filers:

            print(
                f"Checking: {filer.name}"
            )

            sync_status = (
                filer.sync.get_status()
            )

            collected_sync.append({

                "name":
                    filer.name,

                "sync_status":
                    sync_status
            })

        return collected_sync

    except Exception as e:

        print(
            f"Failed collecting "
            f"cloud sync status: {e}"
        )

        return []