from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Callable

if __package__ in (None, ""):
    project_root = Path(__file__).resolve().parents[1]
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

from src_backup.service import add_event, delete_event, edit_event, find_event_by_id, list_events


Event = dict[str, Any]


def print_menu():
    print("\nEvent Planner")
    print("1. Add event")
    print("2. View events")
    print("3. Edit event")
    print("4. Delete event")
    print("5. Exit")


def prompt_non_empty(prompt_text: str, field_name: str):
    while True:
        value = input(prompt_text).strip()
        if value:
            return value
        print(f"{field_name} cannot be empty. Please try again.")


def prompt_event_id():
    while True:
        raw_id = input("Enter event ID: ").strip()

        if not raw_id:
            print("ID cannot be empty. Please try again.")
            continue

        if not raw_id.isdigit() or int(raw_id) <= 0:
            print("ID must be a positive integer. Please try again.")
            continue

        return int(raw_id)


def prompt_yes_no(prompt_text: str):
    while True:
        choice = input(prompt_text).strip().lower()

        if not choice:
            print("Response cannot be empty. Enter 'y' or 'n'.")
            continue

        if choice in {"y", "yes"}:
            return True

        if choice in {"n", "no"}:
            return False

        print("Invalid response. Enter 'y' or 'n'.")


def prompt_event_fields(existing: Event | None = None):
    if existing is None:
        name = prompt_non_empty("Name: ", "Name")
        date = prompt_non_empty("Date (YYYY-MM-DD): ", "Date")
        location = prompt_non_empty("Location: ", "Location")
        description = input("Description (optional): ")
        return name, date, location, description

    current_name = str(existing["name"])
    current_date = str(existing["date"])
    current_location = str(existing["location"])
    current_description = str(existing["description"])

    name = input(f"Name [{current_name}]: ").strip() or current_name
    date = input(f"Date [{current_date}] (YYYY-MM-DD): ").strip() or current_date
    location = input(f"Location [{current_location}]: ").strip() or current_location

    shown_description = current_description if current_description else "<empty>"
    description_input = input(
        f"Description [{shown_description}] (Enter to keep, '-' to clear): "
    ).strip()
    if description_input == "-":
        description = ""
    elif description_input == "":
        description = current_description
    else:
        description = description_input

    return name, date, location, description


def print_event(event: Event) -> None:
    description = str(event["description"]).strip() or "<empty>"
    print(f'ID: {event["id"]}')
    print(f'Name: {event["name"]}')
    print(f'Date: {event["date"]}')
    print(f'Location: {event["location"]}')
    print(f"Description: {description}")


def handle_add_event():
    print("\nAdd Event")
    name, date, location, description = prompt_event_fields()
    created = add_event(name=name, date=date, location=location, description=description)
    print("\nEvent added successfully.")
    print_event(created)


def handle_view_events():
    print("\nAll Events")
    events = list_events()

    if not events:
        print("No events found.")
        return

    for index, event in enumerate(events, start=1):
        print(f"\n[{index}]")
        print_event(event)


def handle_edit_event():
    print("\nEdit Event")
    event_id = prompt_event_id()
    existing = find_event_by_id(event_id)

    if existing is None:
        raise ValueError(f"Event with ID {event_id} was not found.")

    name, date, location, description = prompt_event_fields(existing)
    updated = edit_event(
        event_id=event_id,
        name=name,
        date=date,
        location=location,
        description=description,
    )

    print("\nEvent updated successfully.")
    print_event(updated)


def handle_delete_event():
    print("\nDelete Event")
    event_id = prompt_event_id()

    confirm = prompt_yes_no(f"Delete event ID {event_id}? (y/n): ")
    if not confirm:
        print("Delete cancelled.")
        return

    deleted = delete_event(event_id)
    print("\nEvent deleted successfully.")
    print_event(deleted)


def run_cli():
    handlers: dict[str, Callable[[], None]] = {
        "1": handle_add_event,
        "2": handle_view_events,
        "3": handle_edit_event,
        "4": handle_delete_event,
    }

    while True:
        print_menu()

        try:
            choice = input("Choose an option (1-5): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            return

        if not choice:
            print("Choice cannot be empty. Please try again.")
            continue

        if choice == "5":
            print("Goodbye.")
            return

        handler = handlers.get(choice)
        if handler is None:
            print("Invalid option. Please enter a number from 1 to 5.")
            continue

        try:
            handler()
        except ValueError as exc:
            print(f"Error: {exc}")
        except (EOFError, KeyboardInterrupt):
            print("\nAction cancelled.")


if __name__ == "__main__":
    run_cli()
