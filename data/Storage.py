import os

def save_event(file, event):
    '''
    Saves an event into a .txt file.

    Parameters:
        file (str): path to the .txt file where events are stored
        event (dict): must contain exactly 3 keys — name (str), date (str), status (str)

    Returns:
        True if the event was stored successfully.

    Raises:
        ValueError: if the file is not a .txt file, or event is invalid.
        FileNotFoundError: if the file does not exist.
    '''
    # Verify file existence
    if not os.path.exists(file):
        raise FileNotFoundError(f"File not found: {file}")
    
    # Verify file type
    if not file.endswith(".txt"):
        raise ValueError("File must be a .txt file.")

    # Verify data type
    if not isinstance(event, dict):
        raise TypeError("Event must be a dictionary.")
    
    # Verify data structure
    if len(event) != 3:
        raise ValueError("Event must be a dict with exactly 3 elements.")

    # Read existing events from file
    with open(file, "r") as f:
        events = f.read()
    
    # Text -> Data conversion
    events = eval(events) if events else []

    # Update list of events and overwrite file
    with open(file, "w") as f:
        events.append(event)
        f.write(f"{events}\n")
    
    return True

def load_event(file):
    '''
    Loads an event from a .txt file.

    Parameters:
        file (str): path to the .txt file where events are stored

    Returns:
        list: list of dicts containing event information.

    Raises:
        ValueError: if the file is not a .txt file.
        FileNotFoundError: if the file does not exist.
    '''
    # Verify file existence
    if not os.path.exists(file):
        raise FileNotFoundError(f"File not found: {file}")
    
    # Verify file type
    if not file.endswith(".txt"):
        raise ValueError("File must be a .txt file.")

    # Read existing events from file and return as list of dicts
    with open(file, "r") as f:
        events = f.read()
    events = eval(events) if events else []
    return events