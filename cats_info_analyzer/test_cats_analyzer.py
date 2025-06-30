import unittest
import os
import tempfile
from typing import List, Dict
from cats_analyzer import get_cats_info, CatsInfoList


class TestCatsAnalyzer(unittest.TestCase):
    """Test suite for the cats analyzer functions covering various boundary conditions."""
    
    def setUp(self) -> None:
        """Set up test fixtures before each test method."""
        self.test_data_dir: str = "test_data"
    
    def test_valid_cats_normal_case(self) -> None:
        """Test with valid cat data - normal case."""
        file_path: str = os.path.join(self.test_data_dir, "valid_cats.txt")
        cats_info: CatsInfoList = get_cats_info(file_path)
        
        expected_cats: CatsInfoList = [
            {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
            {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
            {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
            {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
            {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
        ]
        
        self.assertEqual(len(cats_info), 5)
        self.assertEqual(cats_info, expected_cats)
    
    def test_single_cat(self) -> None:
        """Test with file containing single cat record."""
        file_path: str = os.path.join(self.test_data_dir, "single_cat.txt")
        cats_info: CatsInfoList = get_cats_info(file_path)
        
        expected_cat: Dict[str, str] = {
            "id": "60b90c1c13067a15887e1ae1", 
            "name": "Fluffy", 
            "age": "7"
        }
        
        self.assertEqual(len(cats_info), 1)
        self.assertEqual(cats_info[0], expected_cat)
    
    def test_empty_file(self) -> None:
        """Test with empty file - should return empty list."""
        file_path: str = os.path.join(self.test_data_dir, "empty_file.txt")
        cats_info: CatsInfoList = get_cats_info(file_path)
        
        self.assertEqual(cats_info, [])
        self.assertEqual(len(cats_info), 0)
    
    def test_file_not_found(self) -> None:
        """Test with non-existent file - should raise FileNotFoundError."""
        file_path: str = "non_existent_file.txt"
        
        with self.assertRaises(FileNotFoundError):
            get_cats_info(file_path)
    
    def test_invalid_format(self) -> None:
        """Test with invalid format - should raise ValueError."""
        file_path: str = os.path.join(self.test_data_dir, "invalid_format.txt")
        
        with self.assertRaises(ValueError) as context:
            get_cats_info(file_path)
        
        self.assertIn("Invalid line format", str(context.exception))
    
    def test_empty_fields(self) -> None:
        """Test with empty fields - should raise ValueError."""
        file_path: str = os.path.join(self.test_data_dir, "empty_fields.txt")
        
        with self.assertRaises(ValueError) as context:
            get_cats_info(file_path)
        
        error_msg: str = str(context.exception).lower()
        self.assertTrue(
            "empty cat id" in error_msg or 
            "empty cat name" in error_msg or 
            "empty age" in error_msg
        )
    
    def test_negative_age(self) -> None:
        """Test with negative age - should raise ValueError."""
        file_path: str = os.path.join(self.test_data_dir, "negative_age.txt")
        
        with self.assertRaises(ValueError) as context:
            get_cats_info(file_path)
        
        self.assertIn("cannot be negative", str(context.exception))
    
    def test_invalid_age_format(self) -> None:
        """Test with non-numeric age - should raise ValueError."""
        file_path: str = os.path.join(self.test_data_dir, "invalid_age.txt")
        
        with self.assertRaises(ValueError) as context:
            get_cats_info(file_path)
        
        self.assertIn("Invalid age format", str(context.exception))
    
    def test_empty_lines_handling(self) -> None:
        """Test file with empty lines mixed with valid data."""
        file_path: str = os.path.join(self.test_data_dir, "empty_lines.txt")
        cats_info: CatsInfoList = get_cats_info(file_path)
        
        expected_cats: CatsInfoList = [
            {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
            {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
            {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
        ]
        
        self.assertEqual(len(cats_info), 3)
        self.assertEqual(cats_info, expected_cats)
    
    def test_whitespace_handling(self) -> None:
        """Test with whitespace around data."""
        file_path: str = os.path.join(self.test_data_dir, "whitespace_data.txt")
        cats_info: CatsInfoList = get_cats_info(file_path)
        
        expected_cats: CatsInfoList = [
            {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
            {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
            {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
        ]
        
        self.assertEqual(len(cats_info), 3)
        self.assertEqual(cats_info, expected_cats)
    
    def test_zero_age(self) -> None:
        """Test with zero age cats - should work correctly."""
        file_path: str = os.path.join(self.test_data_dir, "zero_age.txt")
        cats_info: CatsInfoList = get_cats_info(file_path)
        
        expected_cats: CatsInfoList = [
            {"id": "60b90c1c13067a15887e1ae1", "name": "Kitten", "age": "0"},
            {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
            {"id": "60b90c2e13067a15887e1ae3", "name": "Baby Cat", "age": "0"},
        ]
        
        self.assertEqual(len(cats_info), 3)
        self.assertEqual(cats_info, expected_cats)
    
    def test_large_dataset(self) -> None:
        """Test with large dataset using temporary file."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8') as temp_file:
            # Create 100 cat records
            for i in range(100):
                temp_file.write(f"id_{i:03d},Cat_{i},{i % 20}\n")
            temp_file_path: str = temp_file.name
        
        try:
            cats_info: CatsInfoList = get_cats_info(temp_file_path)
            
            self.assertEqual(len(cats_info), 100)
            
            # Check first and last records
            first_cat: Dict[str, str] = cats_info[0]
            self.assertEqual(first_cat["id"], "id_000")
            self.assertEqual(first_cat["name"], "Cat_0")
            self.assertEqual(first_cat["age"], "0")
            
            last_cat: Dict[str, str] = cats_info[-1]
            self.assertEqual(last_cat["id"], "id_099")
            self.assertEqual(last_cat["name"], "Cat_99")
            self.assertEqual(last_cat["age"], "19")
            
        finally:
            os.unlink(temp_file_path)
    
    def test_special_characters_in_names(self) -> None:
        """Test with special characters in cat names using temporary file."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8') as temp_file:
            temp_file.write("id1,Mr. Whiskers,3\n")
            temp_file.write("id2,Señor Gato,5\n")
            temp_file.write("id3,Cat-in-Hat,2\n")
            temp_file.write("id4,Мурзик,4\n")  # Cyrillic name
            temp_file_path: str = temp_file.name
        
        try:
            cats_info: CatsInfoList = get_cats_info(temp_file_path)
            
            self.assertEqual(len(cats_info), 4)
            self.assertEqual(cats_info[0]["name"], "Mr. Whiskers")
            self.assertEqual(cats_info[1]["name"], "Señor Gato") 
            self.assertEqual(cats_info[2]["name"], "Cat-in-Hat")
            self.assertEqual(cats_info[3]["name"], "Мурзик")
            
        finally:
            os.unlink(temp_file_path)
    



def run_all_tests() -> bool:
    """Run all tests and display results."""
    # Change to the directory containing the test files
    test_dir: str = os.path.dirname(os.path.abspath(__file__))
    os.chdir(test_dir)
    
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCatsAnalyzer)
    runner = unittest.TextTestRunner(verbosity=2)
    
    print("Running comprehensive tests for cats analyzer functions...")
    print("=" * 60)
    
    result = runner.run(suite)
    
    print("\n" + "=" * 60)
    if result.wasSuccessful():
        print("✅ All tests passed successfully!")
    else:
        print(f"❌ {len(result.failures + result.errors)} test(s) failed.")
        
    return result.wasSuccessful()


if __name__ == "__main__":
    run_all_tests() 