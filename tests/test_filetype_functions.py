import unittest
from typing import Set

from opencf_core.filetypes import (
    FileType,
    MimeType,
    get_equivalent_file_types,
    get_file_type_children,
    get_mime_type_children,
)


class TestGetMimeTypeChildren(unittest.TestCase):
    def test_get_file_type_children(self) -> None:
        # Test for IMG_RASTER
        mimetype: MimeType = FileType.IMG_RASTER.value
        all_image_children = get_mime_type_children(mimetype)
        expected_children = {
            FileType.PNG.value,
            FileType.JPEG.value,
            FileType.TIFF.value,
        }
        self.assertEqual(all_image_children, expected_children)

        # Test for TEXT
        text_children: Set[MimeType] = get_mime_type_children(FileType.TEXT.value)
        expected_text_children: Set[MimeType] = set()
        self.assertEqual(text_children, expected_text_children)

        # Test the include_head arg
        mimetype = FileType.TEXT.value
        text_children = get_mime_type_children(mimetype, include_head=True)
        expected_text_children = {mimetype}
        self.assertEqual(text_children, expected_text_children)

        # Add more test cases here...


class TestGetEquivalentFileTypes(unittest.TestCase):
    def test_get_equivalent_file_types(self) -> None:
        # Test with a mix of different MimeTypes
        filetypes: Set[FileType] = {
            FileType.TEXT,
            FileType.JPEG,
            FileType.PNG,
            FileType.PDF,
            FileType.XLSX,
        }
        mime_types: Set[MimeType] = {filetype.value for filetype in filetypes}
        equivalent_types: Set[FileType] = get_equivalent_file_types(mime_types)
        expected_types: Set[FileType] = filetypes
        self.assertEqual(equivalent_types, expected_types)

        # Test with empty set of MimeTypes
        empty_mime_types: Set[MimeType] = set()
        empty_equivalents: Set[FileType] = get_equivalent_file_types(empty_mime_types)
        self.assertEqual(empty_equivalents, set())

        # Add more test cases here...


class TestGetFileTypeChildren(unittest.TestCase):
    def test_include_head_false(self) -> None:
        image_children: Set[FileType] = get_file_type_children(FileType.IMG_RASTER)
        self.assertTrue(FileType.PNG in image_children)
        self.assertTrue(FileType.JPEG in image_children)
        self.assertTrue(FileType.TIFF in image_children)

    def test_include_head_true(self) -> None:
        image_children_with_head: Set[FileType] = get_file_type_children(
            FileType.IMG_RASTER, include_head=True
        )
        self.assertTrue(FileType.IMG_RASTER in image_children_with_head)
        self.assertTrue(FileType.PNG in image_children_with_head)
        self.assertTrue(FileType.JPEG in image_children_with_head)
        self.assertTrue(FileType.TIFF in image_children_with_head)

    def test_notype(self) -> None:
        notype_children: Set[FileType] = get_file_type_children(FileType.NOTYPE)
        self.assertEqual(len(notype_children), 0)


if __name__ == "__main__":
    unittest.main()
