def suspend_cloud_sync(admin):
    """
    Suspend cloud sync on:

    - One Edge Filer
    - ALL Edge Filers (protected confirmation)
    """

    try:

        filers = list(
            admin.devices.filers()
        )

        # --------------------------------------------------
        # User input
        # --------------------------------------------------
        target = input(
            "\nEnter Edge Filer name "
            "for suspending Cloud Sync\n"
            "(or type ALL for all filers): "
        ).strip()

        # --------------------------------------------------
        # Suspend ALL filers
        # --------------------------------------------------
        if target.upper() == "ALL":

            print(
                "\n⚠ WARNING"
            )

            print(
                "You are about to suspend "
                "Cloud Sync on ALL Edge Filers."
            )

            print(
                "\nType EXACTLY:\n"
                "SUSPEND CLOUD SYNC ALL\n"
            )

            confirmation = input("> ").strip()

            if (
                confirmation
                != "SUSPEND CLOUD SYNC ALL"
            ):

                print(
                    "\n❌ Confirmation failed."
                )

                print(
                    "Operation cancelled."
                )

                return

            suspended_count = 0

            for filer in filers:

                print(
                    f"Suspending: "
                    f"{filer.name}"
                )

                filer.sync.suspend()

                print(
                    f"✅ Cloud sync suspended "
                    f"for {filer.name}"
                )

                suspended_count += 1

            print(
                f"\n✅ Suspended Cloud Sync "
                f"on {suspended_count} "
                f"filer(s)"
            )

            return

        # --------------------------------------------------
        # Suspend ONE filer
        # --------------------------------------------------
        suspended = False

        for filer in filers:

            print(
                f"Checking: {filer.name}"
            )

            if (
                filer.name.strip().lower()
                ==
                target.lower()
            ):

                print(
                    f"Found: {filer.name}"
                )

                filer.sync.suspend()

                print(
                    f"✅ Cloud sync suspended "
                    f"for {filer.name}"
                )

                suspended = True
                break

        if not suspended:

            print(
                f"\n❌ Edge Filer "
                f"not found: {target}"
            )

    except Exception as e:

        print(
            f"\n❌ Failed to suspend "
            f"cloud sync: {e}"
        )

def un_suspend_cloud_sync(admin):
    """
    Unsuspend cloud sync on:

    - One Edge Filer
    - ALL Edge Filers (protected confirmation)
    """

    try:

        filers = list(
            admin.devices.filers()
        )

        # --------------------------------------------------
        # User Input
        # --------------------------------------------------
        target = input(
            "\nEnter Edge Filer name "
            "for UNSUSPENDING Cloud Sync\n"
            "(or type ALL for all filers): "
        ).strip()

        # --------------------------------------------------
        # Unsuspend ALL filers
        # --------------------------------------------------
        if target.upper() == "ALL":

            print(
                "\n⚠ WARNING"
            )

            print(
                "You are about to "
                "UNSUSPEND Cloud Sync "
                "on ALL Edge Filers."
            )

            print(
                "\nType EXACTLY:\n"
                "UNSUSPEND CLOUD SYNC ALL\n"
            )

            expected_confirmation = (
                "UNSUSPEND CLOUD SYNC ALL"
            )

            confirmation = input("> ").strip()

            if (
                confirmation.strip().upper()
                != expected_confirmation
            ):

                print(
                    "\n❌ Confirmation failed"
                )

                print(
                    "\nExpected:"
                )

                print(
                    expected_confirmation
                )

                print(
                    "\nOperation cancelled."
                )

                return

            unsuspended_count = 0

            for filer in filers:

                print(
                    f"Unsuspending: "
                    f"{filer.name}"
                )

                filer.sync.unsuspend()

                print(
                    f"✅ Cloud sync "
                    f"unsuspended for "
                    f"{filer.name}"
                )

                unsuspended_count += 1

            print(
                f"\n✅ Unsuspended "
                f"Cloud Sync on "
                f"{unsuspended_count} "
                f"filer(s)"
            )

            return

        # --------------------------------------------------
        # Unsuspend ONE filer
        # --------------------------------------------------
        unsuspended = False

        for filer in filers:

            print(
                f"Checking: "
                f"{filer.name}"
            )

            if (
                filer.name.strip().lower()
                ==
                target.lower()
            ):

                print(
                    f"Found: "
                    f"{filer.name}"
                )

                filer.sync.unsuspend()

                print(
                    f"✅ Cloud sync "
                    f"unsuspended for "
                    f"{filer.name}"
                )

                unsuspended = True
                break

        if not unsuspended:

            print(
                f"\n❌ Edge Filer "
                f"not found: {target}"
            )

    except Exception as e:

        print(
            f"\n❌ Failed to "
            f"unsuspend cloud sync: "
            f"{e}"
        )