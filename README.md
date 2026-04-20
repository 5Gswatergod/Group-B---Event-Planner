# Event Planner App

## Description
This program is a simple Event Planner written in Python.  
It allows users to create, view, update, and delete events. Each event includes a name, date (YYYYMMDD), and status (Upcoming or Past).  
All events are saved to a `.txt` file so they can be loaded again when the program runs.

---

## How to Run

1. Make sure all files (`main.py`, `event.py`, `storage.py`) are in the same folder  
2. Run the program using: python main.py

```bash

Example Input/Output

Menu:

--- Event Planner ---
1. Add Event
2. View All Events
3. Mark Event Status
4. Remove Event
5. Exit

Example input:

Choose an Option: 1
Enter Event Name: Meeting
Enter Event Date: (YYYYMMDD) 20260420
Upcoming OR Past? (u/p) u

Example output:

[Upcoming] Meeting - 2026 / 04 / 20

