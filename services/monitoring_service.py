from collectors.filer_collector import collect_all_filers
from parsers.filer_parser import parse_filer
from display.terminal import display_filers


def show_filer_monitoring(admin):
    """
    Collect, parse and display filer monitoring
    """

    # -----------------------------------------------------
    # Collect raw filers
    # -----------------------------------------------------
    filers = collect_all_filers(admin)

    # -----------------------------------------------------
    # Parse filers
    # -----------------------------------------------------
    parsed_filers = []

    for filer in filers:

        parsed = parse_filer(filer)

        if parsed:
            parsed_filers.append(parsed)

    print(
        f"\n✅ Successfully parsed "
        f"{len(parsed_filers)} filer(s)"
    )

    print(
        f"\n✅ Cloud Sync Status Summary: "
    )

    # -----------------------------------------------------
    # Default monitoring columns
    # -----------------------------------------------------
    display_columns = [
        "name",
        "connected",
        "public_ip",
        "firmware",
        "storage_state",
        "used_volume_space",
        "free_volume_space",
        "location"
    ]

    # -----------------------------------------------------
    # Display
    # -----------------------------------------------------
    display_filers(
        parsed_filers,
        display_columns
    )