# Event Planner Scope

## Project Overview
Event Planner is a single-user, local, command-line application for managing personal events.  
The product is intentionally limited to a reliable MVP: CRUD operations, date-sorted viewing, and JSON file persistence.

## Target User(s)
- One personal user (student-level use).
- No account system.
- No collaboration or shared event ownership.

## Functional Requirements (Must-have Features)
- Add an event.
- View events sorted by date (ascending).
- Edit an existing event by ID.
- Delete an existing event by ID.
- Persist all event changes to a local JSON file.

## Event Record Contract
- `id: int`
- `name: str` (required)
- `date: str` (required, strict `YYYY-MM-DD`)
- `location: str` (required)
- `description: str` (optional, default `""`)

## Validation Requirements
- `name`, `date`, and `location` cannot be empty.
- `date` must match strict ISO date format `YYYY-MM-DD`.
- Invalid or impossible dates (for example `2026-02-30`) are rejected with clear CLI error messages.

## Non-Functional Requirements (Constraints)
- Fully offline local usage.
- Python standard library only.
- Menu-prompt CLI interaction model.
- Error messages should be clear and actionable for user input mistakes.

## Out-of-Scope Features
- Multi-user support.
- Authentication/authorization.
- Reminders/notifications.
- Recurring events.
- Conflict detection.
- GUI or web interface.
- Cloud sync.
- Flexible date parsing (only strict `YYYY-MM-DD` is supported).

## Deliverables
- Updated scope documentation in `SCOPE.md`.
- Updated project documentation in `README.md`.
- README implementation checklist with this ordered task sequence:
  1. Create JSON storage loader/saver.
  2. Implement CRUD service functions.
  3. Build interactive menu loop.
  4. Add input/date validation.
  5. Add unit tests for core behavior.
  6. Document run/test commands.

## Runtime Assumptions
- Runtime data file: `data/events.json`.
- `data/template.json` remains an example/reference file.
- Date handling is date-only (no time or timezone logic in v1).
