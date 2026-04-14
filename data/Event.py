# Group B - Event Planner
# Event Planner: App Requirements
# The application must, at a minimum:

# Allow the user to create an event with a name or description.
# Allow the user to assign a date to each event.
# Allow the user to view all events in a list.
# Clearly show whether each event is upcoming or already past.
# Allow the user to mark an event as upcoming or past.
# Save event data so that they are still available when the program is run again.


class Event:
    # Class Method
    _event_count = 0

    def __init__(self,name:str,date:str,status:bool):
        # upcoming: True 
        # Past: False

        self._name = name
        self._date = date
        self._status = status

        Event._event_count += 1

    # Get count
    @classmethod
    def get_event_count(cls):
        return cls._event_count

    # Helper Methods  
    def _is_valid_int(self,num):
        if isinstance(num,int) and num >0:
            return True       
        
    def _is_valid_flt(self,num):
        if isinstance(num,float) and num >=0:
            return True    
        
    def _is_valid_string(self,string):
        if isinstance(string,str) and string.strip() !="":
            return True
        
    def _is_valid_date_string(self,new_date):
        if len(new_date) == 8 and new_date.isdigit():
            return True    

    # Name
    def set_name(self,new_name):
        if self._is_valid_string(new_name):
            self._name = new_name
        else:
            raise ValueError("Invalid Event Name.")

    def get_name(self):
        return self._name
    
    # Date
    def set_date(self,new_date):
        if self._is_valid_date_string(new_date):
            self._date = new_date
        else:
            raise ValueError("Invalid Event Date.")
    
    def get_date(self):
        return self._date

    # Status
    def set_status(self,new_status):
        self._status = new_status

    def get_status(self):
        return self._status
    
    # Display single Event
    def _is_upcoming_or_past(self):
        if self._status == True:
            return "Upcoming"
        else:
            return "Past"
        
    def __str__(self):
        date = self._date[:4] + " / " + self._date[4:6] + " / " + self._date[6:]
        status = self._is_upcoming_or_past()
        return f"[{status}] {self._name} - {date}"