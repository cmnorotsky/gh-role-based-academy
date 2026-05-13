"""
Repo health score calculator (dry-run by default).
Usage: python repo-health-score.py --input samples/migration-data/sample-repo-inventory.csv --dry-run
"""
import argparse
import csv

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=False, default="samples/migration-data/sample-repo-inventory.csv")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    with open(args.input, newline="") as handle:
        rows = list(csv.DictReader(handle))

    if args.dry_run:
        print(f"Dry run: loaded {len(rows)} rows")
        return

    # TODO: Calculate a health score.
    print("TODO: generate repo health score")

if __name__ == "__main__":
    main()
