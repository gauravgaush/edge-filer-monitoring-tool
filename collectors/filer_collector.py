def collect_all_filers(admin):
    """
    Retrieve all Edge Filers from portal.

    Returns:
        list: Raw filer objects from CTERA SDK
    """

    try:
        print("\nCollecting Edge Filers...")

        fields = [
            "owner",
            "deviceConnectionStatus",
            "deviceReportedStatus"
        ]

        # Convert generator → list
        filers = list(admin.devices.filers(fields))

        print(f"✅ Collected {len(filers)} filer(s)")

        return filers

    except Exception as e:
        print(f"❌ Failed to collect filers: {e}")
        return []