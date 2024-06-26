# Usage Examples

## Introduction

You can define your own converters like in [simple_converter.py](./simple_converter.py).
Then, you can choose some converter to create a CLI App like done [cli_app_example.py](./cli_app_example.py).
I've added support to add multiple files as input.

## Multiple Files Support

At the beginning, I wanted to get a file and then write another file. Then, I figured, for some conversions (like img to pdf), I may want to send multiple files as input. When the converter only needs one file, it will just get the first element of the list of inputs.

Then, I have extended the functionality to support lists of elements, including:

- **Individual Files:** You can specify individual files directly.
- **Folders:** You can specify a folder, and all files within the folder will be considered.
- **Glob Patterns:** You can use glob patterns to match multiple files based on pattern matching.

This enhancement provides greater flexibility and convenience for batch processing and complex file selection scenarios.

For example, the script below demonstrates how to convert all `.txt` files in a directory to a single output file:

```bash
python examples/cli_app_example.py examples/data/*.txt -o examples/output.txt
```

Similarly, you can specify folders or multiple files directly:

```bash
python examples/cli_app_example.py examples/data/file1.txt examples/data/file2.txt -o examples/output.txt
```

Or specify a folder to include all files within it:

```bash
python examples/cli_app_example.py examples/data/ -o examples/output.txt
```

### Example Usage of TXTToTXTConverter with Enhanced Support

```bash
# Using glob patterns
python examples/cli_app_example.py examples/data/*.txt -o examples/output.txt

# Using a list of files
python examples/cli_app_example.py examples/data/file1.txt examples/data/file2.txt -o examples/output.txt

# Using a folder
python examples/cli_app_example.py examples/data/ -o examples/output.txt

# Combining different types
python examples/cli_app_example.py examples/data/file1.txt examples/data/*.txt -o examples/output.txt
```

## Folder Saving Support

After the multiple files support, I figured, sometimes, for some conversions like (pdf to img), I may want to save multiple files. So, I chose to give more flexibility in the options: output filepath (`-o`) and output file type (`-ot`).

### Setting `-o` as a Folder

You cannot set a folder without adding a valid filetype because the output format needs to be inferred somehow. So, let's proceed under the assumption the filetype (`-ot`) has also been set.

When you set a folder (as `output_path`) and a filetype, the folder would be created and files would be set in it. How does that work?

- When the converter has a writer, only the filepath is used for saving.
- When the converter doesn't have a writer, the folder is sent along with a default filepath inside the folder. So, in the converter, you can choose any option. Below, for example, I use the `output_file` for saving instead of the `output_folder`.

  ```python
  class TXTToTXTConverter(BaseConverter):

      file_reader = TxtToStrReader()
      # no file writer means the converter will handle the saving

      @classmethod
      def _get_supported_input_type(cls) -> FileType:
          return FileType.TEXT

      @classmethod
      def _get_supported_output_type(cls) -> FileType:
          return FileType.TEXT

      def _convert(self, input_contents: List[str], output_file: Path, **kwargs):
          md_content = "\n".join(input_contents)
          output_file.write_text(md_content)
  ```

For example, the script below will save the file `examples/output/opencf-output.md`:

```bash
python examples/cli_app_example.py examples/data/*.txt -o examples/output -ot md
```

### Setting `-o` as a Filepath

When you send an output path that has a suffix (like `myfile.txt`, not `myfile`), the filepath will be sent to the converter.
The output format will be inferred from the filetype (`-ot`) if you set it. Or, it will be inferred from the filepath suffix. If both (the suffix and the output type) are valid formats, they should match, or an error will be raised.

For example, the script below will save the file `output.f`:

```bash
python examples/cli_app_example.py examples/data/*.txt -o examples/output.f -ot md
```

## Usage Example of TXTToTXTConverter to Merge TXT Files

```bash
python examples/cli_app_example.py examples/data/example.txt examples/data/example2.txt -o examples/output.txt -ot txt
# or
find examples -type f -name "*.txt" | xargs python examples/cli_app_example.py -o examples/output.txt -ot txt
# or
python examples/cli_app_example.py examples/data/*.txt -o examples/output.txt
```

## Usage Example of TXTToMDConverter to Merge TXT Files into a MD File

```bash
python examples/cli_app_example.py examples/data/*.txt -o examples/output.md
```

## XLSX to CSV Conversion Example

Below is an example of a converter that reads an XLSX file and converts it to a CSV file.

```python
import sys
from pathlib import Path
from typing import List

import pandas as pd
from opencf_core.base_converter import BaseConverter, ResolvedInputFile
from opencf_core.filetypes import FileType
from opencf_core.io_handler import Reader, ListToCsvWriter

class SpreadsheetToPandasReader(Reader):
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
```

For example, to convert an XLSX file to CSV, run the script as follows:

```bash
python examples/cli_app_example.py examples/data/example.xlsx -o examples/data/example.csv
```

## Abstract `Converter` Class

The `Converter` class provides a structured way to define data converters, including methods to check input and output formats, and perform the conversion. Here's the abstract base class and an example implementation:

### Previous Implementation Approach

Previously, when writing an implementation of `WriterBasedConverter`, one would typically override the `_convert` method directly. Here’s a simplified example to illustrate:

```python
class TXTToTXTConverter(BaseConverter):

    file_reader = TxtToStrReader()
    # no file writer means the converter will handle the saving

    @classmethod
    def _get_supported_input_type(cls) -> FileType:
        return FileType.TEXT

    @classmethod
    def _get_supported_output_type(cls) -> FileType:
        return FileType.TEXT

    def _convert(self, input_contents: List[str], output_file: Path, **kwargs):
        md_content = "\n".join(input_contents)
        output_file.write_text(md_content)
```

In this method:

- The `_convert` method is overridden to implement the conversion logic.
- The input and output formats are defined within the `_convert` method itself.

### New Implementation Approach with `Converter` Class

With the new `Converter` class, the conversion process is broken down into more modular steps:

1. **Checking Input Format**: Ensure that the content meets the expected input format.
2. **Checking Output Format**: Ensure that the content meets the expected output format.
3. **Performing Conversion**: Implement the actual conversion logic.

This structure provides a more robust framework for implementing converters and facilitates better code reuse and readability.

### Example Implementation: `StrToStrConverter`

```python
from typing import List

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
```

### Example Usage: `MDToTXTConverter`

The `MDToTXTConverter` class demonstrates the new approach where an attribute `converters` is defined:

```python
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
```

### Key Differences and Benefits

#### Modularity and Reusability

- **Old Way**: The conversion logic is embedded directly within the `_convert` method, making it less modular and harder to reuse.
- **New Way**: The `Converter` class separates the concerns of checking input/output formats and performing the conversion, promoting modularity and reusability.

#### Clarity and Structure

- **Old Way**: The conversion logic can become cluttered, especially when handling complex conversions involving multiple steps or checks.
- **New Way**: By defining distinct methods for checking formats and performing conversion, the new approach offers a clearer and more structured way to implement converters.

#### Attribute `converters`

- **Old Way**: The `_convert` method must be overridden for each specific converter.
- **New Way**: One can define a list of converter instances in the `converters` attribute, allowing for chaining or combining multiple conversion steps easily.

### Practical Example

To convert markdown files (`.md`) to text files (`.txt`) using the new `MDToTXTConverter`, you would use the following command:

```bash
python examples/cli_app_example.py examples/data/*.md -o examples/output.txt
```

### Summary

The introduction of the abstract `Converter` class offers a more structured and modular approach to defining data converters. By separating the checking of input/output formats and the conversion logic, it enhances code clarity, reusability, and maintainability. The new approach also allows for defining a chain of converters through the `converters` attribute, further improving flexibility in handling complex conversion tasks.

## Summary

Here's a recap of the main points:

- **Custom Converters:** You can define and use custom converters for various data transformation tasks.
- **Multi-file Support:** The application can handle multiple files, folders, and glob patterns as input, providing flexibility for batch processing.
- **Output Options:** The application supports saving output to a specified file or folder, with the ability to infer or specify the output format.
- **Abstract Converter Class:** A structured way to define data converters, with methods to check input and output formats and perform the conversion.
- **Practical Example:** Demonstrated using the `MDToTXTConverter` and `StrToStrConverter` classes to convert markdown files to text files.

By incorporating these features, the CLI application becomes a powerful tool for various file conversion tasks, accommodating complex input and output scenarios.
