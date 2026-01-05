#!/usr/bin/env python3
"""
Create one GitHub Issue per FRE 521D lecture using GitHub CLI (gh), no token needed.

Repo: https://github.com/aaneloy/FRE521D-Winter2026-UBC

Prereqs (one-time):
  gh auth login

Run:
  python create_lecture_issues_gh.py
  python create_lecture_issues_gh.py --schedule FRE521D_Schedule.md --dry-run
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Dict, List, Optional, Set


API_REPO = "aaneloy/FRE521D-Winter2026-UBC"

MONTHS = {
    "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
    "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
}


@dataclass
class LectureRow:
    lecture_no: int
    week: int
    dt: date
    day: str
    topic_title: str
    topic_details: str
    deliverables: str


def run_gh(args: List[str], capture: bool = True) -> str:
    cmd = ["gh"] + args
    try:
        r = subprocess.run(
            cmd,
            check=True,
            text=True,
            capture_output=capture
        )
        return (r.stdout or "").strip()
    except FileNotFoundError:
        raise RuntimeError("GitHub CLI (gh) not found. Install gh and run: gh auth login")
    except subprocess.CalledProcessError as e:
        out = (e.stdout or "").strip()
        err = (e.stderr or "").strip()
        msg = "\n".join([s for s in [out, err] if s])
        raise RuntimeError(f"gh command failed: {' '.join(cmd)}\n{msg}")


def gh_json(args: List[str]) -> object:
    out = run_gh(args, capture=True)
    if not out:
        return []
    return json.loads(out)


def ensure_gh_auth() -> None:
    # exits non-zero if not logged in
    run_gh(["auth", "status"], capture=True)


def clean_md(text: str) -> str:
    t = text.strip()
    t = t.replace("–", "-").replace("—", "-")
    t = re.sub(r"\*\*(.*?)\*\*", r"\1", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def parse_month_day(s: str, year: int = 2026) -> date:
    s = s.strip()
    parts = s.split()
    if len(parts) != 2:
        raise ValueError(f"Unexpected date format: {s!r}")
    mon, day_s = parts
    if mon not in MONTHS:
        raise ValueError(f"Unknown month: {mon!r}")
    return date(year, MONTHS[mon], int(day_s))


def parse_schedule_markdown(md: str) -> List[LectureRow]:
    lines = md.splitlines()

    start_idx = None
    for i, line in enumerate(lines):
        if line.strip() == "## Weekly Schedule":
            start_idx = i
            break
    if start_idx is None:
        raise ValueError("Could not find '## Weekly Schedule' section.")

    table_start = None
    for i in range(start_idx, len(lines)):
        if lines[i].lstrip().startswith("| Week"):
            table_start = i
            break
    if table_start is None:
        raise ValueError("Could not find the weekly schedule table header.")

    table_lines: List[str] = []
    for i in range(table_start, len(lines)):
        line = lines[i]
        if not line.strip():
            if table_lines:
                break
            continue
        if not line.lstrip().startswith("|"):
            if table_lines:
                break
            continue
        table_lines.append(line)

    if len(table_lines) < 3:
        raise ValueError("Weekly schedule table seems too short.")

    data_lines = table_lines[2:]  # skip header + separator

    lectures: List[LectureRow] = []
    current_week: Optional[int] = None
    lecture_no = 0

    for raw in data_lines:
        parts = [c.strip() for c in raw.split("|")]
        if len(parts) < 7:
            continue

        week_cell, date_cell, day_cell, topic_cell, deliv_cell = parts[1:6]
        week_cell = clean_md(week_cell)
        date_cell = clean_md(date_cell)
        day_cell = clean_md(day_cell)
        topic_cell = clean_md(topic_cell)
        deliv_cell = clean_md(deliv_cell)

        if week_cell:
            wk = int(re.sub(r"[^\d]", "", week_cell))
            current_week = wk
        if current_week is None:
            raise ValueError("Week number missing before the first lecture row.")

        if not date_cell or not day_cell or not topic_cell:
            continue

        lecture_no += 1

        if " - " in topic_cell:
            topic_title, topic_details = topic_cell.split(" - ", 1)
        else:
            topic_title, topic_details = topic_cell, ""

        lectures.append(
            LectureRow(
                lecture_no=lecture_no,
                week=current_week,
                dt=parse_month_day(date_cell, year=2026),
                day=day_cell,
                topic_title=topic_title.strip(),
                topic_details=topic_details.strip(),
                deliverables=deliv_cell.strip(),
            )
        )

    if not lectures:
        raise ValueError("No lectures parsed from the weekly schedule table.")
    return lectures


def build_issue_title(lec: LectureRow) -> str:
    return f"Lecture {lec.lecture_no:02d} ({lec.dt.isoformat()} {lec.day}): {lec.topic_title}"


def build_issue_body(lec: LectureRow) -> str:
    deliverables = lec.deliverables if lec.deliverables else "None listed"
    details = lec.topic_details if lec.topic_details else "N/A"

    return (
        "## Lecture details\n"
        f"- Week: {lec.week}\n"
        f"- Date: {lec.dt.isoformat()} ({lec.day})\n"
        f"- Topic: {lec.topic_title}\n"
        f"- Details: {details}\n"
        f"- Deliverables: {deliverables}\n\n"
        "## Content to upload\n"
        "- [ ] Slides (PDF)\n"
        "- [ ] Lecture notes (Markdown)\n"
        "- [ ] Code (notebook or scripts)\n"
        "- [ ] Data files or links (if any)\n"
        "- [ ] Readings or references\n"
        "- [ ] Recording link (if available)\n"
        "- [ ] Canvas updates (Modules, Announcements)\n\n"
        "## Suggested repo structure\n"
        f"- [ ] Create or update: lectures/week-{lec.week:02d}/lecture-{lec.lecture_no:02d}/\n"
        "- [ ] Add: slides.pdf, notes.md, code/, data/ (optional)\n"
    )


def list_existing_issue_titles(repo: str) -> Set[str]:
    items = gh_json(["issue", "list", "--repo", repo, "--state", "all", "--limit", "2000", "--json", "title"])
    titles: Set[str] = set()
    for it in items:
        t = it.get("title")
        if t:
            titles.add(t)
    return titles


def list_labels(repo: str) -> Set[str]:
    items = gh_json(["label", "list", "--repo", repo, "--limit", "500", "--json", "name"])
    names: Set[str] = set()
    for it in items:
        n = it.get("name")
        if n:
            names.add(n)
    return names


def ensure_labels(repo: str, lectures: List[LectureRow]) -> None:
    existing = list_labels(repo)

    needed: List[Dict[str, str]] = []
    needed.append({"name": "lecture", "color": "1f6feb", "description": "Lecture content upload tracker"})

    for wk in sorted({l.week for l in lectures}):
        needed.append({"name": f"week-{wk:02d}", "color": "c5def5", "description": f"Week {wk} lectures"})

    for lab in needed:
        if lab["name"] in existing:
            continue
        run_gh([
            "label", "create", lab["name"],
            "--repo", repo,
            "--color", lab["color"],
            "--description", lab["description"]
        ], capture=True)


def create_issue(repo: str, title: str, body: str, labels: List[str], dry_run: bool) -> None:
    if dry_run:
        print(f"[DRY-RUN] {title} | labels={labels}")
        return

    with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".md") as f:
        f.write(body)
        body_path = f.name

    try:
        args = ["issue", "create", "--repo", repo, "--title", title, "--body-file", body_path]
        for lab in labels:
            args += ["--label", lab]
        out = run_gh(args, capture=True)
        print(f"[CREATED] {title}")
        if out:
            print(f"          {out}")
    finally:
        try:
            os.remove(body_path)
        except OSError:
            pass


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=API_REPO, help="owner/repo")
    ap.add_argument("--schedule", default="FRE521D_Schedule.md", help="path to schedule markdown")
    ap.add_argument("--dry-run", action="store_true", help="print actions without creating issues")
    ap.add_argument("--no-labels", action="store_true", help="do not create/apply labels")
    args = ap.parse_args()

    ensure_gh_auth()

    schedule_path = Path(args.schedule)
    if not schedule_path.exists():
        print(f"Schedule file not found: {schedule_path}", file=sys.stderr)
        return 2

    md = schedule_path.read_text(encoding="utf-8")
    lectures = parse_schedule_markdown(md)

    existing_titles = list_existing_issue_titles(args.repo)

    if not args.no_labels:
        ensure_labels(args.repo, lectures)

    created = 0
    skipped = 0

    for lec in lectures:
        title = build_issue_title(lec)
        if title in existing_titles:
            print(f"[SKIP] {title}")
            skipped += 1
            continue

        body = build_issue_body(lec)
        labels = [] if args.no_labels else ["lecture", f"week-{lec.week:02d}"]
        create_issue(args.repo, title, body, labels, dry_run=args.dry_run)
        created += 1

    print(f"\nDone. Created: {created} | Skipped: {skipped} | Total lectures: {len(lectures)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
