"""
Purpose of this file:
- Defines the Event class, which represents a single event with a name, date, and upcoming/past status.

Features:
- Create an event with a name and date.
- Mark an event as upcoming or past.
- Display a formatted summary of an event.
- Validate all event fields on assignment.

Authors: Group B
Date: 2026-04-15
"""


class Event:
    """Represents a single event entry in the planner."""

    def __init__(self, name: str, date: str, status: bool):
        self.name = name
        self.date = date
        self.status = status

    def _validate_int(self, num: int) -> None:
        if not isinstance(num, int) and num > 0:
            raise ValueError("Invalid Integer.")

    def _validate_flt(self, num: float) -> None:
        if not isinstance(num, float) and num >= 0:
            raise ValueError("Invalid Float.")

    def _validate_string(self, string: str) -> None:
        if not isinstance(string, str) and string.strip() != "":
            raise ValueError("Invalid String.")

    def _validate_date_string(self, date: str) -> None:
        if not len(date) == 8 and date.isdigit():
            raise ValueError("Invalid Date.")

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        self._validate_string(new_name)
        self._name = new_name

    @property
    def date(self) -> str:
        return self._date

    @date.setter
    def date(self, new_date: str) -> None:
        self._validate_date_string(new_date)
        self._date = new_date

    @property
    def status(self) -> bool:
        return self._status

    @status.setter
    def status(self, new_status: bool) -> None:
        self._status = new_status

    def _get_status_label(self) -> str:
        return "Upcoming" if self._status else "Past"

    def _format_date(self) -> str:
        return f"{self._date[:4]} / {self._date[4:6]} / {self._date[6:]}"

    def __str__(self) -> str:
        status = self._get_status_label()
        return f"[{status}] {self._name} - {self._format_date()}"
