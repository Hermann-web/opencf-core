from typing import List

from opencf_core.base_converter import (
    FileAsOutputConversionArgs,
    FileAsOutputConverter,
    WriterBasedConverter,
)
from opencf_core.file_handler import ResolvedInputFile
from opencf_core.filetypes import FileType
from opencf_core.io_handler import Converter, StrToTxtWriter, TxtToStrReader
from opencf_core.logging_config import logger_config

logger_config.set_log_level_str(level="debug")


class StrToStrConverter(Converter):
    def _check_input_format(self, content: List[str]) -> bool:
        return isinstance(content, List) and all(
            isinstance(item, str) for item in content
        )

    def _check_output_format(self, content: str) -> bool:
        return isinstance(content, str)

    def _convert(self, content: List[str]) -> str:
        md_content = "\n".join(content)
        return md_content


class TXTToMDConverter(WriterBasedConverter):
    file_reader = TxtToStrReader()
    file_writer = StrToTxtWriter()

    @classmethod
    def _get_supported_input_types(cls) -> FileType:
        return FileType.TEXT

    @classmethod
    def _get_supported_output_types(cls) -> FileType:
        return FileType.MD

    def _convert(self, input_contents: List[str], args=None):
        md_content = "\n".join(input_contents)
        return md_content


class MDToTXTConverter(WriterBasedConverter):
    file_reader = TxtToStrReader()
    converters = [StrToStrConverter()]
    file_writer = StrToTxtWriter()

    @classmethod
    def _get_supported_input_types(cls) -> FileType:
        return FileType.MD

    @classmethod
    def _get_supported_output_types(cls) -> FileType:
        return FileType.TEXT


class TXTToTXTConverter(FileAsOutputConverter):
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

    def _convert(self, input_contents: List[str], args: FileAsOutputConversionArgs):
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

    converter3 = MDToTXTConverter(output_file, input_file)
    converter3.run_conversion()


if __name__ == "__main__":
    main()
