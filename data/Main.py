'''
Purpose of this file:
- Provides the main interface for the Event Planner application.

Features:
- Display a menu for the user to add, view, update and remove events from the list.
- Validates user's inputs before creating / modifying events.

Authors: Group B
Date: 2026-04-15
'''

import os
from Event import Event
from Storage import save_event, load_event

FILE_PATH = "saved_events.txt"

def _save_all(events):
    '''
    Overwrites saved_events.txt with the current full list of events.
    Called after removing an event or updating an event's status.

    Parameters:
        events (list): list of Event objects to be saved.

    Returns:
        None
    '''

    events_dicts = []

    for e in events:
        events_dicts.append({"name": e.name, "date": e.date, "status": e.status})
    with open(FILE_PATH, "w") as f:
        f.write(str(events_dicts) + "\n")

# Display a summary
def display_list(events):
    if not events:
        print("Current No Events.")
    else:
        for i in range(len(events)):
            print(f"{i+1}. {events[i]}")

# Helper Methods
def _is_valid_string(string):
    if isinstance(string, str) and string.strip() != "":
        return True

def _is_valid_date_string(new_date):
    if len(new_date) == 8 and new_date.isdigit():
        return True

# Get Inputs from the User and Validates
def get_valid_name():
    while True:
        name = input("Enter Event Name: ")
        if _is_valid_string(name):
            return name
        print("Invalid Name. Enter Again.")

def get_valid_date():
    while True:
        date = input("Enter Event Date: (YYYYMMDD)")
        if _is_valid_date_string(date):
            return date
        print("Invalid date. Enter Again.")

def get_event_index(events):
    display_list(events)
    return int(input("Enter The event index: ")) - 1

def get_valid_status():
    while True:
        status = input("Upcoming OR Past? (u/p)").lower()
        if status == "u":
            return True
        elif status == "p":
            return False
        print("Invalid input. Enter 'u' or 'p'.")

def main():
    # Create the data file if doesn not exist
    if not os.path.exists(FILE_PATH):
        open(FILE_PATH, "w").close()

    # Load saved events from file, 
    # and convert each dict to an Event Object
    events = [Event(d["name"], d["date"], d["status"]) for d in load_event(FILE_PATH)]

    # Interface
    while True:
        print("\n--- Event Planner ---")
        print("1. Add Event")
        print("2. View All Events")
        print("3. Mark Event Status")
        print("4. Remove Event")
        print("5. Exit")

        choice = input("Choose an Option: ")

            # Add Event
        if choice == "1":
            event_name = get_valid_name()
            event_date = get_valid_date()
            event_status = get_valid_status()

            new_event = Event(event_name, event_date, event_status)
            events.append(new_event)
            save_event(FILE_PATH, {"name": new_event.name, "date": new_event.date, "status": new_event.status})

            # View All Events
        elif choice == "2":
            display_list(events)

            # Mark Event Status
        elif choice == "3":
            if len(events) == 0:
                print("Current No Events.")
            else:
                try:
                    # Get the object event, and update its status
                    events[get_event_index(events)].status = get_valid_status()
                    print("Status Updated.")
                    _save_all(events)
                except (ValueError, IndexError):
                    print("Invalid input.")

            # Remove Event
        elif choice == "4":
            if len(events) == 0:
                print("Current No Events.")
            else:
                try:
                    events.pop(get_event_index(events))
                    print("Event Removed.")
                    _save_all(events)
                except (ValueError, IndexError):
                    print("Invalid input.")

            # Quit
        elif choice == "5":
            print("Goodbye.")
            break

if __name__ == "__main__":
    main()
