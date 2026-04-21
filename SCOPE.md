# Event Planner Scope

## Project Overview

The Event Planner is a command-line Python application that helps users keep a simple list of events. Each event stores a name, a date in `YYYYMMDD` format, and a status showing whether the event is upcoming or past.

The program loads saved events when it starts, lets the user manage the list through a menu, and saves the updated list to `./data/saved_events.txt` when the user exits.

## Target User(s)

- Students or individuals who need a lightweight way to track events.
- Users who are comfortable running a Python program from the terminal.
- Group project evaluators who need to review basic Python class, file storage, validation, and menu-flow functionality.

## Functional Requirements (Must-have Features)

- Display a terminal menu with options to add, view, update, remove, and exit.
- Add a new event with:
  - event name
  - event date
  - event status
- Validate that event names are not empty.
- Validate that event dates are real dates in `YYYYMMDD` format.
- Let users choose event status as upcoming or past using `u` or `p`.
- Display all saved events in a numbered list.
- Format displayed events as `[Upcoming] Name - YYYY / MM / DD` or `[Past] Name - YYYY / MM / DD`.
- Mark an existing event as upcoming or past.
- Remove an existing event by selecting its numbered index.
- Show a clear message when there are no events.
- Handle invalid event index input without crashing.
- Create the data file if it does not already exist.
- Load event data from a `.txt` file.
- Save event data back to a `.txt` file.
- Convert `Event` objects into dictionaries for storage.

## Non-Functional Requirements (Constraints)

- The application must run in Python from the command line.
- Event data must be stored locally in `./data/saved_events.txt`.
- Storage files must use the `.txt` extension.
- The project should remain small and readable, with separate files for:
  - menu and user interaction logic
  - event data model logic
  - file loading and saving logic
- User input should be checked before creating or modifying events.
- The program should avoid crashing during common invalid input cases.
- The saved data format must preserve each event's `name`, `date`, and `status`.

## Out-of-Scope Features

- Graphical user interface.
- Online accounts, login, or multi-user support.
- Cloud storage or database storage.
- Calendar integration.
- Email, text, or push reminders.
- Event search, filtering, sorting, or categories.
- Event times, locations, descriptions, or guests.
- Automatic date-based status changes.
- Recurring events.
- Importing or exporting calendar files.

## Deliverables

- `src/main.py`: command-line menu, input validation helpers, and main event-management flow.
- `src/event.py`: `Event` class with event fields, status labels, date formatting, and string display.
- `src/storage.py`: functions for converting events to dictionaries, saving events, and loading events.
- `data/saved_events.txt`: local text file used to persist saved event data.
- `README.md`: project description, run instructions, and example input/output.
- `test/test_src.py`: automated tests for event objects, storage behavior, validation helpers, and main menu flows.
- `test/test_plan.md`: testing plan describing the main test cases and expected results.
