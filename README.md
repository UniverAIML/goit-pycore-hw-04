# Developer Salary Analyzer

A Python project that analyzes developer salary data from text files and calculates total and average salaries.

## Project Description

This project implements a function `total_salary(path)` that reads salary data from a text file and returns the total and average salary of all developers. The function handles various edge cases and provides comprehensive error handling.

## File Format

The input file should contain salary data in the following format:
```
Developer Name,Salary
Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
```

## Testing

The project includes comprehensive tests covering various boundary conditions:

### Test Cases Covered

1. **Normal Cases:**
   - Valid salary data with multiple records
   - Single record file
   - Files with zero salary values
   - Float salary values
   - Large salary numbers
   - Whitespace handling

2. **Edge Cases:**
   - Empty files
   - Files with only empty lines
   - Files with mixed empty and valid lines

3. **Error Cases:**
   - Non-existent files
   - Invalid salary format (non-numeric)
   - Negative salary values
   - Wrong number of commas per line
   - Empty developer names

## Error Handling

- `File not found`
- `Empty file`
- `Invalid format`: Open on error
- `Negative salary`
- `Empty names`


# Cats Info Analyzer

A Python project that reads cat information from text files and returns structured data as a list of dictionaries.

## Project Description

This project implements a function `get_cats_info(path)` that reads cat data from a text file and returns a list of dictionaries with information about each cat. The function handles various edge cases and provides comprehensive error handling with full type annotations.

## File Format

The input file should contain cat data in the following format:
```
cat_id,cat_name,age
60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
```

Each line contains:
- Cat ID (string, cannot be empty)
- Cat name (string, cannot be empty)
- Age (integer, cannot be negative)

### Expected Output Format

```python
[
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
    {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
]
```

## Test Data Files

- `valid_cats.txt`
- `single_cat.txt`
- `empty_file.txt`
- `invalid_format.txt`
- `empty_fields.txt`
- `negative_age.txt`
- `invalid_age.txt`
- `empty_lines.txt`
- `whitespace_data.txt`
- `zero_age.txt`


# Directory Visualizer
A command-line script that visualizes directory structure with beautiful colored output using tree-like formatting.

**Location**: `directory_visualizer/`

**Features**:
- 🎨 **Colored Output**: Different colors for directories and files
- 📁 **Tree Structure**: Beautiful tree-like visualization with Unicode characters
- 🚀 **Fast Performance**: Efficient recursive directory traversal
- 🛡️ **Error Handling**: Robust error handling for permissions and file access

**Usage**:
```bash
python hw03.py /path/to/directory
```

**Installation**:
```bash
cd directory_visualizer
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```


# Console Bot Assistant

A console bot that manages contacts with names and phone numbers. The bot recognizes commands entered from the keyboard and responds accordingly.

**Location**: `console_bot_assistant/`

**Features**:
- 📞 **Contact Management**: Add, change, and view contacts
- 🔤 **Case Insensitive**: Commands work regardless of case
- ⚠️ **Error Handling**: Proper validation and error messages
- 🔄 **Interactive CLI**: Continuous loop for user interaction
- 🏗️ **Clean Architecture**: Separate functions for each command

**Commands**:
- `hello` - Greet the user
- `add [name] [phone]` - Add a new contact
- `change [name] [phone]` - Change existing contact's phone number
- `phone [name]` - Show phone number for a contact
- `all` - Show all contacts
- `close/exit` - Exit the bot

**Usage**:
```bash
cd console_bot_assistant
python bot.py
```

**Example Session**:
```
Welcome to the assistant bot!
Enter a command: add John 1234567890
Contact added.
Enter a command: phone John
1234567890
Enter a command: all
John: 1234567890
Enter a command: close
Good bye!
```

**Testing**:
```bash
cd console_bot_assistant
python test_bot.py
```
