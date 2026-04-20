# Event Planner App

## Overview
This is a simple Event Planner application written in Python.  
It allows users to create, view, update, and delete events. All events are saved to a `.txt` file so they can be loaded again later.

---

## Features

- Add a new event (name, date, status)
- View all events in a numbered list
- Update an event’s status (Upcoming or Past)
- Remove an event
- Save and load events from a file

---

## File Structure

- `main.py` → Main program (user interface)
- `event.py` → Defines the Event class
- `storage.py` → Handles saving and loading data
- `data/saved_events.txt` → Stores event data

---

## How to Run

1. Make sure all files are in the same folder
2. Run the program:

```bash
python main.py
Example Usage
--- Event Planner ---
1. Add Event
2. View All Events
3. Mark Event Status
4. Remove Event
5. Exit

Choose an Option: 1
Enter Event Name: Meeting
Enter Event Date: (YYYYMMDD) 20260420
Upcoming OR Past? (u/p) u

Output:

[Upcoming] Meeting - 2026 / 04 / 20
Data Storage

Events are stored in:

./data/saved_events.txt

Example format:

[
  {"name": "Meeting", "date": "20260420", "status": True}
]
Input Validation

The program checks:

Name is not empty
Date is exactly 8 digits (YYYYMMDD)
Status must be u or p
Edge Cases
Empty event name → rejected
Invalid date format → rejected
Selecting an event that does not exist → handled with error message
No events in list → displays "Current No Events."
Limitations
Date is stored as a string (no real date validation like leap years)
Data is stored in a .txt file instead of a database
No sorting or searching functionality
Future Improvements
Add real date validation
Add event sorting (by date)
Add search functionality
Use JSON or database instead of .txt

