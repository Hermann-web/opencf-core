import unittest
from pathlib import Path

from opencf_core.mimes import guess_mime_type_from_file


class TestMimeGuesser(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.data_dir = Path(__file__).parent.parent / "examples/data"
        assert self.data_dir.exists() and self.data_dir.is_dir()

    def test_text_file(self):
        self.assertEqual(
            guess_mime_type_from_file(self.data_dir / "example.txt"), "text/plain"
        )

    def test_csv_file(self):
        self.assertIn(
            guess_mime_type_from_file(self.data_dir / "example.csv"),
            ("text/csv", "text/plain"),
        )

    def test_markdown_file(self):
        self.assertIn(
            guess_mime_type_from_file(self.data_dir / "example.md"),
            ("text/markdown", "text/plain"),
        )

    def test_excel_file(self):
        self.assertIn(
            guess_mime_type_from_file(self.data_dir / "example.xlsx"),
            (
                "application/octet-stream",
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            ),
        )
        # self.assertIn(guess_mime_type_from_file(self.data_dir / 'example.xls'), ('application/octet-stream', 'application/vnd.ms-excel'))

    def test_msword_file(self):
        self.assertIn(
            guess_mime_type_from_file(self.data_dir / "example.docx"),
            (
                "application/octet-stream",
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            ),
        )
        # self.assertIn(guess_mime_type_from_file(self.data_dir / 'example.doc'), ('application/octet-stream', 'application/msword'))

    def test_json_file(self):
        self.assertEqual(
            guess_mime_type_from_file(self.data_dir / "example.json"),
            "application/json",
        )

    def test_pdf_file(self):
        self.assertEqual(
            guess_mime_type_from_file(self.data_dir / "example.pdf"), "application/pdf"
        )

    def test_image_file(self):
        self.assertEqual(
            guess_mime_type_from_file(self.data_dir / "example.jpg"), "image/jpeg"
        )
        self.assertEqual(
            guess_mime_type_from_file(self.data_dir / "example.png"), "image/png"
        )

    # def test_gif_file(self):
    #     self.assertEqual(guess_mime_type_from_file(self.data_dir / 'example.gif'), 'image/gif')

    # def test_video_file(self):
    #     self.assertEqual(guess_mime_type_from_file(self.data_dir / 'example.mp4'), 'video/mp4')
    #     self.assertEqual(guess_mime_type_from_file(self.data_dir / 'example.avi'), 'video/x-msvideo')

    # def test_unhandled_file(self):
    #     self.assertEqual(guess_mime_type_from_file(self.data_dir / 'example.unknown'), 'application/octet-stream')


if __name__ == "__main__":
    unittest.main()
