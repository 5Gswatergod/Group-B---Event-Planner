"""
Purpose of this file:
- Provides functions to save and load event data to/from a .txt file.

Features:
- Save a single event (as a dict) to a .txt file.
- Load all stored events from a .txt file as a list of dicts.
- Validates file path and event structure before any read/write operation.

Authors: Group B
Date: 2026-04-15
"""

import os
from ast import literal_eval

from event import Event

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FILE_PATH = os.path.join(PROJECT_ROOT, "data", "saved_events.txt")

def eventToDict(events: list[Event]) -> list[dict]:
    """
    Converts a list of Event objects to a list of dictionaries.
    Called after removing an event or updating an event's status.

    Parameters:
        events (list): list of Event objects to be saved.

    Returns:
        list[dict]: list of dictionaries representing the events.
    """

    events_dicts = [
        {"name": event.name, "date": event.date, "status": event.status}
        for event in events
    ]
    
    return events_dicts


def save_event(file, event: dict | list[dict]) -> bool:
    """
    Saves an event into a .txt file.

    Parameters:
        file (str): path to the .txt file where events are stored
        event (dict | list[dict]): event data to store

    Returns:
        True if the event was stored successfully.

    Raises:
        ValueError: if the file is not a .txt file, or event is invalid.
        FileNotFoundError: if the file does not exist.
    """

    # Verify file existence, create if not.
    if not os.path.exists(file):
        os.makedirs(os.path.dirname(file) or ".", exist_ok=True)
        with open(file, 'w') as f:
            f.write('[]\n')

    # Verify file type
    if not file.endswith(".txt"):
        raise ValueError("File must be a .txt file.")

    # Verify data type
    if not isinstance(event, (dict, list)):
        raise TypeError("Event must be a dictionary or list of dictionaries.")

    # Read existing events from file
    with open(file, "r") as f:
        events = f.read()

    # Text -> Data conversion
    events = literal_eval(events) if events else []

    if isinstance(event, dict):
        # Verify data structure
        if len(event) != 3:
            raise ValueError("Event must be a dict with exactly 3 elements.")
        events.append(event)
    else:
        if not all(isinstance(item, dict) for item in event):
            raise TypeError("All items in the event list must be dictionaries.")
        events = event

    # Update list of events and overwrite file
    with open(file, "w") as f:
        f.write(f"{events}\n")

    return True

def load_event(file) -> list[dict]:
    """
    Loads an event from a .txt file.

    Parameters:
        file (str): path to the .txt file where events are stored

    Returns:
        list: list of dicts containing event information.

    Raises:
        ValueError: if the file is not a .txt file.
        FileNotFoundError: if the file does not exist.
    """
    # Verify file existence
    if not os.path.exists(file):
        raise FileNotFoundError(f"File not found: {file}")
    
    # Verify file type
    if not file.endswith(".txt"):
        raise ValueError("File must be a .txt file.")

    # Read existing events from file and return as list of dicts
    with open(file, "r") as f:
        events = f.read()
    events = literal_eval(events) if events else []
    return events
