import unittest
from pathlib import Path

from opencf_core.exceptions import EmptySuffixError, UnsupportedFileTypeError
from opencf_core.filetypes import FileType, MimeType

DATA_FOLDER = Path(__file__).parent.parent / "examples" / "data"
assert DATA_FOLDER.exists() and DATA_FOLDER.is_dir()


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

        self.assertEqual(FileType.from_path(text_path)[0], FileType.TEXT)
        self.assertEqual(FileType.from_path(csv_path)[0], FileType.CSV)
        self.assertEqual(FileType.from_path(excel_path)[0], FileType.EXCEL)
        self.assertEqual(FileType.from_path(json_path)[0], FileType.JSON)
        self.assertEqual(FileType.from_path(img_path)[0], FileType.IMAGE)
        self.assertEqual(FileType.from_path(Path("no_extension"))[0], FileType.NOTYPE)
        self.assertEqual(FileType.from_path(Path("unknown.xyz"))[0], FileType.UNHANDLED)

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

    def test_get_one_suffix(self):
        """Test the get_suffix method."""
        self.assertEqual(FileType.TEXT.get_one_suffix(), ".txt")
        self.assertEqual(FileType.CSV.get_one_suffix(), ".csv")
        self.assertEqual(FileType.NOTYPE.get_one_suffix(), "")
        self.assertEqual(FileType.UNHANDLED.get_one_suffix(), "")

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
        text_path = Path(DATA_FOLDER / "example.txt")
        csv_path = Path(DATA_FOLDER / "example.csv")
        xlsx_path = Path(DATA_FOLDER / "example.xlsx")
        xml_path = Path(DATA_FOLDER / "example.xml")

        # the mimetype should be valid
        self.assertTrue(FileType.TEXT.is_valid_mime_type(text_path))
        self.assertTrue(FileType.EXCEL.is_valid_mime_type(xlsx_path))
        self.assertTrue(FileType.XML.is_valid_mime_type(xml_path))

        # the mimetype should be invalid
        self.assertFalse(FileType.TEXT.is_valid_mime_type(xlsx_path))
        self.assertFalse(FileType.EXCEL.is_valid_mime_type(text_path))

        # by checking only the content, all flat files identified as text/plain should match with all possible text/plain formats
        # no need actually, while fill up the matches ?
        self.assertFalse(FileType.CSV.is_valid_mime_type(text_path))
        self.assertFalse(FileType.XML.is_valid_mime_type(text_path))
        # text/plain has been added in txt options upper_mime_types,
        # as csv can't be easily deteted i guess
        self.assertTrue(FileType.TEXT.is_valid_mime_type(csv_path))
        # unlike xml
        self.assertFalse(FileType.TEXT.is_valid_mime_type(xml_path))

    def test_from_suffix(self):
        """Test the from_suffix method."""
        self.assertEqual(FileType.from_suffix(".txt")[0], FileType.TEXT)
        self.assertEqual(FileType.from_suffix(".csv")[0], FileType.CSV)
        self.assertEqual(FileType.from_suffix(".xlsx")[0], FileType.EXCEL)
        self.assertEqual(FileType.from_suffix(".json")[0], FileType.JSON)
        self.assertEqual(FileType.from_suffix(".jpg")[0], FileType.IMAGE)
        self.assertEqual(FileType.from_suffix(".xml")[0], FileType.XML)
        self.assertEqual(FileType.from_suffix(".unknown")[0], FileType.UNHANDLED)
        self.assertEqual(FileType.from_suffix("")[0], FileType.NOTYPE)

        # Test with return_matches=True
        self.assertEqual(
            FileType.from_suffix(".txt", return_matches=True),
            (FileType.TEXT, (FileType.TEXT,)),
        )
        self.assertEqual(
            FileType.from_suffix(".unknown", return_matches=True),
            (FileType.UNHANDLED, tuple()),
        )

    def test_from_mimetype(self):
        """Test the from_mimetype method."""
        DATA_FOLDER = Path("examples/data")
        assert DATA_FOLDER.exists()
        text_path = Path(DATA_FOLDER / "example.txt")
        # csv_path = Path(DATA_FOLDER / "example.csv")
        xlsx_path = Path(DATA_FOLDER / "example.xlsx")
        json_path = Path(DATA_FOLDER / "example.json")
        img_path = Path(DATA_FOLDER / "example.jpg")
        xml_path = Path(DATA_FOLDER / "example.xml")

        self.assertEqual(FileType.from_mimetype(text_path)[0], FileType.TEXT)
        # Need to handle csv vs plain
        # self.assertEqual(FileType.from_mimetype(csv_path), (FileType.CSV, (FileType.CSV, FileType.TEXT)))
        self.assertEqual(FileType.from_mimetype(xlsx_path)[0], FileType.EXCEL)
        self.assertEqual(FileType.from_mimetype(json_path)[0], FileType.JSON)
        self.assertEqual(FileType.from_mimetype(img_path)[0], FileType.IMAGE)
        self.assertEqual(FileType.from_mimetype(xml_path)[0], FileType.XML)

        # Test with return_matches=True
        self.assertEqual(
            FileType.from_mimetype(text_path, return_matches=True),
            (FileType.TEXT, (FileType.TEXT,)),
        )
        self.assertEqual(
            FileType.from_mimetype(xml_path, return_matches=True),
            (FileType.XML, (FileType.XML,)),
        )
        # Need to find a file which content is unhandled by the magic moule
        # self.assertEqual(FileType.from_mimetype(DATA_FOLDER / "example.xyz", return_matches=True), (FileType.UNHANDLED, tuple()))

    def test_from_path(self):
        """Test the from_path method."""
        text_path = Path(DATA_FOLDER / "example.txt")
        csv_path = Path(DATA_FOLDER / "example.csv")
        xlsx_path = Path(DATA_FOLDER / "example.xlsx")
        json_path = Path(DATA_FOLDER / "example.json")
        img_path = Path(DATA_FOLDER / "example.jpg")
        xml_path = Path(DATA_FOLDER / "example.xml")

        self.assertEqual(FileType.from_path(text_path)[0], FileType.TEXT)
        self.assertEqual(FileType.from_path(csv_path)[0], FileType.CSV)
        self.assertEqual(FileType.from_path(xlsx_path)[0], FileType.EXCEL)
        self.assertEqual(FileType.from_path(json_path)[0], FileType.JSON)
        self.assertEqual(FileType.from_path(img_path)[0], FileType.IMAGE)
        self.assertEqual(FileType.from_path(xml_path)[0], FileType.XML)

        # Test read_content=True
        self.assertEqual(
            FileType.from_path(text_path, read_content=True)[0], FileType.TEXT
        )
        # Need to handle csv vs plain
        self.assertEqual(
            FileType.from_path(csv_path, read_content=True)[0], FileType.CSV
        )
        self.assertEqual(
            FileType.from_path(xlsx_path, read_content=True)[0], FileType.EXCEL
        )
        self.assertEqual(
            FileType.from_path(json_path, read_content=True)[0], FileType.JSON
        )
        self.assertEqual(
            FileType.from_path(img_path, read_content=True)[0], FileType.IMAGE
        )
        self.assertEqual(
            FileType.from_path(xml_path, read_content=True)[0], FileType.XML
        )

        # Test with return_matches=True
        self.assertEqual(
            FileType.from_path(text_path, return_matches=True),
            (FileType.TEXT, (FileType.TEXT,)),
        )
        self.assertEqual(
            FileType.from_path(Path("examples/data/unknown.xyz"), return_matches=True),
            (FileType.UNHANDLED, tuple()),
        )

    def test_unsupported_file_type_error(self):
        """Test UnsupportedFileTypeError exception."""
        with self.assertRaises(UnsupportedFileTypeError):
            FileType.from_suffix("unsupported_extension", raise_err=True)

    def test_empty_suffix_error(self):
        """Test EmptySuffixError exception."""
        with self.assertRaises(EmptySuffixError):
            FileType.from_suffix("", raise_err=True)

    def test_combined_methods(self):
        """Test combined functionality of multiple methods."""
        text_path = Path("examples/data/example.txt")
        self.assertTrue(FileType.TEXT.is_valid_path(text_path))
        self.assertTrue(FileType.TEXT.is_valid_mime_type(text_path))
        self.assertEqual(FileType.from_suffix(".txt")[0], FileType.TEXT)
        self.assertEqual(FileType.from_mimetype(text_path)[0], FileType.TEXT)
        self.assertEqual(FileType.from_path(text_path)[0], FileType.TEXT)
        self.assertTrue(FileType.TEXT.is_true_filetype())
        self.assertEqual(FileType.TEXT.get_one_suffix(), ".txt")
        self.assertTrue(FileType.TEXT.is_valid_suffix(".txt"))

    def test_get_filetypes(self):
        """Test the get_filetypes method to ensure all filetypes are returned."""
        filetypes = list(FileType.get_filetypes())
        self.assertIn(FileType.TEXT, filetypes)
        self.assertIn(FileType.CSV, filetypes)
        self.assertIn(FileType.EXCEL, filetypes)
        self.assertIn(FileType.JSON, filetypes)
        self.assertIn(FileType.IMAGE, filetypes)
        self.assertIn(FileType.NOTYPE, filetypes)
        self.assertIn(FileType.UNHANDLED, filetypes)

    def test_edge_case_extensions(self):
        """Test edge cases for file extensions."""
        self.assertEqual(FileType.from_suffix(".TXT"), (FileType.TEXT, tuple()))
        self.assertEqual(FileType.from_suffix(".Csv"), (FileType.CSV, tuple()))
        self.assertEqual(FileType.from_suffix(".XLSX"), (FileType.EXCEL, tuple()))
        self.assertEqual(FileType.from_suffix(".JsOn"), (FileType.JSON, tuple()))
        self.assertEqual(FileType.from_suffix(".JPG"), (FileType.IMAGE, tuple()))
        self.assertEqual(FileType.from_suffix(".jpeg"), (FileType.IMAGE, tuple()))
        self.assertEqual(FileType.from_suffix(".docx"), (FileType.MSWORD, tuple()))
        self.assertEqual(FileType.from_suffix(".xml"), (FileType.XML, tuple()))
        self.assertEqual(FileType.from_suffix(".r"), (FileType.UNHANDLED, tuple()))

    def test_invalid_paths(self):
        """Test invalid file paths."""
        self.assertEqual(
            FileType.from_path(Path("nonexistent.file")), (FileType.UNHANDLED, tuple())
        )
        self.assertEqual(
            FileType.from_path(Path("unknown_type.xyz")), (FileType.UNHANDLED, tuple())
        )

    def test_case_insensitivity(self):
        """Test that file type detection is case insensitive."""
        self.assertEqual(FileType.from_suffix(".Txt")[0], FileType.TEXT)
        self.assertEqual(FileType.from_suffix(".CSv")[0], FileType.CSV)
        self.assertEqual(FileType.from_suffix(".Xlsx")[0], FileType.EXCEL)
        self.assertEqual(FileType.from_suffix(".jSoN")[0], FileType.JSON)
        self.assertEqual(FileType.from_suffix(".Jpg")[0], FileType.IMAGE)

    def test_special_characters_in_path(self):
        """Test paths with special characters."""
        special_path = Path("test@file!.txt")
        self.assertEqual(
            FileType.from_path(special_path), (FileType.TEXT, (FileType.TEXT,))
        )

    def test_long_extensions(self):
        """Test file types with long extensions."""
        self.assertEqual(FileType.from_suffix(".tar.gz"), (FileType.UNHANDLED, tuple()))
        self.assertEqual(FileType.from_suffix(".backup"), (FileType.UNHANDLED, tuple()))

    def test_whitespace_in_path(self):
        """Test file paths with leading or trailing whitespace."""
        self.assertEqual(
            FileType.from_path(Path(" test.txt ")), (FileType.UNHANDLED, tuple())
        )
        self.assertEqual(
            FileType.from_path(Path(" data.csv ")), (FileType.UNHANDLED, tuple())
        )

    def test_no_suffix_file(self):
        """Test a file with no suffix."""
        self.assertEqual(
            FileType.from_path(Path("file_with_no_suffix")), (FileType.NOTYPE, tuple())
        )

    # def test_invalid_mime_type(self):
    #     """Test invalid MIME types."""
    #     self.assertEqual(FileType.from_mimetype(Path("invalid_file.fake")), FileType.UNHANDLED)

    def test_from_path_with_nonexistent_file(self):
        """Test from_path method with read_content=True for non-existent files."""
        with self.assertRaises(FileNotFoundError):
            FileType.from_path(Path("nonexistent.txt"), read_content=True)

    def test_from_mimetype_with_nonexistent_file(self):
        """Test from_mimetype method for non-existent files."""
        with self.assertRaises(FileNotFoundError):
            FileType.from_mimetype(Path("nonexistent.txt"))

    # def test_update_file_type_enum(self):
    #     class FileTypeUpdate(Enum):
    #         DOCX = M
    #         XLSX = "xlsx"

    #     extend_filetype_enum(FileTypeUpdate)

    #     new_members = list(FileTypeUpdate)
    #     updated_enum_members = list(FileType)


if __name__ == "__main__":
    unittest.main()
