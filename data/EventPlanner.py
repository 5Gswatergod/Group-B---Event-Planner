# Allow the user to create an event with a name or description.
# Allow the user to assign a date to each event.
# Allow the user to view all events in a list.
# Clearly show whether each event is upcoming or already past.
# Allow the user to mark an event as upcoming or past.
# Save event data so that they are still available when the program is run again.

from Event import Event

class EventPlanner:
    def __init__(self):
        self._events = []


    # HELPER METHODS
    def _is_valid_event(self,new_event):
        if isinstance(new_event,Event):
            return True

    def _is_valid_int(self,num):
        if isinstance(num,int) and num >=0:
            return True       
        
    # FUNCTIONS

    def add_event(self,new_event):
        if self._is_valid_event(new_event):
            self._events.append(new_event)
        else:
            raise ValueError("Invalid Event Object.")

    def remove_event(self,index):
        if 0 <= index < len(self._events) and isinstance(index,int):
            self._events.pop(index)
        else:
            raise ValueError("Invalid index.")

    def get_event(self,index):
        if 0 <= index < len(self._events) and isinstance(index,int):
            return self._events[index]
        else:
            raise ValueError("Invalid index.")
    
    def get_all_events(self):
        return self._events
        
    def display_list(self):
        if len(self._events) == 0:
            print("Current No Events.")

        else:
            for i in range(len(self._events)):
                print(f"{i+1}. {self._events[i]}")


