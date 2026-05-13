"""
Apply GitHub Project fields to all role-based academy projects.

Usage:
  python apply-project-config.py --owner cmnorotsky
"""
import argparse
import json
import subprocess


def run(cmd, check=True):
    result = subprocess.run(cmd, capture_output=True, text=True)
    if check and result.returncode != 0:
        raise RuntimeError(result.stderr.strip())
    return result.stdout.strip()


FIELDS = [
    {
        "name": "Track",
        "type": "SINGLE_SELECT",
        "options": [
            "foundations",
            "admin",
            "actions",
            "migration",
            "ghas",
            "copilot",
            "aidlc",
            "capstone",
            "ai-coach",
        ],
    },
    {
        "name": "Module",
        "type": "SINGLE_SELECT",
        "options": [
            "orientation",
            "foundations",
            "administration",
            "actions",
            "migration",
            "ghas",
            "copilot",
            "ai-sdlc",
            "capstone",
            "ai-coach",
        ],
    },
    {
        "name": "Role",
        "type": "SINGLE_SELECT",
        "options": [
            "app-dev",
            "infra",
            "devops",
            "security",
            "qa",
            "ba-product",
            "architect",
            "manager",
            "ai-coach",
            "release-manager",
            "all",
        ],
    },
    {
        "name": "Certification",
        "type": "SINGLE_SELECT",
        "options": [
            "foundations",
            "actions",
            "admin",
            "ghas",
            "copilot",
        ],
    },
    {
        "name": "Status",
        "type": "SINGLE_SELECT",
        "options": [
            "ready",
            "in-progress",
            "in-review",
            "done",
            "blocked",
        ],
    },
    {
        "name": "Priority",
        "type": "SINGLE_SELECT",
        "options": [
            "p0",
            "p1",
            "p2",
        ],
    },
    {"name": "Effort", "type": "NUMBER"},
    {"name": "Due date", "type": "DATE"},
    {"name": "Evidence link", "type": "TEXT"},
    {"name": "Reviewer", "type": "TEXT"},
    {"name": "Readiness score", "type": "NUMBER"},
    {
        "name": "Capstone category",
        "type": "SINGLE_SELECT",
        "options": [
            "discovery",
            "migration",
            "governance",
            "security",
            "copilot",
            "ai-sdlc",
            "ai-coach",
            "executive",
        ],
    },
]


def get_projects(owner):
    raw = run(["gh", "project", "list", "--owner", owner, "--format", "json", "--limit", "200"])
    data = json.loads(raw)
    return [p for p in data.get("projects", []) if p.get("title", "").startswith("Academy - role:")]


def get_field_names(owner, project_number):
    raw = run(["gh", "project", "field-list", str(project_number), "--owner", owner, "--format", "json", "--limit", "200"])
    data = json.loads(raw)
    fields = data.get("fields", [])
    return {f.get("name") for f in fields}


def create_field(owner, project_number, field):
    cmd = [
        "gh",
        "project",
        "field-create",
        str(project_number),
        "--owner",
        owner,
        "--name",
        field["name"],
        "--data-type",
        field["type"],
    ]
    if field["type"] == "SINGLE_SELECT":
        cmd.extend(["--single-select-options", ",".join(field["options"])])
    run(cmd, check=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--owner", required=True)
    args = parser.parse_args()

    projects = get_projects(args.owner)
    for project in projects:
        number = project.get("number")
        existing = get_field_names(args.owner, number)
        for field in FIELDS:
            if field["name"] in existing:
                continue
            create_field(args.owner, number, field)


if __name__ == "__main__":
    main()
