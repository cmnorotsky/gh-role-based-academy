"""
GHAS alert summary report (dry-run by default).
Usage: python ghas-alert-summary.py --input samples/migration-data/sample-ghas-alerts.csv --dry-run
"""
import argparse
import csv

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=False, default="samples/migration-data/sample-ghas-alerts.csv")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    with open(args.input, newline="") as handle:
        rows = list(csv.DictReader(handle))

    if args.dry_run:
        print(f"Dry run: loaded {len(rows)} rows")
        return

    # TODO: Summarize alerts by severity and status.
    print("TODO: generate GHAS alert summary")

if __name__ == "__main__":
    main()
