from typing import Tuple, List, TextIO


def total_salary(path: str) -> Tuple[float, float]:
    """
    Analyzes salary data from a text file and calculates total and average salary.
    
    Args:
        path (str): Path to the text file containing salary data
        
    Returns:
        Tuple[float, float]: A tuple containing (total_salary, average_salary)
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        ValueError: If the file contains invalid data
        RuntimeError: For unexpected errors during processing
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines: List[str] = file.readlines()
        
        # Filter out empty lines
        lines = [line.strip() for line in lines if line.strip()]
        
        if not lines:
            raise ValueError("File is empty or contains no valid data")
        
        total: float = 0.0
        count: int = 0
        
        for line in lines:
            try:
                # Split by comma and validate format
                parts: List[str] = line.split(',')
                if len(parts) != 2:
                    raise ValueError(f"Invalid line format: {line}")
                
                name: str
                salary_str: str
                name, salary_str = parts
                name = name.strip()
                salary_str = salary_str.strip()
                
                # Validate name is not empty
                if not name:
                    raise ValueError(f"Empty name in line: {line}")
                
                # Convert salary to float
                salary: float = float(salary_str)
                
                # Validate salary is non-negative
                if salary < 0:
                    raise ValueError(f"Negative salary not allowed: {salary}")
                
                total += salary
                count += 1
                
            except ValueError as e:
                raise ValueError(f"Error processing line '{line}': {str(e)}")
        
        if count == 0:
            raise ValueError("No valid salary records found")
        
        average: float = total / count
        return (total, average)
        
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")
    except Exception as e:
        if isinstance(e, (ValueError, FileNotFoundError)):
            raise
        else:
            raise RuntimeError(f"Unexpected error processing file: {str(e)}") 
        

total, average = total_salary("test_data/valid_salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")        