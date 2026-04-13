import json
import os
from typing import Any


DATA_FILE = os.path.join("data", "events.json")


def ensure_data_dir() -> None:
    """Ensure the data directory exists."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)


def load_events() -> list[dict[str, Any]]:
    """
    Load events from the JSON file.

    Rules:
    - If file does not exist, return an empty list.
    - If file is empty, return an empty list.
    - If JSON is invalid, raise ValueError.
    - If root JSON is not a list, raise ValueError.
    """
    ensure_data_dir()

    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        raw = file.read().strip()

    if not raw:
        return []

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError("events.json is corrupted or contains invalid JSON.") from exc

    if not isinstance(data, list):
        raise ValueError("events.json root must be a JSON array.")

    return data


def save_events(events: list[dict[str, Any]]) -> None:
    """
    Save events to the JSON file using atomic write.
    """
    ensure_data_dir()

    temp_file = DATA_FILE + ".tmp"

    with open(temp_file, "w", encoding="utf-8") as file:
        json.dump(events, file, ensure_ascii=False, indent=2)

    os.replace(temp_file, DATA_FILE)
