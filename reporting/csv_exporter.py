"""
Purpose:
    Export reports to CSV.

Responsibilities:
    - Generate CSV files
    - Save reports folder

Input:
    Parsed data list

Output:
    CSV report file

Notes:
    Reusable exporter.
"""
import csv
from pathlib import Path
from datetime import datetime


def export_csv(
        data,
        report_name):
    """
    Export parsed data to CSV
    """

    if not data:

        print(
            "\n❌ No data to export"
        )

        return

    # -----------------------------------
    # Create reports folder
    # -----------------------------------
    reports_dir = Path(
        "reports"
    )

    reports_dir.mkdir(
        exist_ok=True
    )

    # -----------------------------------
    # File name
    # -----------------------------------
    timestamp = (
        datetime.now()
        .strftime(
            "%Y%m%d_%H%M%S"
        )
    )

    filename = (
        reports_dir
        /
        f"{report_name}_"
        f"{timestamp}.csv"
    )

    try:

        fieldnames = (
            data[0].keys()
        )

        with open(
            filename,
            mode="w",
            newline="",
            encoding="utf-8"
        ) as csv_file:

            writer = (
                csv.DictWriter(
                    csv_file,
                    fieldnames=fieldnames
                )
            )

            writer.writeheader()

            writer.writerows(
                data
            )

        print(
            f"\n✅ Report exported:"
        )

        print(filename)

    except Exception as e:

        print(
            f"\n❌ Failed to "
            f"export report: {e}"
        )