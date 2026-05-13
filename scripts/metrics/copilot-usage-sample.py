"""
Copilot usage sample report (dry-run by default).
Usage: python copilot-usage-sample.py --input samples/migration-data/sample-copilot-metrics.csv --dry-run
"""
import argparse
import csv

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=False, default="samples/migration-data/sample-copilot-metrics.csv")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    with open(args.input, newline="") as handle:
        rows = list(csv.DictReader(handle))

    if args.dry_run:
        print(f"Dry run: loaded {len(rows)} rows")
        return

    # TODO: Generate metrics report.
    print("TODO: generate copilot usage report")

if __name__ == "__main__":
    main()
