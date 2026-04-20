#Automated testing
import unittest

def add_event(events, name, date, status):
    # adds a new event dict to events list
    # raises ValueError if name is empty or whitespace
    if not (isinstance(name, str) and name.strip() != ""):
        raise ValueError("Invalid Event Name.")
    
    events.append({"name": name, "date": date, "status": status})

class TestAddEvent(unittest.TestCase):

    def test_empty_name(self): # Edge
        self.assertRaises(ValueError, add_event, [], "", "20260416", True)
        # pass event list, name, date, and status
        
    def test_whitespace_name(self): # Edge 
        self.assertRaises(ValueError, add_event, [], "   ", "20260416", True)

    def test_valid_add(self): # Normal
        events = []
        add_event(events, "Meeting", "20260416", True) # add 1 event
        self.assertEqual(len(events), 1) # list should have 1 item
        self.assertEqual(events[0]["name"], "Meeting") # item's name should be "Meeting"


if __name__ == '__main__':
    unittest.main()
