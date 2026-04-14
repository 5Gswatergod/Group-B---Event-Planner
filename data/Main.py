from Event import Event 
from EventPlanner import EventPlanner

# Helper Methods
def _is_valid_int(num):
    if isinstance(num,int) and num >0:
        return True       

def _is_valid_string(string):
    if isinstance(string,str) and string.strip() !="":
        return True


def _is_valid_date_string(new_date):
    if len(new_date) == 8 and new_date.isdigit():
        return True    

# input from the user
def get_valid_name():
    while True:
        name = input("Enter Event Name:")
        if _is_valid_string(name):
            return name
        print("Invalid Name. Enter Again.")

def get_valid_date():
    while True:
        date = input("Enter Event Date: (YYYYMMDD)")
        if _is_valid_date_string(date):
            return date
        print("Invalid date. Enter Again.")

def get_valid_status():
    while True:
        status = input("Upcoming OR Past? (u/p)").lower()
        if status == "u":
            return True
        elif status == "p":
            return False
        print("Invalid input. Enter 'u' or 'p'.")


# for loop
def main():
    planner = EventPlanner()

    while True:
        print("\n--- Event Planner ---")
        print("1. Add Event")
        print("2. View All Events")
        print("3. Mark Event Status")
        print("4. Remove Event")
        print("5. Exit")

        choice = input("Choose an Option: ")

        # Add Event
        if choice == "1":
            event_name = get_valid_name()
            event_date = get_valid_date()
            event_status = get_valid_status()

            new_event = Event(event_name,event_date,event_status)
            planner.add_event(new_event)

        # View All Events
        elif choice == "2":
            planner.display_list()

        # Mark Event Status
        elif choice == "3":
            if planner.get_event_count() == 0:
                print("Current No Events.")
            else:
                planner.display_list()
                try:
                    event_index = int(input("Enter The event index.")) - 1
                    event = planner.get_event(event_index)
                    new_status = get_valid_status()
                    event.set_status(new_status)
                    print("Status Updated.")

                except (ValueError, IndexError):
                    print("Invalid input.")

        # Remove Event
        elif choice == "4":
            if planner.get_event_count() == 0:
                print("Current No Events.")
            else:
                planner.display_list()
                try:
                    event_index = int(input("Enter The event index.")) - 1
                    planner.remove_event(event_index)   
                    print("Event Removed.")

                except (ValueError, IndexError):
                    print("Invalid input.")         

        # Quit    
        elif choice == "5":
            print("Goodbye.")
            break

if __name__ == "__main__":  
    main()
