from typing import List

from opencf_core.base_converter import (
    FileConversionArgs,
    FileOutputConverter,
    WriterConverter,
)
from opencf_core.file_handler import ResolvedInputFile
from opencf_core.filetypes import FileType
from opencf_core.io_handler import StrToTxtWriter, TxtToStrReader
from opencf_core.logging_config import logger_config

logger_config.set_log_level_str(level="debug")


class TXTToMDConverter(WriterConverter):
    file_reader = TxtToStrReader()
    file_writer = StrToTxtWriter()

    @classmethod
    def _get_supported_input_types(cls) -> FileType:
        return FileType.TEXT

    @classmethod
    def _get_supported_output_types(cls) -> FileType:
        return FileType.MD

    def _convert(self, input_contents: List[str], _=None):
        md_content = "\n".join(input_contents)
        return md_content


class TXTToTXTConverter(FileOutputConverter):
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

    def _convert(self, input_contents: List[str], args: FileConversionArgs):
        output_file = args.output_file
        md_content = "\n".join(input_contents)
        output_file.write_text(md_content)


def main():
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


if __name__ == "__main__":
    main()
