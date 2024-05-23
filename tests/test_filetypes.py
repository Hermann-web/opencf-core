import unittest
from pathlib import Path

from opencf_core.filetypes import FileType, MimeType
from opencf_core.exceptions import EmptySuffixError, UnsupportedFileTypeError

class FileTypeTest(unittest.TestCase):

    def test_different_mimetypes(self):
        mimetype1 = MimeType()
        mimetype2 = MimeType()
        self.assertNotEqual(mimetype1, mimetype2)
        self.assertNotEqual(id(mimetype1), id(mimetype2))
    
    def test_file_type_parsing(self):
        """Tests for validating the functionality of file type parsing."""
        # Test parsing of different file types
        text_path = Path("test.txt")
        csv_path = Path("data.csv")
        excel_path = Path("results.xlsx")
        json_path = Path("config.json")
        img_path = Path("picture.jpg")

        self.assertEqual(FileType.from_path(text_path), FileType.TEXT)
        self.assertEqual(FileType.from_path(csv_path), FileType.CSV)
        self.assertEqual(FileType.from_path(excel_path), FileType.EXCEL)
        self.assertEqual(FileType.from_path(json_path), FileType.JSON)
        self.assertEqual(FileType.from_path(img_path), FileType.IMAGE)
        self.assertEqual(FileType.from_path(Path("no_extension")), FileType.NOTYPE)
        self.assertEqual(FileType.from_path(Path("unknown.xyz")), FileType.UNHANDLED)

    def test_file_type_matching(self):
        """Tests for validating the functionality of file type matching."""
        # Test matching of different file types
        text_path = Path("test.txt")
        csv_path = Path("data.csv")
        excel_path = Path("results.xlsx")
        json_path = Path("config.json")
        img_path = Path("picture.jpg")

        self.assertTrue(FileType.TEXT.is_valid_path(text_path))
        self.assertFalse(FileType.TEXT.is_valid_path(csv_path))

        self.assertTrue(FileType.CSV.is_valid_path(csv_path))
        self.assertFalse(FileType.CSV.is_valid_path(excel_path))

        self.assertTrue(FileType.EXCEL.is_valid_path(excel_path))
        self.assertFalse(FileType.EXCEL.is_valid_path(json_path))

        self.assertTrue(FileType.JSON.is_valid_path(json_path))
        self.assertFalse(FileType.JSON.is_valid_path(img_path))

        self.assertTrue(FileType.IMAGE.is_valid_path(img_path))
        self.assertFalse(FileType.IMAGE.is_valid_path(text_path))

        self.assertTrue(FileType.NOTYPE.is_valid_path(Path("no_extension")))
        self.assertFalse(FileType.NOTYPE.is_valid_path(text_path))

        self.assertTrue(FileType.UNHANDLED.is_valid_path(Path("unknown.xyz")))
        self.assertFalse(FileType.UNHANDLED.is_valid_path(csv_path))

    def test_is_true_filetype(self):
        """Test the is_true_filetype method."""
        self.assertTrue(FileType.TEXT.is_true_filetype())
        self.assertTrue(FileType.CSV.is_true_filetype())
        self.assertFalse(FileType.NOTYPE.is_true_filetype())
        self.assertFalse(FileType.UNHANDLED.is_true_filetype())

    def test_get_suffix(self):
        """Test the get_suffix method."""
        self.assertEqual(FileType.TEXT.get_suffix(), ".txt")
        self.assertEqual(FileType.CSV.get_suffix(), ".csv")
        self.assertEqual(FileType.NOTYPE.get_suffix(), "")
        self.assertEqual(FileType.UNHANDLED.get_suffix(), "")

    def test_is_valid_suffix(self):
        """Test the is_valid_suffix method."""
        self.assertTrue(FileType.TEXT.is_valid_suffix(".txt"))
        self.assertFalse(FileType.TEXT.is_valid_suffix(".csv"))
        self.assertTrue(FileType.CSV.is_valid_suffix(".csv"))
        self.assertFalse(FileType.CSV.is_valid_suffix(".txt"))

    def test_is_valid_mime_type(self):
        """Test the is_valid_mime_type method."""
        DATA_FOLDER = Path("examples/data")
        assert DATA_FOLDER.exists()
        text_path = Path(DATA_FOLDER/"example.txt")
        csv_path = Path(DATA_FOLDER/"example.csv")
        xlsx_path = Path(DATA_FOLDER/"example.xlsx")

        # the mimetype should be valid
        self.assertTrue(FileType.TEXT.is_valid_mime_type(text_path))
        self.assertTrue(FileType.EXCEL.is_valid_mime_type(xlsx_path))

        # the mimetype should be invalid
        self.assertFalse(FileType.TEXT.is_valid_mime_type(xlsx_path))
        self.assertFalse(FileType.EXCEL.is_valid_mime_type(text_path))

        # by checking only the content, all flat files identified as text/plain should match with all possible text/plain formats
        self.assertTrue(FileType.TEXT.is_valid_mime_type(csv_path))
        self.assertTrue(FileType.CSV.is_valid_mime_type(text_path))
    
    def test_from_suffix(self):
        """Test the from_suffix method."""
        self.assertEqual(FileType.from_suffix(".txt"), FileType.TEXT)
        self.assertEqual(FileType.from_suffix(".csv"), FileType.CSV)
        self.assertEqual(FileType.from_suffix(".xlsx"), FileType.EXCEL)
        self.assertEqual(FileType.from_suffix(".json"), FileType.JSON)
        self.assertEqual(FileType.from_suffix(".jpg"), FileType.IMAGE)
        self.assertEqual(FileType.from_suffix(".unknown"), FileType.UNHANDLED)
        self.assertEqual(FileType.from_suffix(""), FileType.NOTYPE)


    def test_unsupported_file_type_error(self):
        """Test UnsupportedFileTypeError exception."""
        with self.assertRaises(UnsupportedFileTypeError):
            FileType.from_suffix("unsupported_extension", raise_err=True)

    def test_empty_suffix_error(self):
        """Test EmptySuffixError exception."""
        with self.assertRaises(EmptySuffixError):
            FileType.from_suffix("", raise_err=True)

if __name__ == "__main__":
    unittest.main()
