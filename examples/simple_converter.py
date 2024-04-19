import sys
from pathlib import Path
from typing import List

sys.path.append(".")

from convcore.base_converter import BaseConverter, ResolvedInputFile
from convcore.filetypes import FileType
from convcore.io_handler import FileReader, StrToTxtWriter, TxtToStrReader


class TXTToMDConverter(BaseConverter):

    file_reader = TxtToStrReader()
    file_writer = StrToTxtWriter()

    @classmethod
    def _get_supported_input_type(cls) -> FileType:
        return FileType.TEXT

    @classmethod
    def _get_supported_output_type(cls) -> FileType:
        return FileType.MARKDOWN

    def _convert(self, input_contents: List[str]):
        md_content = "\n".join(input_contents)
        return md_content


class TXTToTXTConverter(BaseConverter):

    file_reader = TxtToStrReader()
    # no file writer means the converter will handle the saving
    folder_as_output = False
    # set it to False to mention, a file (output_file) is going to be save instead of a folder (output_folder)

    @classmethod
    def _get_supported_input_type(cls) -> FileType:
        return FileType.TEXT

    @classmethod
    def _get_supported_output_type(cls) -> FileType:
        return FileType.TEXT

    def _convert(self, input_contents: List[str], output_file: Path):
        md_content = "\n".join(input_contents)
        output_file.write_text(md_content)


if __name__ == "__main__":
    input_file_path = "examples/data/example.txt"
    output_file_path = "examples/data/example.md"

    input_file = ResolvedInputFile(input_file_path, is_dir=False, should_exist=True)
    output_file = ResolvedInputFile(
        output_file_path, is_dir=False, should_exist=False, add_suffix=True
    )

    converter = TXTToMDConverter(input_file, output_file)
    converter.convert()

    converter = TXTToTXTConverter(input_file, input_file)
    converter.convert()
