---
name: project-pawpal-state
description: Current build state of PawPal+ — what exists, what is stub-only, and what is missing as of 2026-06-21
metadata:
  type: project
---

PawPal+ is an in-progress Streamlit pet care task planner. As of 2026-06-21 the project has two source files:

- `app.py` — thin Streamlit demo shell; UI collects owner name, pet name, species, and a simple task list in session state. "Generate schedule" button is not wired to any logic.
- `pawpal_system.py` — four class skeletons (Task, Pet, Owner, Schedule) with `uuid`-based IDs. Every method body is `pass` (TODO stubs only).

**Why:** This is a CodePath AI110 module 2 assignment. The student designs UML, writes class skeletons, then implements scheduling logic and connects it to the Streamlit UI.

**How to apply:** When suggesting implementations, start from the stub methods in `pawpal_system.py` and wire results into `app.py`. Do not assume any logic is already running.

Key design gaps identified (see code review 2026-06-21):
- No owner ↔ pet back-reference (Pet has no `owner_id`)
- No Schedule ↔ Owner link
- Tasks in app.py are plain dicts, not Task objects — they will not match pawpal_system.py
- All method bodies are pass; return-type contracts are broken (get_pending_tasks returns None, not list)
- Schedule.generate() takes a separate task list instead of reading from Pet.task_list
- No priority validation (UML says int, no range defined)
