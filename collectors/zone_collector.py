"""
Purpose:
    Collect zone information.

Responsibilities:
    - Retrieve zones
    - Retrieve mapped cloud folders
    - Return enriched zone data

Input:
    Authenticated admin object

Output:
    Zone objects with cloud folders

Notes:
    Uses getZoneFolders API.
"""

from cterasdk import Object
from cterasdk.core import query


def _zone_query_param(zone_id):
    """
    Build query parameter
    for getZoneFolders
    """

    param = Object()

    builder = (
        query.QueryParamBuilder()
        .include_classname()
        .startFrom(0)
        .countLimit(100)
        .orFilter(True)
    )

    param.query = builder.build()

    param._classname = "ZoneQuery"

    param.delta = Object()
    param.delta._classname = "ZoneDelta"
    param.delta.policyDelta = []

    param.zoneId = zone_id

    return param


def collect_all_zones(admin):
    """
    Collect all zones
    including cloud drive folders
    """

    try:

        zones = list(
            admin.cloudfs.zones.all()
        )

        print(
            "\nCollecting Zones..."
        )

        print(
            f"✅ Collected "
            f"{len(zones)} zone(s)"
        )

        collected_zones = []

        for zone in zones:

            try:

                # -----------------------------------
                # Query parameter
                # -----------------------------------
                param = (
                    _zone_query_param(
                        zone.zoneId
                    )
                )

                # -----------------------------------
                # Get cloud drive folders
                # -----------------------------------
                response = (
                    admin.api.execute(
                        '/',
                        'getZoneFolders',
                        param
                    )
                )

                folders = [
                    folder.name
                    for folder
                    in response.objects
                ]

            except Exception as e:

                print(
                    f"Failed to get "
                    f"folders for zone "
                    f"{zone.name}: {e}"
                )

                folders = []

            collected_zones.append({

                "zone":
                    zone,

                "cloud_drive_folders":
                    folders
            })

        return collected_zones

    except Exception as e:

        print(
            f"❌ Failed to "
            f"collect zones: {e}"
        )

        return []