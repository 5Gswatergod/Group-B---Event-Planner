# Testing Plan

## Overview
**Functions tested:** Add Event
**Testing types:** Unit  
**Date:**  2026/04/16

---

## Test Case Table

| Test ID | Description | Input(s) | Expected Output | Type | Pass/Fail | Notes |
|---------|-------------|----------|-----------------|------|-----------|-------|
T1|Empty Event Name|[], "", "20260416", True|ValueError Raised|Edge Case|Pass||
T2|whitespace Name|[], "   ", "20260416", True|ValueError Raised|Edge Case|Pass||
T3|Valid String|events, "Meeting", "20260416", True|Event added to list, len(events) == 1|Normal Case|Pass||
---

## Code Used for Testing
```

def add_event(events, name, date, status):
    # adds a new event dict to events list
    # raises ValueError if name is empty or whitespace
    if not (isinstance(name, str) and name.strip() != ""):
        raise ValueError("Invalid Event Name.")
    
    events.append({"name": name, "date": date, "status": status})


```