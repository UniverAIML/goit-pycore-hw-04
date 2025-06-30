from typing import List, Dict

CatInfo = Dict[str, str]
CatsInfoList = List[CatInfo]


def get_cats_info(path: str) -> CatsInfoList:
    """
    Reads cat information from a text file and returns a list of dictionaries.
    
    Each line in the file should contain: id,name,age
    
    Args:
        path (str): Path to the text file containing cat data
        
    Returns:
        List[Dict[str, str]]: List of dictionaries with keys "id", "name", "age"
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        ValueError: If the file contains invalid data format
        RuntimeError: For unexpected errors during processing
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines: List[str] = file.readlines()
        
        # Filter out empty lines
        lines = [line.strip() for line in lines if line.strip()]
        
        cats_list: CatsInfoList = []
        
        for line_number, line in enumerate(lines, 1):
            try:
                # Split by comma and validate format
                parts: List[str] = line.split(',')
                if len(parts) != 3:
                    raise ValueError(f"Invalid line format (expected 3 fields): {line}")
                
                # Clean whitespace and assign variables
                cat_id: str = parts[0].strip()
                name: str = parts[1].strip()
                age_str: str = parts[2].strip()
                
                # Validate fields are not empty
                if not cat_id:
                    raise ValueError(f"Empty cat ID in line {line_number}: {line}")
                if not name:
                    raise ValueError(f"Empty cat name in line {line_number}: {line}")
                if not age_str:
                    raise ValueError(f"Empty age in line {line_number}: {line}")
                
                # Validate age is numeric and non-negative
                try:
                    age_int: int = int(age_str)
                except ValueError:
                    raise ValueError(f"Invalid age format (must be integer): {age_str}")
                
                if age_int < 0:
                    raise ValueError(f"Age cannot be negative: {age_str}")
                
                # Create and add cat dictionary
                cat_info: CatInfo = {
                    "id": cat_id,
                    "name": name,
                    "age": age_str
                }
                
                cats_list.append(cat_info)
                
            except ValueError as e:
                raise ValueError(f"Error processing line {line_number} '{line}': {str(e)}")
        
        return cats_list
        
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")
    except Exception as e:
        if isinstance(e, (ValueError, FileNotFoundError)):
            raise
        else:
            raise RuntimeError(f"Unexpected error processing file: {str(e)}")


cats_info = get_cats_info("test_data/valid_cats.txt")
print(cats_info) 