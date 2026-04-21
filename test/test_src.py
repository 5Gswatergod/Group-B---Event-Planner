import io
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from unittest.mock import mock_open, patch


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_DIR = os.path.join(PROJECT_ROOT, "src")

if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

import main
import storage
from event import Event


class EventTests(unittest.TestCase):
    # TC-001: Event stores name, date, and status, then formats as a string.
    def test_event_stores_values_and_formats_string(self):
        event = Event("Meeting", "20260416", True)

        self.assertEqual(event.name, "Meeting")
        self.assertEqual(event.date, "20260416")
        self.assertTrue(event.status)
        self.assertEqual(str(event), "[Upcoming] Meeting - 2026 / 04 / 16")

    # TC-002: Event status label changes when the status value changes.
    def test_event_status_label_changes_with_status(self):
        event = Event("Workshop", "20260416", False)

        self.assertEqual(event._get_status_label(), "Past")

        event.status = True

        self.assertEqual(event._get_status_label(), "Upcoming")


class StorageTests(unittest.TestCase):
    # TC-003: Convert Event objects into dictionaries for storage.
    def test_event_to_dict_converts_event_objects(self):
        events = [
            Event("Meeting", "20260416", True),
            Event("Exam", "20260420", False),
        ]

        result = storage.eventToDict(events)

        self.assertEqual(
            result,
            [
                {"name": "Meeting", "date": "20260416", "status": True},
                {"name": "Exam", "date": "20260420", "status": False},
            ],
        )

    # TC-004: Save one event dictionary to an empty .txt file.
    def test_save_event_appends_single_event_dict(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "events.txt")
            with open(file_path, "w", encoding="utf-8") as file:
                file.write("[]\n")

            result = storage.save_event(
                file_path,
                {"name": "Meeting", "date": "20260416", "status": True},
            )

            self.assertTrue(result)
            self.assertEqual(
                storage.load_event(file_path),
                [{"name": "Meeting", "date": "20260416", "status": True}],
            )

    # TC-005: Save a full event list and overwrite existing stored data.
    def test_save_event_overwrites_with_full_event_list(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "events.txt")
            with open(file_path, "w", encoding="utf-8") as file:
                file.write("[{'name': 'Old', 'date': '20260101', 'status': True}]\n")

            new_events = [
                {"name": "Exam", "date": "20260420", "status": False},
                {"name": "Party", "date": "20260501", "status": True},
            ]

            result = storage.save_event(file_path, new_events)

            self.assertTrue(result)
            self.assertEqual(storage.load_event(file_path), new_events)

    # TC-006: Reject invalid save data that is not a dict or list of dicts.
    def test_save_event_rejects_invalid_type(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "events.txt")
            with self.assertRaises(TypeError):
                storage.save_event(file_path, "not an event") #type:ignore

    # TC-007: Reject storage files that do not use the .txt extension.
    def test_save_event_rejects_wrong_extension(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "events.json")
            with self.assertRaises(ValueError):
                storage.save_event(
                    file_path,
                    {"name": "Meeting", "date": "20260416", "status": True},
                )

    # TC-008: Raise FileNotFoundError when loading from a missing file.
    def test_load_event_raises_for_missing_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            missing_path = os.path.join(temp_dir, "missing.txt")

            with self.assertRaises(FileNotFoundError):
                storage.load_event(missing_path)


class MainHelperTests(unittest.TestCase):
    # TC-009: Display the empty-list message when there are no events.
    def test_display_list_prints_empty_message(self):
        output = io.StringIO()

        with redirect_stdout(output):
            main.display_list([])

        self.assertIn("Current No Events.", output.getvalue())

    # TC-010: Display saved events as a numbered list.
    def test_display_list_prints_numbered_events(self):
        events = [Event("Meeting", "20260416", True)]
        output = io.StringIO()

        with redirect_stdout(output):
            main.display_list(events)

        self.assertIn("1. [Upcoming] Meeting - 2026 / 04 / 16", output.getvalue())

    # TC-011: Validate a non-empty event name.
    def test_string_helper_returns_true_for_valid_name(self):
        self.assertTrue(main._is_valid_string("Meeting"))

    # TC-012: Validate a real date in YYYYMMDD format.
    def test_date_helper_returns_true_for_valid_date(self):
        self.assertTrue(main._is_valid_date_string("20260416"))

    # TC-013: Reject impossible calendar dates.
    def test_date_helper_rejects_impossible_date(self):
        self.assertFalse(main._is_valid_date_string("20260230"))

    # TC-014: Accept leap-day dates in valid leap years.
    def test_date_helper_accepts_leap_day(self):
        self.assertTrue(main._is_valid_date_string("20240229"))

    # TC-015: Retry name input until the user enters a valid name.
    def test_get_valid_name_retries_until_valid_input(self):
        with patch("builtins.input", side_effect=["", "Meeting"]):
            output = io.StringIO()
            with redirect_stdout(output):
                result = main.get_valid_name()

        self.assertEqual(result, "Meeting")
        self.assertIn("Invalid Name. Enter Again.", output.getvalue())

    # TC-016: Retry date input until the user enters a valid date.
    def test_get_valid_date_retries_until_valid_input(self):
        with patch("builtins.input", side_effect=["abc", "20260416"]):
            output = io.StringIO()
            with redirect_stdout(output):
                result = main.get_valid_date()

        self.assertEqual(result, "20260416")
        self.assertIn("Invalid date. Enter a real date in YYYYMMDD format.", output.getvalue())

    # TC-017: Strip extra spaces from valid date input.
    def test_get_valid_date_strips_extra_spaces(self):
        with patch("builtins.input", return_value=" 20260416 "):
            self.assertEqual(main.get_valid_date(), "20260416")

    # TC-018: Convert a user's one-based event selection to a zero-based index.
    def test_get_event_index_returns_zero_based_index(self):
        events = [Event("Meeting", "20260416", True)]

        with patch("builtins.input", return_value="1"):
            output = io.StringIO()
            with redirect_stdout(output):
                self.assertEqual(main.get_event_index(events), 0)

    # TC-019: Retry status input until the user enters u or p.
    def test_get_valid_status_retries_until_u_or_p(self):
        with patch("builtins.input", side_effect=["x", "p"]):
            output = io.StringIO()
            with redirect_stdout(output):
                result = main.get_valid_status()

        self.assertFalse(result)
        self.assertIn("Invalid input. Enter 'u' or 'p'.", output.getvalue())

if __name__ == "__main__":
    unittest.main()
