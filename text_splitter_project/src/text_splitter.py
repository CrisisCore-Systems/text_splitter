class TextSplitter:
    def __init__(self, input_file, max_chunk_size=1024*1024):  # 1MB default chunk size
        self.input_file = input_file
        self.max_chunk_size = max_chunk_size
        
    def split_file(self):
        try:
            chunk_number = 0
            with open(self.input_file, 'r', encoding='utf-8') as f:
                current_chunk = []
                current_size = 0
                
                for line in f:
                    line_size = len(line.encode('utf-8'))
                    
                    if current_size + line_size > self.max_chunk_size:
                        # Write current chunk to file
                        self._write_chunk(current_chunk, chunk_number)
                        chunk_number += 1
                        current_chunk = []
                        current_size = 0
                    
                    current_chunk.append(line)
                    current_size += line_size
                
                # Write final chunk if any content remains
                if current_chunk:
                    self._write_chunk(current_chunk, chunk_number)
                    
        except UnicodeDecodeError:
            with open(self.input_file, 'r', encoding='latin-1') as f:
                # Repeat the same process for latin-1 encoding
                pass
    
    def _write_chunk(self, chunk, chunk_number):
        output_file = f"{self.input_file}.{chunk_number:03d}.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(chunk)
