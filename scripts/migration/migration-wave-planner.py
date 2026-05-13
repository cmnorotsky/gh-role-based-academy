"""
Migration wave planner (dry-run by default).
Usage: python migration-wave-planner.py --input samples/migration-data/sample-repo-inventory.csv --dry-run
"""
import argparse
import csv

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    with open(args.input, newline="") as handle:
        rows = list(csv.DictReader(handle))

    if args.dry_run:
        print(f"Dry run: loaded {len(rows)} rows")
        return

    # TODO: Add wave planning logic.
    print("TODO: generate migration waves")

if __name__ == "__main__":
    main()
