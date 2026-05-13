"""
Add all issues in the repo to a GitHub Project.

Usage:
  python add-all-issues-to-project.py --owner cmnorotsky --repo gh-role-based-academy --project-title "Academy - All Roles"
"""
import argparse
import json
import subprocess


def run(cmd, check=True):
    result = subprocess.run(cmd, capture_output=True, text=True)
    if check and result.returncode != 0:
        raise RuntimeError(result.stderr.strip())
    return result.stdout.strip()


def get_project_number(owner, title):
    raw = run(["gh", "project", "list", "--owner", owner, "--format", "json", "--limit", "200"])
    data = json.loads(raw)
    for project in data.get("projects", []):
        if project.get("title") == title:
            return project.get("number")
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--owner", required=True)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--project-title", required=True)
    args = parser.parse_args()

    project_number = get_project_number(args.owner, args.project_title)
    if project_number is None:
        raise RuntimeError("Project not found")

    raw = run([
        "gh",
        "issue",
        "list",
        "--repo",
        f"{args.owner}/{args.repo}",
        "--state",
        "all",
        "--limit",
        "500",
        "--json",
        "url",
    ])
    issues = json.loads(raw)
    for item in issues:
        run([
            "gh",
            "project",
            "item-add",
            str(project_number),
            "--owner",
            args.owner,
            "--url",
            item["url"],
        ], check=False)


if __name__ == "__main__":
    main()
