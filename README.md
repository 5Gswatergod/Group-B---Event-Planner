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

Output:

[Upcoming] Math Test - 2026 / 05 / 08

Example 2: View Events

Output:

1. [Upcoming] Math Test - 2026 / 05 / 08
2. [Past] English Essay - 2026 / 04 / 15

Example 3: Update Event Status

Input:

Choose an Option: 3
Enter The event index: 1
Upcoming OR Past? (u/p) p

Output:

Status Updated.

Updated List:

1. [Past] Math Test - 2026 / 05 / 08

Example 4: Remove Event

Input:

Choose an Option: 4
Enter The event index: 1

Output:

Event Removed.

Example 5: Invalid Input

Input:

Choose an Option: 1
Enter Event Name:

Output:

Invalid Name. Enter Again.

Example 6: Empty Event List

Output:

Current No Events.



