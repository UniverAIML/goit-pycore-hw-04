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
