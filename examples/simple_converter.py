from pathlib import Path
from typing import List

from opencf_core.base_converter import BaseConverter
from opencf_core.file_handler import ResolvedInputFile
from opencf_core.filetypes import FileType
from opencf_core.io_handler import FileWriter, StrToTxtWriter, TxtToStrReader
from opencf_core.logging_config import logger_config

logger_config.set_log_level_str(level="debug")


class TXTToMDConverter(BaseConverter):
    file_reader = TxtToStrReader()
    file_writer = StrToTxtWriter()

    @classmethod
    def _get_supported_input_types(cls) -> FileType:
        return FileType.TEXT

    @classmethod
    def _get_supported_output_types(cls) -> FileType:
        return FileType.MD

    def _convert(self, input_contents: List[str]):
        md_content = "\n".join(input_contents)
        return md_content


class TXTToTXTConverter(BaseConverter):
    file_reader = TxtToStrReader()
    # no file writer means the converter will handle the saving
    folder_as_output = False
    # set it to False to mention, a file (output_file) is going to be save instead of a folder (output_folder)

    @classmethod
    def _get_supported_input_types(cls) -> FileType:
        return FileType.TEXT

    @classmethod
    def _get_supported_output_types(cls) -> FileType:
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

    converter1 = TXTToMDConverter(input_file, output_file)
    converter1.run_conversion()

    converter2 = TXTToTXTConverter(input_file, input_file)
    converter2.run_conversion()
