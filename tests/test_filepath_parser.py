import tempfile
import unittest
from pathlib import Path

from opencf_core.utils import get_filepaths_from_inputs


class TestGetFilepathsFromCli(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.TemporaryDirectory()
        self.test_path = Path(self.test_dir.name)

        # Create some files and directories for testing
        (self.test_path / "file1.txt").touch()
        (self.test_path / "file2.log").touch()

        (self.test_path / "subdir").mkdir()
        (self.test_path / "subdir" / "file3.txt").touch()
        (self.test_path / "subdir" / "file4.log").touch()

    def tearDown(self):
        # Cleanup the temporary directory
        self.test_dir.cleanup()

    def test_single_file(self):
        args = [str(self.test_path / "file1.txt")]
        expected = [str(self.test_path / "file1.txt")]
        self.assertEqual(get_filepaths_from_inputs(args), expected)

    def test_directory(self):
        args = [str(self.test_path / "subdir")]
        expected = [
            str(self.test_path / "subdir" / "file3.txt"),
            str(self.test_path / "subdir" / "file4.log"),
        ]
        self.assertCountEqual(get_filepaths_from_inputs(args), expected)

    def test_glob_pattern(self):
        args = [str(self.test_path / "*.txt")]
        expected = [str(self.test_path / "file1.txt")]
        self.assertEqual(get_filepaths_from_inputs(args), expected)

    def test_mixed_input(self):
        args = [
            str(self.test_path / "file1.txt"),
            str(self.test_path / "subdir"),
            str(self.test_path / "*.log"),
        ]
        expected = [
            str(self.test_path / "file1.txt"),
            str(self.test_path / "file2.log"),
            str(self.test_path / "subdir" / "file3.txt"),
            str(self.test_path / "subdir" / "file4.log"),
        ]
        self.assertCountEqual(get_filepaths_from_inputs(args), expected)


if __name__ == "__main__":
    unittest.main()
