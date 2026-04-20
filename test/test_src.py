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
                storage.save_event(file_path, "not an event") #type:ignore

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


class MainFlowTests(unittest.TestCase):
    def test_main_add_view_and_exit_saves_full_event_list(self):
        user_inputs = ["1", "Meeting", "20260416", "u", "2", "5"]
        output = io.StringIO()

        with patch.object(main.os.path, "exists", return_value=True), \
             patch.object(main, "load_event", return_value=[]), \
             patch.object(main, "save_event") as mock_save_event, \
             patch("builtins.input", side_effect=user_inputs), \
             redirect_stdout(output):
            main.main()

        self.assertIn("[Upcoming] Meeting - 2026 / 04 / 16", output.getvalue())
        mock_save_event.assert_called_once_with(
            main.FILE_PATH,
            [{"name": "Meeting", "date": "20260416", "status": True}],
        )

    def test_main_marks_event_status(self):
        user_inputs = ["3", "p", "1", "5"]
        output = io.StringIO()

        with patch.object(main.os.path, "exists", return_value=True), \
             patch.object(
                 main,
                 "load_event",
                 return_value=[{"name": "Meeting", "date": "20260416", "status": True}],
             ), \
             patch.object(main, "save_event") as mock_save_event, \
             patch("builtins.input", side_effect=user_inputs), \
             redirect_stdout(output):
            main.main()

        self.assertIn("Status Updated.", output.getvalue())
        mock_save_event.assert_called_once_with(
            main.FILE_PATH,
            [{"name": "Meeting", "date": "20260416", "status": False}],
        )

    def test_main_removes_event(self):
        user_inputs = ["4", "1", "5"]
        output = io.StringIO()

        with patch.object(main.os.path, "exists", return_value=True), \
             patch.object(
                 main,
                 "load_event",
                 return_value=[{"name": "Meeting", "date": "20260416", "status": True}],
             ), \
             patch.object(main, "save_event") as mock_save_event, \
             patch("builtins.input", side_effect=user_inputs), \
             redirect_stdout(output):
            main.main()

        self.assertIn("Event Removed.", output.getvalue())
        mock_save_event.assert_called_once_with(main.FILE_PATH, [])

    def test_main_handles_empty_list_actions(self):
        user_inputs = ["3", "4", "5"]
        output = io.StringIO()

        with patch.object(main.os.path, "exists", return_value=True), \
             patch.object(main, "load_event", return_value=[]), \
             patch.object(main, "save_event"), \
             patch("builtins.input", side_effect=user_inputs), \
             redirect_stdout(output):
            main.main()

        self.assertGreaterEqual(output.getvalue().count("Current No Events."), 2)

    def test_main_handles_invalid_selected_index(self):
        user_inputs = ["3", "u", "9", "5"]
        output = io.StringIO()

        with patch.object(main.os.path, "exists", return_value=True), \
             patch.object(
                 main,
                 "load_event",
                 return_value=[{"name": "Meeting", "date": "20260416", "status": True}],
             ), \
             patch.object(main, "save_event"), \
             patch("builtins.input", side_effect=user_inputs), \
             redirect_stdout(output):
            main.main()

        self.assertIn("Invalid input.", output.getvalue())

    def test_main_creates_data_file_when_missing(self):
        mocked_file = mock_open()
        output = io.StringIO()

        with patch.object(main.os.path, "exists", return_value=False), \
             patch.object(main, "load_event", return_value=[]), \
             patch.object(main, "save_event"), \
             patch("builtins.open", mocked_file), \
             patch("builtins.input", side_effect=["5"]), \
             redirect_stdout(output):
            main.main()

        mocked_file.assert_called_once_with(main.FILE_PATH, "w")
        self.assertIn("Goodbye.", output.getvalue())


if __name__ == "__main__":
    unittest.main()
