# Table of Contents

- [opencf_core](#opencf_core)
- [opencf_core.exceptions](#opencf_core.exceptions)
  - [UnsupportedFileTypeError](#opencf_core.exceptions.UnsupportedFileTypeError)
  - [EmptySuffixError](#opencf_core.exceptions.EmptySuffixError)
  - [MismatchedException](#opencf_core.exceptions.MismatchedException)
- [opencf_core.converter_app](#opencf_core.converter_app)
  - [BaseConverterApp](#opencf_core.converter_app.BaseConverterApp)
    - [\_\_init\_\_](#opencf_core.converter_app.BaseConverterApp.__init__)
    - [add_converter_pair](#opencf_core.converter_app.BaseConverterApp.add_converter_pair)
    - [get_converters_for_conversion](#opencf_core.converter_app.BaseConverterApp.get_converters_for_conversion)
    - [get_supported_conversions](#opencf_core.converter_app.BaseConverterApp.get_supported_conversions)
    - [run](#opencf_core.converter_app.BaseConverterApp.run)
- [opencf_core.io_handler](#opencf_core.io_handler)
  - [Reader](#opencf_core.io_handler.Reader)
  - [Writer](#opencf_core.io_handler.Writer)
  - [Converter](#opencf_core.io_handler.Converter)
  - [SamePathReader](#opencf_core.io_handler.SamePathReader)
  - [TxtToStrReader](#opencf_core.io_handler.TxtToStrReader)
  - [StrToTxtWriter](#opencf_core.io_handler.StrToTxtWriter)
  - [XmlToTreeReader](#opencf_core.io_handler.XmlToTreeReader)
  - [TreeToXmlWriter](#opencf_core.io_handler.TreeToXmlWriter)
  - [CsvToDictReader](#opencf_core.io_handler.CsvToDictReader)
  - [DictToCsvWriter](#opencf_core.io_handler.DictToCsvWriter)
  - [JsonToDictReader](#opencf_core.io_handler.JsonToDictReader)
  - [DictToJsonWriter](#opencf_core.io_handler.DictToJsonWriter)
  - [XmlToStrReader](#opencf_core.io_handler.XmlToStrReader)
  - [StrToXmlWriter](#opencf_core.io_handler.StrToXmlWriter)
- [opencf_core.enum](#opencf_core.enum)
  - [extend_enum_with_methods](#opencf_core.enum.extend_enum_with_methods)
- [opencf_core.logging_config](#opencf_core.logging_config)
  - [logging_nameToLevel](#opencf_core.logging_config.logging_nameToLevel)
  - [ColoredFormatter](#opencf_core.logging_config.ColoredFormatter)
  - [LoggerConfig](#opencf_core.logging_config.LoggerConfig)
    - [setup_logger](#opencf_core.logging_config.LoggerConfig.setup_logger)
    - [set_log_file](#opencf_core.logging_config.LoggerConfig.set_log_file)
    - [set_log_level](#opencf_core.logging_config.LoggerConfig.set_log_level)
    - [set_log_level_str](#opencf_core.logging_config.LoggerConfig.set_log_level_str)
- [opencf_core.file_handler](#opencf_core.file_handler)
  - [ResolvedInputFile](#opencf_core.file_handler.ResolvedInputFile)
    - [\_\_init\_\_](#opencf_core.file_handler.ResolvedInputFile.__init__)
    - [\_\_resolve_filetype\_\_](#opencf_core.file_handler.ResolvedInputFile.__resolve_filetype__)
    - [\_\_str\_\_](#opencf_core.file_handler.ResolvedInputFile.__str__)
    - [\_\_repr\_\_](#opencf_core.file_handler.ResolvedInputFile.__repr__)
- [opencf_core.mimes](#opencf_core.mimes)
  - [guess_mime_type_from_file](#opencf_core.mimes.guess_mime_type_from_file)
- [opencf_core.filetypes](#opencf_core.filetypes)
  - [MimeType](#opencf_core.filetypes.MimeType)
  - [merge_mimetype](#opencf_core.filetypes.merge_mimetype)
  - [FileType](#opencf_core.filetypes.FileType)
    - [get_value](#opencf_core.filetypes.FileType.get_value)
    - [get_filetypes](#opencf_core.filetypes.FileType.get_filetypes)
    - [from_suffix](#opencf_core.filetypes.FileType.from_suffix)
    - [from_mimetype](#opencf_core.filetypes.FileType.from_mimetype)
    - [from_path](#opencf_core.filetypes.FileType.from_path)
    - [is_true_filetype](#opencf_core.filetypes.FileType.is_true_filetype)
    - [get_one_suffix](#opencf_core.filetypes.FileType.get_one_suffix)
    - [get_one_mimetype](#opencf_core.filetypes.FileType.get_one_mimetype)
    - [is_valid_suffix](#opencf_core.filetypes.FileType.is_valid_suffix)
    - [is_valid_path](#opencf_core.filetypes.FileType.is_valid_path)
    - [is_valid_mime_type](#opencf_core.filetypes.FileType.is_valid_mime_type)
  - [extract_enum_members](#opencf_core.filetypes.extract_enum_members)
  - [extend_filetype_enum](#opencf_core.filetypes.extend_filetype_enum)
  - [FileTypeExamples](#opencf_core.filetypes.FileTypeExamples)
  - [get_mime_type_children](#opencf_core.filetypes.get_mime_type_children)
  - [get_equivalent_file_types](#opencf_core.filetypes.get_equivalent_file_types)
  - [get_file_type_children](#opencf_core.filetypes.get_file_type_children)
  - [get_file_types_clidren](#opencf_core.filetypes.get_file_types_clidren)
- [opencf_core.base_converter](#opencf_core.base_converter)
  - [InvalidOutputFormatError](#opencf_core.base_converter.InvalidOutputFormatError)
  - [BaseConverter](#opencf_core.base_converter.BaseConverter)
    - [\_\_init\_\_](#opencf_core.base_converter.BaseConverter.__init__)
    - [check_io_handlers](#opencf_core.base_converter.BaseConverter.check_io_handlers)
    - [custom_io_handlers_check](#opencf_core.base_converter.BaseConverter.custom_io_handlers_check)
    - [get_supported_input_types](#opencf_core.base_converter.BaseConverter.get_supported_input_types)
    - [get_supported_output_types](#opencf_core.base_converter.BaseConverter.get_supported_output_types)
    - [run_conversion](#opencf_core.base_converter.BaseConverter.run_conversion)
    - [convert_files](#opencf_core.base_converter.BaseConverter.convert_files)
  - [WriterBasedConverter](#opencf_core.base_converter.WriterBasedConverter)
    - [custom_io_handlers_check](#opencf_core.base_converter.WriterBasedConverter.custom_io_handlers_check)
    - [convert_files](#opencf_core.base_converter.WriterBasedConverter.convert_files)
    - [\_\_get_bad_output_content_solving_tips\_\_](#opencf_core.base_converter.WriterBasedConverter.__get_bad_output_content_solving_tips__)
  - [FileAsOutputConverter](#opencf_core.base_converter.FileAsOutputConverter)
    - [custom_io_handlers_check](#opencf_core.base_converter.FileAsOutputConverter.custom_io_handlers_check)
    - [convert_files](#opencf_core.base_converter.FileAsOutputConverter.convert_files)
  - [FolderAsOutputConverter](#opencf_core.base_converter.FolderAsOutputConverter)
    - [custom_io_handlers_check](#opencf_core.base_converter.FolderAsOutputConverter.custom_io_handlers_check)
    - [convert_files](#opencf_core.base_converter.FolderAsOutputConverter.convert_files)
- [opencf_core.utils](#opencf_core.utils)
  - [get_filepaths_from_inputs](#opencf_core.utils.get_filepaths_from_inputs)
- [examples](#examples)
- [examples.simple_converter](#examples.simple_converter)
- [examples.cli_app_example](#examples.cli_app_example)
  - [main](#examples.cli_app_example.main)

<a id="opencf_core"></a>

# opencf_core

<a id="opencf_core.exceptions"></a>

# opencf_core.exceptions

Classes:

- UnsupportedFileTypeError: Custom exception for handling unsupported file types.
- EmptySuffixError: Specialized exception for cases where a file's suffix does not provide enough information
  to determine its type.
- MismatchedException: Exception for handling cases where there's a mismatch between expected and actual file attributes.

<a id="opencf_core.exceptions.UnsupportedFileTypeError"></a>

## UnsupportedFileTypeError Objects

```python
class UnsupportedFileTypeError(Exception)
```

Exception raised for handling cases of unsupported file types.

<a id="opencf_core.exceptions.EmptySuffixError"></a>

## EmptySuffixError Objects

```python
class EmptySuffixError(UnsupportedFileTypeError)
```

Exception raised when a file's suffix does not provide enough information to determine its type.

<a id="opencf_core.exceptions.MismatchedException"></a>

## MismatchedException Objects

```python
class MismatchedException(Exception)
```

Exception raised for mismatches between expected and actual file attributes.

<a id="opencf_core.converter_app"></a>

# opencf_core.converter_app

Main Module

This module contains the main application logic.

<a id="opencf_core.converter_app.BaseConverterApp"></a>

## BaseConverterApp Objects

```python
class BaseConverterApp()
```

Main application class responsible for managing file conversions.

<a id="opencf_core.converter_app.BaseConverterApp.__init__"></a>

#### \_\_init\_\_

```python
def __init__(input_paths: List[str],
             input_file_type: Optional[str] = None,
             output_file_path: Optional[str] = None,
             output_file_type: Optional[str] = None)
```

Initializes the BaseConverterApp instance.

**Arguments**:

- `input_paths` _List[str]_ - List of paths to the input files.
- `input_file_type` _FileType, optional_ - The type of the input file. Defaults to None.
- `output_file_path` _str, optional_ - The path to the output file. Defaults to None.
- `output_file_type` _FileType, optional_ - The type of the output file. Defaults to None.

<a id="opencf_core.converter_app.BaseConverterApp.add_converter_pair"></a>

#### add_converter_pair

```python
def add_converter_pair(converter_class) -> None
```

Adds a converter pair to the application.

**Arguments**:

- `converter_class` _Type[BaseConverter]_ - The converter class to add.

**Raises**:

- `ValueError` - If the converter class is invalid.

<a id="opencf_core.converter_app.BaseConverterApp.get_converters_for_conversion"></a>

#### get_converters_for_conversion

```python
def get_converters_for_conversion(
        input_type: FileType,
        output_type: FileType) -> List[Type[BaseConverter]]
```

Returns a list of converter classes for a given input-output type pair.

**Arguments**:

- `input_type` _str_ - The input type.
- `output_type` _str_ - The output type.

**Returns**:

- `List[Type[BaseConverter]]` - List of converter classes if found, else an empty list.

<a id="opencf_core.converter_app.BaseConverterApp.get_supported_conversions"></a>

#### get_supported_conversions

```python
def get_supported_conversions() -> Tuple[Tuple[FileType, FileType], ...]
```

Retrieves the supported conversions.

**Returns**:

Tuple[Tuple[FileType, FileType]]: A tuple of tuples representing supported conversions.

<a id="opencf_core.converter_app.BaseConverterApp.run"></a>

#### run

```python
def run() -> None
```

Runs the conversion process.

<a id="opencf_core.io_handler"></a>

# opencf_core.io_handler

Input/Output Handler Module

This module is designed to provide a structured approach to handling file input and output operations across various
formats such as plain text, CSV, JSON, and potentially XML. It introduces a set of abstract base classes and concrete
implementations for reading from and writing to files, ensuring type safety and format consistency through method
signatures and runtime checks.

<a id="opencf_core.io_handler.Reader"></a>

## Reader Objects

```python
class Reader(ABC)
```

Abstract base class for file readers.

<a id="opencf_core.io_handler.Writer"></a>

## Writer Objects

```python
class Writer(ABC)
```

Abstract base class for file writers.

<a id="opencf_core.io_handler.Converter"></a>

## Converter Objects

```python
class Converter(ABC)
```

Abstract base class for data converters.

<a id="opencf_core.io_handler.SamePathReader"></a>

## SamePathReader Objects

```python
class SamePathReader(Reader)
```

A Reader that returns the input path itself, useful for operations where the file path is the desired output.

<a id="opencf_core.io_handler.TxtToStrReader"></a>

## TxtToStrReader Objects

```python
class TxtToStrReader(Reader)
```

Reads content from a text file and returns it as a string.

<a id="opencf_core.io_handler.StrToTxtWriter"></a>

## StrToTxtWriter Objects

```python
class StrToTxtWriter(Writer)
```

Writes a string to a text file.

<a id="opencf_core.io_handler.XmlToTreeReader"></a>

## XmlToTreeReader Objects

```python
class XmlToTreeReader(Reader)
```

Reads content from an XML file and returns it as an ElementTree element.

<a id="opencf_core.io_handler.TreeToXmlWriter"></a>

## TreeToXmlWriter Objects

```python
class TreeToXmlWriter(Writer)
```

Writes content from a dictionary to an XML file.

<a id="opencf_core.io_handler.CsvToDictReader"></a>

## CsvToDictReader Objects

```python
class CsvToDictReader(Reader)
```

Reads content from a CSV file and returns it as a list of dictionaries.

**Example**:

> > > reader = CsvToDictReader()
> > > content = reader.read(Path('input.csv'))
> > > print(content)

- `[{'name'` - 'John', 'age': '30'}, {'name': 'Jane', 'age': '25'}]

<a id="opencf_core.io_handler.DictToCsvWriter"></a>

## DictToCsvWriter Objects

```python
class DictToCsvWriter(Writer)
```

Writes content from a dictionary to a CSV file.

<a id="opencf_core.io_handler.JsonToDictReader"></a>

## JsonToDictReader Objects

```python
class JsonToDictReader(Reader)
```

Reads content from a JSON file and returns it as a dictionary.

<a id="opencf_core.io_handler.DictToJsonWriter"></a>

## DictToJsonWriter Objects

```python
class DictToJsonWriter(Writer)
```

Writes content from a dictionary to a JSON file.

<a id="opencf_core.io_handler.XmlToStrReader"></a>

## XmlToStrReader Objects

```python
class XmlToStrReader(Reader)
```

Reads content from an XML file and returns it as a string.

<a id="opencf_core.io_handler.StrToXmlWriter"></a>

## StrToXmlWriter Objects

```python
class StrToXmlWriter(Writer)
```

Writes content as a string to an XML file.

<a id="opencf_core.enum"></a>

# opencf_core.enum

Dependencies:

- aenum.Enum: For creating the FileType enumeration.

<a id="opencf_core.enum.extend_enum_with_methods"></a>

#### extend_enum_with_methods

```python
def extend_enum_with_methods(inherited_enum: Type[Enum],
                             added_enum: Type[Enum],
                             filter_func: Callable[[Enum], bool]) -> None
```

Extends an Enum class with members and methods from another Enum class based on a filter function.

This function takes three arguments: `inherited_enum`, `added_enum`, and `filter_func`. It adds all the members from
`added_enum` to `inherited_enum` that pass the filter function provided. It also copies all the methods (including
class methods) from both `inherited_enum` and `added_enum` to the extended `inherited_enum` class.

**Arguments**:

- `inherited_enum` _Type[Enum]_ - The Enum class to be extended with new members and methods.
- `added_enum` _Type[Enum]_ - The Enum class whose members and methods will be added to `inherited_enum`.
- `filter_func` _Callable[[Enum], bool]_ - A function that filters which members to add from `added_enum` to `inherited_enum`.

**Returns**:

None

<a id="opencf_core.logging_config"></a>

# opencf_core.logging_config

<a id="opencf_core.logging_config.logging_nameToLevel"></a>

#### logging_nameToLevel

pylint: disable=protected-access

<a id="opencf_core.logging_config.ColoredFormatter"></a>

## ColoredFormatter Objects

```python
class ColoredFormatter(logging.Formatter)
```

- original code from [Sergey Pleshakov, stackoverflow](https://stackoverflow.com/a/56944256/16668046)

<a id="opencf_core.logging_config.LoggerConfig"></a>

## LoggerConfig Objects

```python
class LoggerConfig()
```

<a id="opencf_core.logging_config.LoggerConfig.setup_logger"></a>

#### setup_logger

```python
def setup_logger(name: str,
                 log_file: Optional[str] = None,
                 level: int = logging.INFO) -> None
```

Set up logger.

**Arguments**:

- `name` _str_ - Name of the logger.
- `log_file` _str, optional_ - Path to the log file. Defaults to None.
- `level` _int, optional_ - Logging level. Defaults to logging.INFO.

<a id="opencf_core.logging_config.LoggerConfig.set_log_file"></a>

#### set_log_file

```python
def set_log_file(log_file: str) -> None
```

Set log file.

**Arguments**:

- `log_file` _str_ - Path to the log file.

<a id="opencf_core.logging_config.LoggerConfig.set_log_level"></a>

#### set_log_level

```python
def set_log_level(level: int) -> None
```

Set log level.

**Arguments**:

- `level` _int_ - Logging level.

<a id="opencf_core.logging_config.LoggerConfig.set_log_level_str"></a>

#### set_log_level_str

```python
def set_log_level_str(level: str) -> None
```

Set log level.

**Arguments**:

- `level` _str_ - Logging level.

<a id="opencf_core.file_handler"></a>

# opencf_core.file_handler

Resolved Input File Module

This module provides the ResolvedInputFile class, which manages file paths and types, resolving them as needed.
It supports resolving file types based on paths, optional content reading, and handling both files and directories.

Classes:

- ResolvedInputFile: Manages file paths and types, resolving them as needed.

Exceptions:

- ValueError: Raised when file paths or types are incompatible or unsupported.

<a id="opencf_core.file_handler.ResolvedInputFile"></a>

## ResolvedInputFile Objects

```python
class ResolvedInputFile()
```

Handles resolving the file type of a given file or folder, managing path adjustments and optional content reading.

<a id="opencf_core.file_handler.ResolvedInputFile.__init__"></a>

#### \_\_init\_\_

```python
def __init__(path: Union[str, Path],
             is_dir: Optional[bool] = None,
             should_exist: bool = True,
             file_type: Optional[str] = None,
             add_suffix: bool = False,
             read_content: bool = False,
             filetype_class: Optional[Type[FileType]] = FileType)
```

Initializes an instance of ResolvedInputFile with options for type resolution and path modification.

**Arguments**:

- `path` _str_ - The path to the file or folder.
- `is_dir` _bool, optional_ - Specifies if the path is a directory. If None, inferred using pathlib. Defaults to None.
- `should_exist` _bool, optional_ - Specifies if the existence of the path is required. Defaults to True.
- `file_type` _str, optional_ - The explicit type of the file. If None, attempts to resolve to a filetype object based on the path or content.
- `add_suffix` _bool, optional_ - Whether to append the resolved file type's suffix to the file path. Defaults to False.
- `read_content` _bool, optional_ - Whether to read the file's content to assist in type resolution. Defaults to False.

<a id="opencf_core.file_handler.ResolvedInputFile.__resolve_filetype__"></a>

#### \_\_resolve_filetype\_\_

```python
def __resolve_filetype__(file_type: Optional[str], file_path: Path,
                         read_content: bool) -> FileType
```

Determines the file type, utilizing the provided type, file path, or content as needed.

**Arguments**:

- `file_type` _FileType or str, optional_ - An explicit file type or extension.
- `file_path` _str_ - The path to the file, used if file_type is not provided.
- `read_content` _bool_ - Indicates if file content should be used to help resolve the file type.

**Returns**:

- `FileType` - The resolved file type.

<a id="opencf_core.file_handler.ResolvedInputFile.__str__"></a>

#### \_\_str\_\_

```python
def __str__()
```

Returns the absolute file path as a string.

**Returns**:

- `str` - The resolved file path.

<a id="opencf_core.file_handler.ResolvedInputFile.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__()
```

Returns the absolute file path as a string.

**Returns**:

- `str` - The resolved file path.

<a id="opencf_core.mimes"></a>

# opencf_core.mimes

MIME Type Guesser Module

This module provides a singleton class for guessing MIME types from file paths using the python-magic library.

<a id="opencf_core.mimes.guess_mime_type_from_file"></a>

#### guess_mime_type_from_file

```python
def guess_mime_type_from_file(file_path: Union[str, Path]) -> str
```

Guesses the MIME type from the file path.

**Arguments**:

- `file_path` _str_ - The path to the file.

**Returns**:

- `str` - The guessed MIME type.

<a id="opencf_core.filetypes"></a>

# opencf_core.filetypes

File Type Definitions Module

This module provides a comprehensive framework for handling various file types within a file conversion context.
It defines classes and enumerations for identifying, validating, and working with different file types, based on
file extensions, MIME types, and optionally, file content. It also includes custom exceptions for handling common
errors related to file type processing.

Classes:

- FileType: Enum class that encapsulates various file types supported by the system, providing methods for
  type determination from file attributes.

Dependencies:

- collections.namedtuple: For defining simple classes for storing MIME type information.
- pathlib.Path: For file path manipulations and checks.
- opencf_core.mimes.guess_mime_type_from_file: Utility function to guess MIME type from a file path.

Usage Examples:

```python
from pathlib import Path
from mymodule import FileType, EmptySuffixError, UnsupportedFileTypeError

# Example: Determine file type from suffix
try:
    file_type, _ = FileType.from_suffix('.txt')
    print(f'File type: {file_type.name}')
except (EmptySuffixError, UnsupportedFileTypeError) as e:
    print(f'Error: {e}')

# Example: Determine file type from MIME type
try:
    file_path = Path('/path/to/file.txt')
    file_type, _ = FileType.from_mimetype(file_path)
    print(f'File type: {file_type.name}')
except FileNotFoundError as e:
    print(f'Error: {e}')
except UnsupportedFileTypeError as e:
    print(f'Error: {e}')

# Example: Validate file type by path and content
file_path = Path('/path/to/file.txt')
is_valid = FileType.TEXT.is_valid_path(file_path, read_content=True)
print(f'Is valid: {is_valid}')
```

<a id="opencf_core.filetypes.MimeType"></a>

## MimeType Objects

```python
@dataclass(eq=False, frozen=True)
class MimeType()
```

Class representing MIME type information.

**Attributes**:

- `extensions` _Tuple[str, ...]_ - Tuple of file extensions associated with the MIME type.
- `mime_types` _Tuple[str, ...]_ - Tuple of MIME types.
- `upper_mime_types` _Tuple[str, ...]_ - Tuple of additional MIME types that can be considered equivalent.

<a id="opencf_core.filetypes.merge_mimetype"></a>

#### merge_mimetype

```python
def merge_mimetype(*mimetypes: MimeType) -> MimeType
```

Merge multiple MimeType objects into one.

<a id="opencf_core.filetypes.FileType"></a>

## FileType Objects

```python
class FileType(Enum)
```

Base enumeration for file types, providing methods for type determination and validation.

**Attributes**:

- `NOTYPE` _MimeType_ - Represents an undefined file type (no extensions).
- `TEXT` _MimeType_ - Represents a text file type (.txt).
- `UNHANDLED` _MimeType_ - Represents an unhandled file type (no extensions).
- `CSV` _MimeType_ - Represents a CSV file type (.csv).
- `MARKDOWN` _MimeType_ - Represents a Markdown file type (.md).
- `EXCEL` _MimeType_ - Represents an Excel file type (.xls, .xlsx).
- `MSWORD` _MimeType_ - Represents a Microsoft Word file type (.doc, .docx).
- `JSON` _MimeType_ - Represents a JSON file type (.json).
- `PDF` _MimeType_ - Represents a PDF file type (.pdf).
- `IMAGE` _MimeType_ - Represents an image file type (.jpg, .jpeg, .png).
- `GIF` _MimeType_ - Represents a GIF file type (.gif).
- `VIDEO` _MimeType_ - Represents a video file type (.mp4, .avi).
- `XML` _MimeType_ - Represents a xml file type (.xml).

<a id="opencf_core.filetypes.FileType.get_value"></a>

#### get_value

```python
def get_value() -> MimeType
```

Returns the `MimeType` associated with the enumeration member.

**Returns**:

- `MimeType` - The MIME type information.

<a id="opencf_core.filetypes.FileType.get_filetypes"></a>

#### get_filetypes

```python
@classmethod
def get_filetypes(cls)
```

Yields all valid file types in the enumeration.

<a id="opencf_core.filetypes.FileType.from_suffix"></a>

#### from_suffix

```python
@classmethod
def from_suffix(
        cls,
        suffix: str,
        raise_err: bool = False,
        return_matches: bool = False) -> Tuple[FileType, Tuple[FileType, ...]]
```

Determines a filetype from a file's suffix.

**Arguments**:

- `suffix` _str_ - The file suffix (extension).
- `raise_err` _bool, optional_ - Whether to raise an exception if the type is unhandled. Defaults to False.
- `return_matches` _bool, optional_ - Whether to return a tuple with the first matching filetype and a list of all options. Defaults to False.

**Returns**:

- `FileType` - The determined filetype enumeration member, or a tuple with the first matching filetype and a list of all options.

**Raises**:

- `EmptySuffixError` - If the suffix is empty and raise_err is True.
- `UnsupportedFileTypeError` - If the file type is unhandled and raise_err is True.

<a id="opencf_core.filetypes.FileType.from_mimetype"></a>

#### from_mimetype

```python
@classmethod
def from_mimetype(
        cls,
        file_path: Union[str, Path],
        raise_err: bool = False,
        return_matches: bool = False) -> Tuple[FileType, Tuple[FileType, ...]]
```

Determines a filetype from a file's MIME type.

**Arguments**:

- `file_path` _str_ - The path to the file.
- `raise_err` _bool, optional_ - Whether to raise an exception if the type is unhandled. Defaults to False.
- `return_matches` _bool, optional_ - Whether to return a tuple with the first matching filetype and a list of all options. Defaults to False.

**Returns**:

- `FileType` - The determined filetype enumeration member, or a tuple with the first matching filetype and a list of all options.

**Raises**:

- `FileNotFoundError` - If the file does not exist.
- `UnsupportedFileTypeError` - If the file type is unhandled and raise_err is True.

<a id="opencf_core.filetypes.FileType.from_path"></a>

#### from_path

```python
@classmethod
def from_path(cls,
              path: Union[str, Path],
              read_content=False,
              raise_err=False,
              return_matches=False) -> Tuple[FileType, Tuple[FileType, ...]]
```

Determines the filetype of a file based on its path. Optionally reads the file's content to verify its type.

**Arguments**:

- `path` _Path_ - The path to the file.
- `read_content` _bool, optional_ - If True, the method also checks the file's content to determine its type.
  Defaults to False.
- `raise_err` _bool, optional_ - If True, raises exceptions for unsupported types or when file does not exist.
  Defaults to False.
- `return_matches` _bool, optional_ - Whether to return a tuple with the first matching filetype and a list of all options. Defaults to False.

**Returns**:

- `FileType` - The determined filetype enumeration member based on the file's suffix and/or content, or a tuple with the first matching filetype and a list of all options.

**Raises**:

- `FileNotFoundError` - If the file does not exist when attempting to read its content.
- `UnsupportedFileTypeError` - If the file type is unsupported and raise_err is True.
- `AssertionError` - If there is a mismatch between the file type determined from the file's suffix and its content.

<a id="opencf_core.filetypes.FileType.is_true_filetype"></a>

#### is_true_filetype

```python
def is_true_filetype() -> bool
```

Determines if the filetype instance represents a supported file type based on the presence of defined extensions.

**Returns**:

- `bool` - True if the filetype has at least one associated file extension, False otherwise.

<a id="opencf_core.filetypes.FileType.get_one_suffix"></a>

#### get_one_suffix

```python
def get_one_suffix() -> str
```

Retrieves the primary file extension associated with the filetype.

**Returns**:

- `str` - The primary file extension for the filetype, prefixed with a period.
  Returns an empty string if the filetype does not have an associated extension.

<a id="opencf_core.filetypes.FileType.get_one_mimetype"></a>

#### get_one_mimetype

```python
def get_one_mimetype() -> str
```

Retrieves the primary mimetype associated with the filetype.

**Returns**:

- `Mimetype` - The primary mimetype for the filetype.
  Returns an empty string if the filetype does not have an associated extension.

<a id="opencf_core.filetypes.FileType.is_valid_suffix"></a>

#### is_valid_suffix

```python
def is_valid_suffix(suffix: str, raise_err=False) -> bool
```

Validates whether a given file extension matches the filetype's expected extensions.

**Arguments**:

- `suffix` _str_ - The file extension to validate, including the leading period (e.g., ".txt").
- `raise_err` _bool, optional_ - If True, raises a MismatchedException for invalid extensions.
  Defaults to False.

**Returns**:

- `bool` - True if the suffix matches one of the filetype's extensions, False otherwise.

**Raises**:

- `MismatchedException` - If the suffix does not match the filetype's extensions and raise_err is True.

<a id="opencf_core.filetypes.FileType.is_valid_path"></a>

#### is_valid_path

```python
def is_valid_path(file_path: Union[str, Path],
                  read_content=False,
                  raise_err=False) -> bool
```

Validates the filetype of a given file path. Optionally reads the file's content to verify its type.

**Arguments**:

- `file_path` _Union[str, Path]_ - The file path to validate.
- `read_content` _bool, optional_ - If True, the method also checks the file's content to validate its type.
  Defaults to False.
- `raise_err` _bool, optional_ - If True, raises exceptions for mismatched or unsupported types.
  Defaults to False.

**Returns**:

- `bool` - True if the file path's type matches the filetype, False otherwise.

**Raises**:

- `AssertionError` - If there is a mismatch between the file type determined from the file's suffix and its content.
- `MismatchedException` - If the file type determined from the file's suffix or content does not match the filetype.

<a id="opencf_core.filetypes.FileType.is_valid_mime_type"></a>

#### is_valid_mime_type

```python
def is_valid_mime_type(file_path: Path, raise_err=False) -> bool
```

Validates whether the MIME type of the file at the specified path aligns with the filetype's expected MIME types.

This method first determines the filetype based on the file's actual MIME type (determined by reading the file's content)
and then checks if this determined filetype matches the instance calling this method. Special consideration is given to
filetype.TEXT, where a broader compatibility check is performed due to the generic nature of text MIME types.

**Arguments**:

- `file_path` _Path_ - The path to the file whose MIME type is to be validated.
- `raise_err` _bool, optional_ - If True, a MismatchedException is raised if the file's MIME type does not match
  the expected MIME types of the filetype instance. Defaults to False.

**Returns**:

- `bool` - True if the file's MIME type matches the expected MIME types for this filetype instance or if special
  compatibility conditions are met (e.g., for filetype.TEXT with "text/plain"). Otherwise, False.

**Raises**:

- `MismatchedException` - If raise_err is True and the file's MIME type does not match the expected MIME types
  for this filetype instance, including detailed information about the mismatch.

<a id="opencf_core.filetypes.extract_enum_members"></a>

#### extract_enum_members

```python
def extract_enum_members(enum_cls: Type) -> Dict[str, MimeType]
```

Extracts MimeType instances from an enum class.

**Arguments**:

- `enum_cls` _Type_ - The enum class.

**Returns**:

Dict[str, MimeType]: Dictionary of MimeType instances keyed by enum member names.

<a id="opencf_core.filetypes.extend_filetype_enum"></a>

#### extend_filetype_enum

```python
def extend_filetype_enum(added_enum: Type[Enum]) -> None
```

Extends the BaseFileType enumeration with members from another enumeration.

**Arguments**:

- `added_enum` _Type[Enum]_ - The enum class to extend BaseFileType with.

<a id="opencf_core.filetypes.FileTypeExamples"></a>

## FileTypeExamples Objects

```python
class FileTypeExamples(Enum)
```

Enumeration of supported file types with methods for type determination and validation.

<a id="opencf_core.filetypes.get_mime_type_children"></a>

#### get_mime_type_children

```python
def get_mime_type_children(mime_type: MimeType,
                           include_head: bool = False) -> Set[MimeType]
```

Recursively get all children MIME types in the subtree of the given MIME type.

**Arguments**:

- `mime_type` _MimeType_ - The MIME type to get the subtree for.
- `include_head` _bool, optional_ - Controls whether to include the head node in the result. Defaults to False.

**Returns**:

- `Set[MimeType]` - A set of all MIME types in the subtree.

**Example**:

> > > all_image_children = get_mime_type_children(MimeType(extensions=('png',), mime_types=('image/png',), upper_mime_types=(), children_mime_types=()))
> > > print(all_image_children)
> > > {MimeType(extensions=('png',), mime_types=('image/png',), upper_mime_types=(), children_mime_types=()),
> > > MimeType(extensions=('jpeg', 'jpg'), mime_types=('image/jpeg',), upper_mime_types=(), children_mime_types=()),
> > > MimeType(extensions=('tiff',), mime_types=('image/tiff',), upper_mime_types=(), children_mime_types=())}

<a id="opencf_core.filetypes.get_equivalent_file_types"></a>

#### get_equivalent_file_types

```python
def get_equivalent_file_types(mime_types: Set[MimeType],
                              raise_error: bool = True) -> Set[FileType]
```

Get the equivalent FileTypes for a given list of MimeTypes.

**Arguments**:

- `mime_types` _Set[MimeType]_ - The list of MIME types to find the equivalent FileTypes for.
- `raise_error` _bool, optional_ - Controls whether to raise an error if no equivalent FileType is found. Defaults to True.

**Returns**:

- `List[FileType]` - A list of equivalent FileTypes if found, otherwise None.

<a id="opencf_core.filetypes.get_file_type_children"></a>

#### get_file_type_children

```python
def get_file_type_children(file_type: FileType,
                           include_head: bool = False) -> Set[FileType]
```

Recursively get all children FileTypes as equivalent FileTypes of the MIME types in the subtree of the given FileType.

**Arguments**:

- `file_type` _FileType_ - The FileType to get the subtree for.
- `include_head` _bool, optional_ - Controls whether to include the head node in the result. Defaults to False.

**Returns**:

- `Set[FileType]` - A set of all equivalent FileTypes in the subtree.

**Example**:

> > > all_image_children = get_file_type_children(FileType.IMG_RASTER)
> > > print(all_image_children)
> > > {FileType.PNG, FileType.JPEG, FileType.TIFF}

<a id="opencf_core.filetypes.get_file_types_clidren"></a>

#### get_file_types_clidren

```python
def get_file_types_clidren(file_types: Iterable[FileType],
                           include_head: bool = False) -> Set[FileType]
```

Recursively get all children FileTypes as equivalent FileTypes of the MIME types
in the subtree of the given list of FileType instances.

**Arguments**:

- `file_types` _List[FileType]_ - The list of FileType instances to get the subtree for.
- `include_head` _bool, optional_ - Controls whether to include the head node in the result. Defaults to False.

**Returns**:

- `Set[FileType]` - A set of all equivalent FileTypes in the subtree.

**Example**:

> > > all_image_children = get_file_types_from_list([FileType.IMG_RASTER])
> > > print(all_image_children)
> > > {FileType.PNG, FileType.JPEG, FileType.TIFF}

<a id="opencf_core.base_converter"></a>

# opencf_core.base_converter

Base Converter Module

This module serves as a foundation for creating file conversion utilities. It facilitates the development
of file converters through abstract base classes, managing file types, and handling input and output files
efficiently. The module is designed to be extendible, supporting various file formats and conversion strategies.

Classes:

- BaseConverter: An abstract base class for creating specific file format converters, enforcing the implementation of file conversion logic.

Exceptions:

- ValueError: Raised when file paths or types are incompatible or unsupported.
- AssertionError: Ensured for internal consistency checks, confirming that file types match expected values.

<a id="opencf_core.base_converter.InvalidOutputFormatError"></a>

## InvalidOutputFormatError Objects

```python
class InvalidOutputFormatError(Exception)
```

Exception raised when the output content format check fails after conversion.

<a id="opencf_core.base_converter.BaseConverter"></a>

## BaseConverter Objects

```python
class BaseConverter(ABC, Generic[T])
```

Abstract base class for file conversion, defining the template for input to output file conversion.

<a id="opencf_core.base_converter.BaseConverter.__init__"></a>

#### \_\_init\_\_

```python
def __init__(input_files: Union[ResolvedInputFile, List[ResolvedInputFile]],
             output_file: ResolvedInputFile)
```

Sets up the converter with specified input and output files, ensuring compatibility.

**Arguments**:

- `input_files` _Union[ResolvedInputFile, List[ResolvedInputFile]]_ - Either a single input file or a list of input files with resolved types.
- `output_file` _ResolvedInputFile_ - The output file where the converted data will be saved.

<a id="opencf_core.base_converter.BaseConverter.check_io_handlers"></a>

#### check_io_handlers

```python
def check_io_handlers()
```

Ensures that valid I/O handlers (file reader and writer) are set for the conversion.

<a id="opencf_core.base_converter.BaseConverter.custom_io_handlers_check"></a>

#### custom_io_handlers_check

```python
@abstractmethod
def custom_io_handlers_check()
```

Custom IO handlers check method. Subclasses should implement this method to ensure proper IO handlers are set.

<a id="opencf_core.base_converter.BaseConverter.get_supported_input_types"></a>

#### get_supported_input_types

```python
@classmethod
def get_supported_input_types(cls) -> Tuple[FileType, ...]
```

Defines the supported input file types for this converter.

**Returns**:

- `Tuple[FileType]` - The file types supported for input.

<a id="opencf_core.base_converter.BaseConverter.get_supported_output_types"></a>

#### get_supported_output_types

```python
@classmethod
def get_supported_output_types(cls) -> Tuple[FileType, ...]
```

Defines the supported output file types for this converter.

**Returns**:

- `Tuple[FileType]` - The file types supported for output.

<a id="opencf_core.base_converter.BaseConverter.run_conversion"></a>

#### run_conversion

```python
def run_conversion()
```

Orchestrates the file conversion process, including reading, converting, and writing the file.

<a id="opencf_core.base_converter.BaseConverter.convert_files"></a>

#### convert_files

```python
@abstractmethod
def convert_files(output_path: Path)
```

Abstract method to be implemented by subclasses to handle file conversion process.

<a id="opencf_core.base_converter.WriterBasedConverter"></a>

## WriterBasedConverter Objects

```python
class WriterBasedConverter(BaseConverter[None])
```

<a id="opencf_core.base_converter.WriterBasedConverter.custom_io_handlers_check"></a>

#### custom_io_handlers_check

```python
def custom_io_handlers_check()
```

Check if the file writer is valid.

<a id="opencf_core.base_converter.WriterBasedConverter.convert_files"></a>

#### convert_files

```python
def convert_files(output_path: Path)
```

Convert input files to output content and save the output to the specified path.

**Arguments**:

- `output_path`: The path where the converted output file will be saved.

**Returns**:

The path where the output file was saved.

<a id="opencf_core.base_converter.WriterBasedConverter.__get_bad_output_content_solving_tips__"></a>

#### \_\_get_bad_output_content_solving_tips\_\_

```python
def __get_bad_output_content_solving_tips__() -> str
```

Provide tips to solve issues with bad output content.

**Returns**:

Tips to solve issues with bad output content.

<a id="opencf_core.base_converter.FileAsOutputConverter"></a>

## FileAsOutputConverter Objects

```python
class FileAsOutputConverter(BaseConverter[FileAsOutputConversionArgs])
```

<a id="opencf_core.base_converter.FileAsOutputConverter.custom_io_handlers_check"></a>

#### custom_io_handlers_check

```python
def custom_io_handlers_check()
```

Check if the file writer and folder output settings are valid.

<a id="opencf_core.base_converter.FileAsOutputConverter.convert_files"></a>

#### convert_files

```python
def convert_files(output_path: Path)
```

Convert input files to output content and save the output to the specified file path.

**Arguments**:

- `output_path`: The path where the converted output file will be saved.

**Returns**:

The path where the output file was saved.

<a id="opencf_core.base_converter.FolderAsOutputConverter"></a>

## FolderAsOutputConverter Objects

```python
class FolderAsOutputConverter(BaseConverter[FolderAsOutputConversionArgs])
```

<a id="opencf_core.base_converter.FolderAsOutputConverter.custom_io_handlers_check"></a>

#### custom_io_handlers_check

```python
def custom_io_handlers_check()
```

Check if the file writer and folder output settings are valid.

<a id="opencf_core.base_converter.FolderAsOutputConverter.convert_files"></a>

#### convert_files

```python
def convert_files(output_path: Path)
```

Convert input files to output content and save the output to the specified folder path.

**Arguments**:

- `output_path`: The path where the converted output folder will be saved.

**Returns**:

The path where the output folder was saved.

<a id="opencf_core.utils"></a>

# opencf_core.utils

<a id="opencf_core.utils.get_filepaths_from_inputs"></a>

#### get_filepaths_from_inputs

```python
def get_filepaths_from_inputs(args: List[str]) -> List[str]
```

Generate a list of file paths from a list of command-line arguments.

**Arguments**:

- `args` _list of str_ - List of command-line arguments including file paths, directory paths, and glob patterns.

**Returns**:

list of str: List of file paths that match the input criteria.

<a id="examples"></a>

# examples

<a id="examples.simple_converter"></a>

# examples.simple_converter

<a id="examples.cli_app_example"></a>

# examples.cli_app_example

Main Module

This module contains the main application logic.

<a id="examples.cli_app_example.main"></a>

#### main

```python
def main()
```

**Usage Example**

## Usage Example of TXTToTXTConverter to merge txt files

```bash
find examples -type f -name "*.txt" | xargs python examples/cli_app_example.py -o examples/output -ot txt
# or
python examples/cli_app_example.py examples/cli_app_example.py examples/data/example.txt -o examples/output -ot txt
# or
python examples/cli_app_example.py examples/data/example.txt  examples/data/example2.txt -o examples/output/example.txt
```

## Usage Examples of TXTToMDConverter to merge txt files into a md file

```bash
find examples -type f -name "*.txt" | xargs python examples/cli_app_example.py -o examples/output.md
```
