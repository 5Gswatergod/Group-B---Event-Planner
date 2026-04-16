from Event import Event


class EventPlanner:
    def __init__(self):
        self._events = []

    # HELPER METHODS
    def _is_valid_event(self, new_event):
        return isinstance(new_event, Event)

    def _is_valid_index(self, index):
        return isinstance(index, int) and 0 <= index < len(self._events)

    # FUNCTIONS
    def add_event(self, new_event):
        if not self._is_valid_event(new_event):
            raise ValueError("Invalid Event Object.")

        self._events.append(new_event)

    def remove_event(self, index):
        if not self._is_valid_index(index):
            raise ValueError("Invalid index.")

        return self._events.pop(index)

    def get_event(self, index):
        if not self._is_valid_index(index):
            raise ValueError("Invalid index.")

        return self._events[index]

    def get_all_events(self):
        return self._events.copy()

    def get_event_count(self):
        return len(self._events)

    def display_list(self):
        if self.get_event_count() == 0:
            print("Current No Events.")
            return

        for index, event in enumerate(self._events, start=1):
            print(f"{index}. {event}")


