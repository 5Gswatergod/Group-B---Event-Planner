"""
Purpose of this file:
- Provides the main interface for the Event Planner application.

Features:
- Display a menu for the user to add, view, update and remove events from the list.
- Validates user's inputs before creating / modifying events.

Authors: Group B
Date: 2026-04-15
"""

import os

from Event import Event
from storage import save_event, load_event, eventToDict

FILE_PATH = "./data/saved_events.txt"

def display_list(events: list[Event]) -> None:
    """Print the current event list in a numbered format."""
    if not events:
        print("Current No Events.")
    else:
        for index, event in enumerate(events, start=1):
            print(f"{index}. {event}")

def _is_valid_string(string: str) -> bool | None:
    if isinstance(string, str) and string.strip() != "":
        return True

def _is_valid_date_string(new_date: str) -> bool | None:
    if len(new_date) == 8 and new_date.isdigit():
        return True

def get_valid_name() -> str:
    while True:
        name = input("Enter Event Name: ")
        if _is_valid_string(name):
            return name
        print("Invalid Name. Enter Again.")

def get_valid_date() -> str:
    while True:
        date = input("Enter Event Date: (YYYYMMDD)")
        if _is_valid_date_string(date):
            return date
        print("Invalid date. Enter Again.")

def get_event_index(events: list[Event]) -> int:
    display_list(events)
    return int(input("Enter The event index: ")) - 1

def get_valid_status() -> bool:
    while True:
        status = input("Upcoming OR Past? (u/p)").lower()
        if status == "u":
            return True
        if status == "p":
            return False
        print("Invalid input. Enter 'u' or 'p'.")

def main() -> None:
    # Create the data file if it does not exist.
    if not os.path.exists(FILE_PATH):
        open(FILE_PATH, "w").close()

    # Load saved events from file and convert each dict to an Event object.
    events = [Event(d["name"], d["date"], d["status"]) for d in load_event(FILE_PATH)]

    while True:
        print("\n--- Event Planner ---")
        print("1. Add Event")
        print("2. View All Events")
        print("3. Mark Event Status")
        print("4. Remove Event")
        print("5. Exit")

        choice = input("Choose an Option: ")
        
        # Collect input then append to list
        if choice == "1":
            event_name = get_valid_name()
            event_date = get_valid_date()
            event_status = get_valid_status()

            new_event = Event(event_name, event_date, event_status)
            events.append(new_event)

        elif choice == "2":
            display_list(events)

        elif choice == "3":
            if not events:
                print("Current No Events.")
            else:
                try:
                    # Get the target event and update its status.
                    events[get_event_index(events)].status = get_valid_status()
                    print("Status Updated.")
                except (ValueError, IndexError):
                    print("Invalid input.")

        elif choice == "4":
            if not events:
                print("Current No Events.")
            else:
                try:
                    events.pop(get_event_index(events))
                    print("Event Removed.")
                except (ValueError, IndexError):
                    print("Invalid input.")
        
        # Save before exit is handled in choice 5
        elif choice == "5":
            save_event(FILE_PATH, eventToDict(events))
            print("Goodbye.")
            break

if __name__ == "__main__":
    main()
