import sys
from pathlib import Path
from typing import List

import pandas as pd

sys.path.append(".")

from opencf_core.base_converter import BaseConverter, ResolvedInputFile
from opencf_core.filetypes import FileType
from opencf_core.io_handler import FileReader, ListToCsvWriter


class SpreadsheetToPandasReader(FileReader):
    input_format = pd.DataFrame

    def _check_input_format(self, content: pd.DataFrame):
        return isinstance(content, pd.DataFrame)

    def _read_content(self, input_path: Path) -> pd.DataFrame:
        return pd.read_excel(input_path)


class XLXSToCSVConverter(BaseConverter):

    file_reader = SpreadsheetToPandasReader()
    file_writer = ListToCsvWriter()

    @classmethod
    def _get_supported_input_types(cls) -> FileType:
        return [FileType.XLSX, FileType.XLS]

    @classmethod
    def _get_supported_output_types(cls) -> FileType:
        return FileType.CSV

    def _convert(self, input_contents: List[pd.DataFrame]):

        df = input_contents[0]
        
        # Convert DataFrame to a list of lists
        data_as_list = df.values.tolist()

        # Insert column names as the first sublist
        data_as_list.insert(0, df.columns.tolist())

        return data_as_list


if __name__ == "__main__":
    input_file_path = "examples/data/example.xlsx"
    output_file_path = "examples/data/example.csv"

    input_file = ResolvedInputFile(input_file_path, is_dir=False, should_exist=True)
    output_file = ResolvedInputFile(
        output_file_path, is_dir=False, should_exist=False, add_suffix=True
    )

    converter = XLXSToCSVConverter(input_file, output_file)
    converter.convert()
