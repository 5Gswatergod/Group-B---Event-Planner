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

Example 1: Add Event

Input:
Choose an Option: 1
Enter Event Name: Math Test
Enter Event Date: (YYYYMMDD) 20260508
Upcoming OR Past? (u/p) u

Example 2: View Events

Input:
Choose an Option: 2

Output:
1. [Upcoming] Math Test - 2026 / 05 / 08

Example 3: Update Event Status

Input:
Choose an Option: 3
Upcoming OR Past? (u/p)p

Output:
1. [Upcoming] Math Test - 2026 / 05 / 08
Enter The event index: 1
Status Updated.

Example 4: Remove Event

Input:
Choose an Option: 4
Enter The event index: 1

Output:
Event Removed.

Example 5: Invalid Event name

Input:
Choose an Option: 1
Enter Event Name:

Output:
Invalid Name. Enter Again.

Example 6: Empty Event List

Output:
Current No Events.

Example 7: Invalid date

Input:
Enter Event Name: 1
Enter Event Date: (YYYYMMDD) 88888888

Output:
Invalid date. Enter a real date in YYYYMMDD format.




