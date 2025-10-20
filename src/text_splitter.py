"""Text file splitting utility with line-aware chunking."""
import os
import logging

logger = logging.getLogger(__name__)


class CrisisCoreSplitter:
    """
    Intelligent text file splitter that splits files into chunks while preserving line boundaries.

    This class splits large text files into smaller chunks based on a maximum chunk size,
    ensuring that lines are not split across chunks. If a line exceeds the maximum chunk
    size, it is skipped with a warning.

    Attributes:
        input_file (str): Path to the input file to be split.
        max_chunk_size (int): Maximum size of each chunk in bytes (default: 1MB).
    """

    def __init__(self, input_file, max_chunk_size=1024 * 1024):
        """
        Initialize the CrisisCoreSplitter with input file and chunk size.

        Args:
            input_file (str): Path to the text file to split.
            max_chunk_size (int, optional): Maximum size of each chunk in bytes.
                                           Defaults to 1MB (1024*1024 bytes).

        Raises:
            ValueError: If max_chunk_size is not positive.
            FileNotFoundError: If the input file does not exist.
        """
        if max_chunk_size <= 0:
            raise ValueError('Chunk size must be positive')
        if not os.path.exists(input_file):
            raise FileNotFoundError(f'Input file not found: {input_file}')
        self.input_file = input_file
        self.max_chunk_size = max_chunk_size
        self._print_banner()

    def _print_banner(self):
        """Display the application banner with version information."""
        banner = '''
+===============================================================+
|                 CrisisCore-Systems v0.1.0-alpha                |
|                    Text Splitting Tool                         |
|              Developed by CrisisCore Systems                   |
+===============================================================+
'''
        logger.info(banner)

    def split_file(self):
        """
        Split the input file into multiple chunks based on the configured chunk size.

        This method reads the input file line by line and groups lines into chunks
        that do not exceed the maximum chunk size. Each chunk is written to a
        separate output file with a numbered suffix (e.g., .cc000.txt, .cc001.txt).

        Returns:
            int: The number of chunks created.

        Raises:
            Exception: If any error occurs during file reading or writing.
        """
        try:
            chunk_number = 0
            with open(self.input_file, 'r', encoding='utf-8') as f:
                current_chunk = []
                current_size = 0

                for line in f:
                    line_size = len(line.encode('utf-8'))

                    if current_size + line_size > self.max_chunk_size and current_chunk:
                        self._write_chunk(current_chunk, chunk_number)
                        chunk_number += 1
                        current_chunk = []
                        current_size = 0

                    if line_size <= self.max_chunk_size:
                        current_chunk.append(line)
                        current_size += line_size
                    else:
                        logger.warning('Skipping line exceeding chunk size')

                if current_chunk:
                    self._write_chunk(current_chunk, chunk_number)

            logger.info(f'Successfully created {chunk_number + 1} chunks')
            return chunk_number + 1

        except Exception as e:
            raise Exception(f'CrisisCore-Systems Error: {str(e)}')

    def _write_chunk(self, chunk, chunk_number):
        """
        Write a chunk of lines to an output file.

        Args:
            chunk (list): List of lines to write to the chunk file.
            chunk_number (int): Sequential number for the chunk file.
        """
        output_file = f"{self.input_file}.cc{chunk_number:03d}.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(chunk)
        logger.info(f'Created chunk: {output_file}')
