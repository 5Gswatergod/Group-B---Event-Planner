# Event Planner

## Description

A single-user, local, menu-driven command-line Event Planner (v1).

This program focuses on:
- Basic CRUD(Create, Read, Update, and Delet) for events.
- Date-sorted event listing.
- JSON file persistence.
- Clear input validation and error messages.

## How to Run

Planned runtime entry command:

```bash
python -m src.main
```

## Example input/output

### Main menu
```text
1. Add Event
2. View Events
3. Edit Event
4. Delete Event
5. Exit
```

### Example event record
```json
{
  "id": 1,
  "name": "Math Club Meeting",
  "date": "2026-05-08",
  "location": "Room 201",
  "description": "Prepare contest questions"
}
```

## In the Scope

- Add an event.
- View events sorted by date ascending.
- Edit an event by ID.
- Delete an event by ID.
- Persist all changes in `data/events.json`.

## Data Model

Event contract:
- `id: int`
- `name: str` (required)
- `date: str` (required, strict `YYYY-MM-DD`)
- `location: str` (required)
- `description: str` (optional, defaults to empty string)

Storage expectations:
- Runtime data file: `data/events.json`.
- `data/template.json` is a reference example, not the runtime store.

## Validation Rules

- Required fields: `name`, `date`, `location` must be non-empty.
- `date` must be strict ISO format `YYYY-MM-DD`.
- Invalid dates (including impossible calendar dates) are rejected with clear CLI errors.

## Implementation Checklist

1. Create JSON storage loader/saver.
2. Implement CRUD service functions.
3. Build interactive menu loop.
4. Add input/date validation.
5. Add unit tests for core behavior.
6. Document run/test commands.

## Test Plan

Target scenarios:
- Add event with valid required fields is saved to JSON.
- List events is sorted by date ascending.
- Edit updates only the selected ID.
- Delete removes only the selected ID.
- Missing required fields are rejected.
- Invalid date format or impossible date is rejected.
- Storage initializes safely when data file is missing or empty.

Planned test command:

```bash
python -m unittest discover -s test -p "test_*.py"
```
