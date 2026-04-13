import json
from dataclasses import dataclass, asdict


@dataclass
class Event:
    id: int
    name: str
    date: str
    location: str
    description: str = ""

def load_events() -> list[dict]:
    pass

def save_events(events: list[dict]) -> None:
    pass