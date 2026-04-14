# Debug Log – Task 1

## Error 1

**Error Message:**  
NameError: name '_event_count' is not defined

**What It Means:**  
Class variables must be accessed through the class name. Writing _event_count directly means Python cannot find it.

**How I Fixed It:**  
Changed `_event_count += 1` to `Event._event_count += 1`

**Resource Used:**  
VScode Debugger

## Error 2

**Error Message:**  
TypeError: object of type 'str' has no len() / incorrect validation

**What It Means:**  
Used _is_valid_int() to validate the date in _is_valid_date_string, but date is a string not an integer, so the type does not match.

**How I Fixed It:**  
Changed `self._is_valid_int(new_date)` to `new_date.isdigit()`

**Resource Used:**  
VScode Debugger

## Error 3

**Error Message:**  
AttributeError: 'Event' object has no attribute 'status'

**What It Means:**  
The attribute was defined as self._status (with underscore), but was called as self.status (without underscore), so the name does not match.

**How I Fixed It:**  
Changed `self.status` to `self._status` in _is_upcoming_or_past()

**Resource Used:**  
VScode Debugger

## Error 4

**Error Message:**  
TypeError: __str__ returned non-string type NoneType

**What It Means:**  
The __str__ method has no return statement. Python returns None by default, but __str__ must return a string.

**How I Fixed It:**  
Added `return f"[{status}] {self._name} - {date}"` at the end of __str__

**Resource Used:**  
VScode Debugger

## Error 5

**Error Message:**  

**What It Means:**  

**How I Fixed It:**  

**Resource Used:**