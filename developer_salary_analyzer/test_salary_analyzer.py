import unittest
import os
import tempfile
from salary_analyzer import total_salary


class TestTotalSalary(unittest.TestCase):
    """Test suite for the total_salary function covering various boundary conditions."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.test_data_dir = "test_data"
    
    def test_valid_salaries_normal_case(self):
        """Test with valid salary data - normal case."""
        file_path = os.path.join(self.test_data_dir, "valid_salaries.txt")
        total, average = total_salary(file_path)
        
        expected_total = 3000 + 2000 + 1000 + 4500 + 3200 + 2800 + 3700 + 2100 + 4000 + 3300
        expected_average = expected_total / 10
        
        self.assertEqual(total, expected_total)
        self.assertEqual(average, expected_average)
    
    def test_single_record(self):
        """Test with file containing single salary record."""
        file_path = os.path.join(self.test_data_dir, "single_record.txt")
        total, average = total_salary(file_path)
        
        self.assertEqual(total, 5000)
        self.assertEqual(average, 5000)
    
    def test_empty_file(self):
        """Test with empty file - should raise ValueError."""
        file_path = os.path.join(self.test_data_dir, "empty_file.txt")
        
        with self.assertRaises(ValueError) as context:
            total_salary(file_path)
        
        self.assertIn("empty", str(context.exception).lower())
    
    def test_file_not_found(self):
        """Test with non-existent file - should raise FileNotFoundError."""
        file_path = "non_existent_file.txt"
        
        with self.assertRaises(FileNotFoundError):
            total_salary(file_path)
    
    def test_invalid_salary_format(self):
        """Test with invalid salary format - should raise ValueError."""
        file_path = os.path.join(self.test_data_dir, "invalid_format.txt")
        
        with self.assertRaises(ValueError) as context:
            total_salary(file_path)
        
        self.assertIn("invalid_salary", str(context.exception))
    
    def test_empty_lines_handling(self):
        """Test file with empty lines mixed with valid data."""
        file_path = os.path.join(self.test_data_dir, "empty_lines.txt")
        total, average = total_salary(file_path)
        
        expected_total = 2500 + 3000 + 1800
        expected_average = expected_total / 3
        
        self.assertEqual(total, expected_total)
        self.assertEqual(average, expected_average)
    
    def test_negative_salary(self):
        """Test with negative salary values - should raise ValueError."""
        file_path = os.path.join(self.test_data_dir, "negative_salary.txt")
        
        with self.assertRaises(ValueError) as context:
            total_salary(file_path)
        
        self.assertIn("negative", str(context.exception).lower())
    
    def test_wrong_comma_count(self):
        """Test with wrong number of commas per line - should raise ValueError."""
        file_path = os.path.join(self.test_data_dir, "wrong_comma_count.txt")
        
        with self.assertRaises(ValueError) as context:
            total_salary(file_path)
        
        self.assertIn("invalid line format", str(context.exception).lower())
    
    def test_empty_name(self):
        """Test with empty names - should raise ValueError."""
        file_path = os.path.join(self.test_data_dir, "empty_name.txt")
        
        with self.assertRaises(ValueError) as context:
            total_salary(file_path)
        
        self.assertIn("empty name", str(context.exception).lower())
    
    def test_zero_salary(self):
        """Test with zero salary values - should work correctly."""
        file_path = os.path.join(self.test_data_dir, "zero_salary.txt")
        total, average = total_salary(file_path)
        
        expected_total = 0 + 3000 + 0 + 2500
        expected_average = expected_total / 4
        
        self.assertEqual(total, expected_total)
        self.assertEqual(average, expected_average)
    
    def test_float_salaries(self):
        """Test with float salary values using temporary file."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_file:
            temp_file.write("John Doe,2500.50\n")
            temp_file.write("Jane Smith,3000.75\n")
            temp_file.write("Bob Johnson,1999.25\n")
            temp_file_path = temp_file.name
        
        try:
            total, average = total_salary(temp_file_path)
            expected_total = 2500.50 + 3000.75 + 1999.25
            expected_average = expected_total / 3
            
            self.assertAlmostEqual(total, expected_total, places=2)
            self.assertAlmostEqual(average, expected_average, places=2)
        finally:
            os.unlink(temp_file_path)
    
    def test_large_salaries(self):
        """Test with large salary values using temporary file."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_file:
            temp_file.write("CEO,1000000\n")
            temp_file.write("CTO,500000\n")
            temp_file_path = temp_file.name
        
        try:
            total, average = total_salary(temp_file_path)
            expected_total = 1000000 + 500000
            expected_average = expected_total / 2
            
            self.assertEqual(total, expected_total)
            self.assertEqual(average, expected_average)
        finally:
            os.unlink(temp_file_path)
    
    def test_whitespace_handling(self):
        """Test with whitespace around names and salaries using temporary file."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_file:
            temp_file.write("  John Doe  ,  3000  \n")
            temp_file.write(" Jane Smith , 2000 \n")
            temp_file_path = temp_file.name
        
        try:
            total, average = total_salary(temp_file_path)
            expected_total = 3000 + 2000
            expected_average = expected_total / 2
            
            self.assertEqual(total, expected_total)
            self.assertEqual(average, expected_average)
        finally:
            os.unlink(temp_file_path)


def run_all_tests():
    """Run all tests and display results."""
    # Change to the directory containing the test files
    test_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(test_dir)
    
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTotalSalary)
    runner = unittest.TextTestRunner(verbosity=2)
    
    print("Running comprehensive tests for total_salary function...")
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