"""
Setup academy automation.
- Create labels and milestones.
- Create issues from backlog markdown files.
- Create role-based GitHub Projects and add issues by role label.

Usage:
  python setup-academy.py --owner cmnorotsky --repo gh-role-based-academy \
    --projects app-dev,infra,devops,security,qa,ba-product,architect,manager,ai-coach \
    --visibility private
"""
import argparse
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LABELS_FILE = ROOT / "project" / "labels.md"
MILESTONES_FILE = ROOT / "project" / "milestones.md"
BACKLOG_FILES = [
    ROOT / "project" / "issue-backlog.md",
    ROOT / "project" / "issue-backlog-seed.md",
]


def run(cmd, check=True):
    result = subprocess.run(cmd, capture_output=True, text=True)
    if check and result.returncode != 0:
        raise RuntimeError(result.stderr.strip())
    return result.stdout.strip()


def parse_list_items(path):
    items = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("- "):
            items.append(line[2:].strip())
    return items


def create_labels(owner, repo):
    labels = parse_list_items(LABELS_FILE)
    for label in labels:
        run([
            "gh",
            "label",
            "create",
            label,
            "--repo",
            f"{owner}/{repo}",
            "--color",
            "ededed",
            "--description",
            "academy label",
        ], check=False)


def create_milestones(owner, repo):
    milestones = parse_list_items(MILESTONES_FILE)
    for milestone in milestones:
        run([
            "gh",
            "api",
            f"repos/{owner}/{repo}/milestones",
            "-f",
            f"title={milestone}",
        ], check=False)


def parse_issues(path):
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    issues = []
    milestone = None
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("## "):
            milestone = line[3:].strip()
        if line.startswith("### "):
            title = line[4:].strip()
            body_lines = []
            i += 1
            while i < len(lines) and not lines[i].startswith("### "):
                if lines[i].startswith("## "):
                    break
                body_lines.append(lines[i])
                i += 1
            body = "\n".join(body_lines).strip()
            issues.append({"title": title, "body": body, "milestone": milestone})
            continue
        i += 1
    return issues


def labels_from_body(body):
    labels = []
    track = re.search(r"^Track:\s*(.+)$", body, re.MULTILINE)
    role = re.search(r"^Role:\s*(.+)$", body, re.MULTILINE)
    cert = re.search(r"^Certification:\s*(.+)$", body, re.MULTILINE)
    labels_line = re.search(r"^Labels:\s*(.+)$", body, re.MULTILINE)

    if labels_line:
        labels.extend([l.strip() for l in labels_line.group(1).split(",") if l.strip()])
    if track:
        labels.append(f"track:{track.group(1).strip()}")
    if role:
        for r in role.group(1).split(","):
            role_value = r.strip()
            if role_value == "all":
                labels.append("role:all")
            else:
                labels.append(f"role:{role_value}")
    if cert:
        labels.append(f"cert:{cert.group(1).strip()}")

    # Normalize label spacing
    labels = [l.replace(" ", "-") for l in labels]
    return sorted(set(labels))


def create_issues(owner, repo):
    seen = set()
    for path in BACKLOG_FILES:
        if not path.exists():
            continue
        for issue in parse_issues(path):
            if issue["title"] in seen:
                continue
            seen.add(issue["title"])
            if issue_exists(owner, repo, issue["title"]):
                continue
            labels = labels_from_body(issue["body"])
            cmd = [
                "gh",
                "issue",
                "create",
                "--repo",
                f"{owner}/{repo}",
                "--title",
                issue["title"],
                "--body",
                issue["body"],
            ]
            if labels:
                cmd.extend(["--label", ",".join(labels)])
            if issue["milestone"]:
                cmd.extend(["--milestone", issue["milestone"]])
            run(cmd)


def create_role_projects(owner, roles):
    for role in roles:
        title = f"Academy - role:{role}"
        run([
            "gh",
            "project",
            "create",
            "--owner",
            owner,
            "--title",
            title,
        ], check=False)


def get_project_number(owner, title):
    raw = run(["gh", "project", "list", "--owner", owner, "--format", "json"])
    data = json.loads(raw)
    projects = data.get("projects", [])
    for project in projects:
        if project.get("title") == title:
            return project.get("number")
    return None


def issue_exists(owner, repo, title):
    raw = run([
        "gh",
        "issue",
        "list",
        "--repo",
        f"{owner}/{repo}",
        "--search",
        f'"{title}" in:title',
        "--json",
        "title",
        "--limit",
        "50",
    ])
    items = json.loads(raw)
    return any(item.get("title") == title for item in items)


def add_issues_to_projects(owner, roles):
    for role in roles:
        title = f"Academy - role:{role}"
        project_number = get_project_number(owner, title)
        if project_number is None:
            continue
        raw = run([
            "gh",
            "issue",
            "list",
            "--repo",
            f"{owner}/gh-role-based-academy",
            "--label",
            f"role:{role},role:all",
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
                owner,
                "--url",
                item["url"],
            ], check=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--owner", required=True)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--projects", required=True)
    parser.add_argument("--visibility", default="private")
    args = parser.parse_args()

    roles = [r.strip() for r in args.projects.split(",") if r.strip()]

    create_labels(args.owner, args.repo)
    create_milestones(args.owner, args.repo)
    create_issues(args.owner, args.repo)
    create_role_projects(args.owner, roles)
    add_issues_to_projects(args.owner, roles)


if __name__ == "__main__":
    main()
