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
TypeError: _is_valid_string() takes 2 positional arguments but 1 was given

**What It Means:**  
The helper functions were copied from a class but placed outside of a class in main.py. Functions outside a class do not need the self parameter.

**How I Fixed It:**  
Removed the self parameter from all helper functions in main.py.

**Resource Used:** 
Claude AI 

## Error 6

**Error Message:**  
TypeError: _is_valid_int() takes 2 positional arguments but 1 was given

**What It Means:**  
Helper functions in main.py are not inside a class, so they do not need the self parameter. Having self there causes Python to expect an extra argument.

**How I Fixed It:**  
Removed self from _is_valid_int() and _is_valid_date_string() in main.py.

**Resource Used:**  
Claude AI

## Error 7

**Error Message:**  
TypeError: add_event() missing 1 required positional argument: 'new_event'

**What It Means:**  
Used the class name EventPlanner instead of the instance planner to call methods. Calling methods on the class name does not automatically pass the instance.

**How I Fixed It:**  
Changed EventPlanner.add_event() to planner.add_event(), and same for display_list(), remove_event(), and get_event_count().

**Resource Used:**  
VScode Debugger

## Error 8

**Error Message:**  
TypeError: isinstance() arg 2 must be a type, not str

**What It Means:**  
input() always returns a string, but _is_valid_int() checks for int type. The string from input will never pass the int check.

**How I Fixed It:**  
Used int(input()) to convert the input to an integer before checking.

**Resource Used:**  
VScode Debugger

## Error 9

**Error Message:**  
Program exits unexpectedly when selecting option 3 or 4.

**What It Means:**  
Used return inside main() which exits the entire function. return should only be used to end the function, not to break out of a while loop.

**How I Fixed It:**  
Changed return event_index to break.

**Resource Used:**  
VScode Debugger

## Error 10

**Error Message:**  
AttributeError: type object 'Event' has no method that works this way

**What It Means:**  
Used Event.set_status(status) on the class instead of on a specific event instance. Need to first get the event from the planner, then call set_status on that event.

**How I Fixed It:**  
Used planner.get_event(index) to get the specific event, then called event.set_status(new_status) on it.

**Resource Used:**  
VScode Debugger