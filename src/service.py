from typing import Any

from src.storage import load_events, save_events
from src.validation import validate_event_input


def get_next_id(events: list[dict[str, Any]]):
    """
    Return the next available integer ID.
    """
    return max((event["id"] for event in events), default=0) + 1


def add_event(
    name: str,
    date: str,
    location: str,
    description: str = "",
):
    """
    Create and save a new event.
    """
    events = load_events()
    validated = validate_event_input(name, date, location, description)

    new_event = {
        "id": get_next_id(events),
        "name": validated["name"],
        "date": validated["date"],
        "location": validated["location"],
        "description": validated["description"],
    }

    events.append(new_event)
    save_events(events)
    return new_event


def list_events():
    """
    Return all events sorted by date ascending, then by ID ascending.
    """
    events = load_events()
    return sorted(events, key=lambda event: (event["date"], event["id"]))


def find_event_by_id(event_id: int):
    """
    Find and return an event by ID, or None if not found.
    """
    events = load_events()
    for event in events:
        if event["id"] == event_id:
            return event
    return None


def edit_event(
    event_id: int,
    name: str,
    date: str,
    location: str,
    description: str = "",
):
    """
    Update an existing event by ID.
    Raises ValueError if event is not found.
    """
    events = load_events()
    validated = validate_event_input(name, date, location, description)

    for event in events:
        if event["id"] == event_id:
            event["name"] = validated["name"]
            event["date"] = validated["date"]
            event["location"] = validated["location"]
            event["description"] = validated["description"]
            save_events(events)
            return event

    raise ValueError(f"Event with ID {event_id} was not found.")


def delete_event(event_id: int):
    """
    Delete an existing event by ID.
    Raises ValueError if event is not found.
    """
    events = load_events()

    for index, event in enumerate(events):
        if event["id"] == event_id:
            deleted_event = events.pop(index)
            save_events(events)
            return deleted_event

    raise ValueError(f"Event with ID {event_id} was not found.")
