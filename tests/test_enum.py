import unittest

from opencf_core.enum import Enum, extend_enum_with_methods
from opencf_core.filetypes import FileType, MimeType


class TestExtendEnumMethods(unittest.TestCase):
    def test_extend_enum_methods(self):
        # Create a new Enum class with two mimetype members
        new_file_type = Enum(
            "NewFileType",
            {
                "new_file_type1": MimeType(("json",), ("application/json",)),
                "new_file_type2": MimeType(("pdf",), ("application/pdf",)),
            },
        )

        # add two methods
        setattr(new_file_type, "method1", lambda x: 0)
        setattr(new_file_type, "method2", lambda x: 0)

        # Define a filter function
        def filter_func(member):
            return isinstance(member.value, MimeType)

        # Extend the FileType Enum with the new Enum and filter function
        extend_enum_with_methods(FileType, new_file_type, filter_func)

        # Check if the new Enum members were added
        self.assertIn("new_file_type1", FileType.__members__)
        self.assertIn("new_file_type2", FileType.__members__)

        # Check if the methods were copied
        self.assertTrue(hasattr(FileType, "method1"))
        self.assertTrue(hasattr(FileType, "method2"))


if __name__ == "__main__":
    unittest.main()
