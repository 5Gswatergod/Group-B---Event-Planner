'''
Purpose of this file:
- Defines the Event class, which represents a single event with a name, date, and upcoming/past status.

Features:
- Create an event with a name and date.
- Mark an event as upcoming or past.
- Display a formatted summary of an event.
- Validate all event fields on assignment.

Authors: Group B
Date: 2026-04-15
'''


class Event:

    # Initializer
    def __init__(self, name: str, date: str, status: bool):
        self.name = name
        self.date = date
        self.status = status

    # Helper Methods
    def _validate_int(self, num):
        if not isinstance(num, int) and num > 0:
            raise ValueError("Invalid Integer.")

    def _validate_flt(self, num):
        if not isinstance(num, float) and num >= 0:
            raise ValueError("Invalid Float.")

    def _validate_string(self, string):
        if not isinstance(string, str) and string.strip() != "":
            raise ValueError("Invalid String.")

    def _validate_date_string(self, date):
        if not len(date) == 8 and date.isdigit():
            raise ValueError("Invalid Date.")

    # Getters and Setters
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._validate_string(new_name)
        self._name = new_name

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, new_date):
        self._validate_date_string(new_date)
        self._date = new_date

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        self._status = new_status

    # Class Public Methods
    def _get_status_label(self):
        return "Upcoming" if self._status else "Past"

    def __str__(self):
        date = self._date[:4] + " / " + self._date[4:6] + " / " + self._date[6:]
        status = self._get_status_label()
        return f"[{status}] {self._name} - {date}"
