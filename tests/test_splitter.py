import unittest
import os
from src.text_splitter import CrisisCoreSplitter
from pathlib import Path

class TestCrisisCoreSplitter(unittest.TestCase):
    def setUp(self):
        # Create test directory and file
        self.test_dir = Path('test_data')
        self.test_dir.mkdir(exist_ok=True)
        self.test_file = self.test_dir / 'test.txt'
        with open(self.test_file, 'w', encoding='utf-8') as f:
            f.write('This is a test file\\nfor testing the splitter\\nwith multiple lines')
            
    def tearDown(self):
        # Clean up test files
        for file in self.test_dir.glob('*.txt'):
            file.unlink()
        if self.test_dir.exists():
            self.test_dir.rmdir()
        
    def test_initialization(self):
        splitter = CrisisCoreSplitter(str(self.test_file))
        self.assertIsInstance(splitter, CrisisCoreSplitter)
        
    def test_file_splitting(self):
        splitter = CrisisCoreSplitter(str(self.test_file), max_chunk_size=20)
        splitter.split_file()
        chunk_files = list(self.test_dir.glob('*.cc*.txt'))
        self.assertTrue(len(chunk_files) > 1)
        
    def test_chunk_size(self):
        splitter = CrisisCoreSplitter(str(self.test_file), max_chunk_size=50)
        splitter.split_file()
        for chunk_file in self.test_dir.glob('*.cc*.txt'):
            size = len(chunk_file.read_bytes())
            self.assertLessEqual(size, 50)
            
    def test_file_not_found(self):
        with self.assertRaises(Exception):
            splitter = CrisisCoreSplitter('nonexistent.txt')
            splitter.split_file()
            
    def test_invalid_chunk_size(self):
        with self.assertRaises(Exception):
            splitter = CrisisCoreSplitter(str(self.test_file), max_chunk_size=-1)
            splitter.split_file()

if __name__ == '__main__':
    unittest.main()
