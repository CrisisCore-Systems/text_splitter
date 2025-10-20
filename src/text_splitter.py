import os

class CrisisCoreSplitter:
    def __init__(self, input_file, max_chunk_size=1024*1024):
        if max_chunk_size <= 0:
            raise ValueError('Chunk size must be positive')
        if not os.path.exists(input_file):
            raise FileNotFoundError(f'Input file not found: {input_file}')
        self.input_file = input_file
        self.max_chunk_size = max_chunk_size
        self._print_banner()
        
    def _print_banner(self):
        banner = '''
+===============================================================+
|                   CrisisCore-Systems v1.0                      |
|                    Text Splitting Tool                         |
|              Developed by CrisisCore Systems                   |
+===============================================================+
'''
        print(banner)
        
    def split_file(self):
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
                        print(f'Warning: Skipping line exceeding chunk size')
                
                if current_chunk:
                    self._write_chunk(current_chunk, chunk_number)
            
            print(f'Successfully created {chunk_number + 1} chunks')
            
        except Exception as e:
            raise Exception(f'CrisisCore-Systems Error: {str(e)}')
    
    def _write_chunk(self, chunk, chunk_number):
        output_file = f"{self.input_file}.cc{chunk_number:03d}.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(chunk)
        print(f'Created chunk: {output_file}')
