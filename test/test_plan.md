# Testing Plan

## Overview
**Functions/classes tested:** `Event`, `eventToDict`, `save_event`, `load_event`, `display_list`, `_is_valid_string`, `_is_valid_date_string`, `get_valid_name`, `get_valid_date`, `get_event_index`, `get_valid_status`, `main`  
**Testing types:** Unit / Integration / Regression  
**Date:** 2026-04-20  

This test plan is based on the automated tests in `test_src.py`. The tests check event formatting, storage behavior, user input validation, menu flow behavior, and error handling.

---

## Test Case Table

| Test ID | Description | Input(s) | Expected Output | Type | Pass/Fail | Notes |
|---------|-------------|----------|-----------------|------|-----------|-------|
| TC-001 | Event stores name, date, and status, then formats as a string | `Event("Meeting", "20260416", True)` | Event fields match inputs; string is `[Upcoming] Meeting - 2026 / 04 / 16` | Unit | Pass | Tests constructor, properties, and `__str__` |
| TC-002 | Event status label changes when status changes | `Event("Workshop", "20260416", False)`, then `status = True` | Label changes from `Past` to `Upcoming` | Unit | Pass | Tests `_get_status_label` |
| TC-003 | Convert event objects to dictionaries | Two `Event` objects | List of dictionaries with `name`, `date`, and `status` | Unit | Pass | Tests `eventToDict` |
| TC-004 | Save one event dictionary to an empty file | Empty temp `.txt` file and one event dict | Save returns `True`; file loads with one event | Integration | Pass | Uses temp file |
| TC-005 | Save full event list and overwrite old data | Temp `.txt` file with old data and new event list | Save returns `True`; loaded file equals new list | Integration | Pass | Confirms overwrite behavior |
| TC-006 | Reject invalid save data type | `"not an event"` | Raises `TypeError` | Unit | Pass | Tests storage validation |
| TC-007 | Reject wrong file extension | `events.json` path | Raises `ValueError` | Unit | Pass | Only `.txt` files should be accepted |
| TC-008 | Reject missing file when loading | Missing temp path | Raises `FileNotFoundError` | Unit | Pass | Tests `load_event` error handling |
| TC-009 | Display empty event list | `[]` | Prints `Current No Events.` | Unit | Pass | Tests empty list output |
| TC-010 | Display numbered event list | One meeting event | Prints numbered event line | Unit | Pass | Tests formatted list display |
| TC-011 | Validate non-empty event name | `"Meeting"` | Returns `True` | Unit | Pass | Tests `_is_valid_string` |
| TC-012 | Validate correct date string | `"20260416"` | Returns `True` | Unit | Pass | Tests valid `YYYYMMDD` date |
| TC-013 | Reject impossible date | `"20260230"` | Returns `False` | Unit | Pass | Rejects February 30 |
| TC-014 | Accept leap day date | `"20240229"` | Returns `True` | Unit | Pass | Confirms leap year support |
| TC-015 | Retry name input until valid | `""`, then `"Meeting"` | Returns `"Meeting"` and prints invalid-name message | Unit | Pass | Uses mocked input |
| TC-016 | Retry date input until valid | `"abc"`, then `"20260416"` | Returns `"20260416"` and prints invalid-date message | Unit | Pass | Uses mocked input |
| TC-017 | Strip spaces from valid date input | `" 20260416 "` | Returns `"20260416"` | Unit | Pass | Confirms input cleanup |
| TC-018 | Convert selected event number to zero-based index | User enters `"1"` | Returns `0` | Unit | Pass | Also displays event list |
| TC-019 | Retry status input until `u` or `p` | `"x"`, then `"p"` | Returns `False` and prints invalid-status message | Unit | Pass | `False` means Past |

---

## Code Used for Testing

```python
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
    def test_event_stores_values_and_formats_string(self):
        event = Event("Meeting", "20260416", True)

        self.assertEqual(event.name, "Meeting")
        self.assertEqual(event.date, "20260416")
        self.assertTrue(event.status)
        self.assertEqual(str(event), "[Upcoming] Meeting - 2026 / 04 / 16")

    def test_event_status_label_changes_with_status(self):
        event = Event("Workshop", "20260416", False)

        self.assertEqual(event._get_status_label(), "Past")

        event.status = True

        self.assertEqual(event._get_status_label(), "Upcoming")


class StorageTests(unittest.TestCase):
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

    def test_save_event_rejects_invalid_type(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "events.txt")
            with self.assertRaises(TypeError):
                storage.save_event(file_path, "not an event")

    def test_save_event_rejects_wrong_extension(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "events.json")
            with self.assertRaises(ValueError):
                storage.save_event(
                    file_path,
                    {"name": "Meeting", "date": "20260416", "status": True},
                )

    def test_load_event_raises_for_missing_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            missing_path = os.path.join(temp_dir, "missing.txt")

            with self.assertRaises(FileNotFoundError):
                storage.load_event(missing_path)


class MainHelperTests(unittest.TestCase):
    def test_display_list_prints_empty_message(self):
        output = io.StringIO()

        with redirect_stdout(output):
            main.display_list([])

        self.assertIn("Current No Events.", output.getvalue())

    def test_display_list_prints_numbered_events(self):
        events = [Event("Meeting", "20260416", True)]
        output = io.StringIO()

        with redirect_stdout(output):
            main.display_list(events)

        self.assertIn("1. [Upcoming] Meeting - 2026 / 04 / 16", output.getvalue())

    def test_string_helper_returns_true_for_valid_name(self):
        self.assertTrue(main._is_valid_string("Meeting"))

    def test_date_helper_returns_true_for_valid_date(self):
        self.assertTrue(main._is_valid_date_string("20260416"))

    def test_date_helper_rejects_impossible_date(self):
        self.assertFalse(main._is_valid_date_string("20260230"))

    def test_date_helper_accepts_leap_day(self):
        self.assertTrue(main._is_valid_date_string("20240229"))

    def test_get_valid_name_retries_until_valid_input(self):
        with patch("builtins.input", side_effect=["", "Meeting"]):
            output = io.StringIO()
            with redirect_stdout(output):
                result = main.get_valid_name()

        self.assertEqual(result, "Meeting")
        self.assertIn("Invalid Name. Enter Again.", output.getvalue())

    def test_get_valid_date_retries_until_valid_input(self):
        with patch("builtins.input", side_effect=["abc", "20260416"]):
            output = io.StringIO()
            with redirect_stdout(output):
                result = main.get_valid_date()

        self.assertEqual(result, "20260416")
        self.assertIn("Invalid date. Enter a real date in YYYYMMDD format.", output.getvalue())

    def test_get_valid_date_strips_extra_spaces(self):
        with patch("builtins.input", return_value=" 20260416 "):
            self.assertEqual(main.get_valid_date(), "20260416")

    def test_get_event_index_returns_zero_based_index(self):
        events = [Event("Meeting", "20260416", True)]

        with patch("builtins.input", return_value="1"):
            output = io.StringIO()
            with redirect_stdout(output):
                self.assertEqual(main.get_event_index(events), 0)

    def test_get_valid_status_retries_until_u_or_p(self):
        with patch("builtins.input", side_effect=["x", "p"]):
            output = io.StringIO()
            with redirect_stdout(output):
                result = main.get_valid_status()

        self.assertFalse(result)
        self.assertIn("Invalid input. Enter 'u' or 'p'.", output.getvalue())

if __name__ == "__main__":
    unittest.main()
```
