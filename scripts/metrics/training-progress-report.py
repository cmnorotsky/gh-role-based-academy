"""
Training progress report (dry-run by default).
Usage: python training-progress-report.py --dry-run
"""
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if args.dry_run:
        print("Dry run: no data source configured")
        return

    # TODO: Fetch issues and summarize by label.
    print("TODO: generate training progress report")

if __name__ == "__main__":
    main()
