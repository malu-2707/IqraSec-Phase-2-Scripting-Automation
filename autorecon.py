#!/usr/bin/env python3
"""AutoRecon Lite - Authorized reconnaissance automation."""

import argparse
import ipaddress
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def validate_target(target):
    """Accept valid IP addresses or syntactically valid hostnames."""
    if not target or target != target.strip() or len(target) > 253:
        return False

    try:
        ipaddress.ip_address(target)
        return True
    except ValueError:
        pass

    # A dotted string made entirely of numeric labels should be a valid IP,
    # not a hostname. Reject it when IP parsing fails.
    labels = target.split(".")
    if len(labels) == 4 and all(label.isdigit() for label in labels):
        return False

    # Validate hostname labels.
    if target.endswith("."):
        target = target[:-1]

    if not target:
        return False

    labels = target.split(".")
    for label in labels:
        if (
            not label
            or len(label) > 63
            or label.startswith("-")
            or label.endswith("-")
            or not all(ch.isalnum() or ch == "-" for ch in label)
        ):
            return False

    return True

def main():
    parser = argparse.ArgumentParser(
        description="Automate basic reconnaissance in an authorized lab."
    )
    parser.add_argument(
        "--target",
        required=True,
        help="Authorized target IP address or hostname",
    )
    parser.add_argument(
        "--output",
        default="reports",
        help="Directory for scan results (default: reports)",
    )
    args = parser.parse_args()

    if not validate_target(args.target):
        parser.error("Invalid target IP address or hostname.")

    nmap = shutil.which("nmap")
    if not nmap:
        print("Error: Nmap is not installed or not in PATH.", file=sys.stderr)
        return 2

    output_dir = Path(args.output)
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        print(f"Error creating output directory: {exc}", file=sys.stderr)
        return 2

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    safe_target = "".join(
        char if char.isalnum() or char in ".-_" else "_" for char in args.target
    )
    prefix = output_dir / f"{safe_target}_{timestamp}"
    text_file = Path(f"{prefix}.txt")
    xml_file = Path(f"{prefix}.xml")
    report_file = prefix.with_name(prefix.name + "_report.md")

    command = [
        nmap,
        "-sV",
        "-T3",
        "--top-ports",
        "1000",
        "-oN",
        str(text_file),
        "-oX",
        str(xml_file),
        args.target,
    ]

    print(f"Target: {args.target}")
    print("Running Nmap service enumeration...")
    print("Only run this tool against systems you are authorized to assess.")

    try:
        result = subprocess.run(command, check=False, timeout=900)
    except subprocess.TimeoutExpired:
        print("Error: Scan timed out after 15 minutes.", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"Error running Nmap: {exc}", file=sys.stderr)
        return 1

    if result.returncode != 0:
        print(f"Nmap exited with status {result.returncode}.", file=sys.stderr)
        return result.returncode or 1

    try:
        scan_output = text_file.read_text(encoding="utf-8", errors="replace")
        report = (
            "# AutoRecon Lite — Scan Report\n\n"
            f"- **Target:** `{args.target}`\n"
            f"- **UTC time:** {datetime.now(timezone.utc).isoformat()}\n"
            "- **Scan:** Nmap service/version detection, top 1000 TCP ports\n"
            "- **Scope:** Authorized assessment only\n\n"
            "## Raw scan results\n\n"
            "```text\n"
            f"{scan_output.rstrip()}\n"
            "```\n"
        )
        report_file.write_text(report, encoding="utf-8")
    except OSError as exc:
        print(f"Scan completed, but report generation failed: {exc}", file=sys.stderr)
        return 1

    print("\nScan completed successfully.")
    print(f"Text results: {text_file}")
    print(f"XML results:  {xml_file}")
    print(f"Markdown report: {report_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
