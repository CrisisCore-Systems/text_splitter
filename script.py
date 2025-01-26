import os
from typing import List, Optional, Tuple
from dataclasses import dataclass
import re
from pathlib import Path

@dataclass
class SplitConfig:
    """Configuration for file splitting parameters"""
    max_section_size: int = 4096  # bytes
    min_section_size: int = 512   # bytes
    heading_patterns: List[str] = None
    preserve_headers: bool = True
    output_dir: str = "split_output"
    
    def __post_init__(self):
        if self.heading_patterns is None:
            self.heading_patterns = [
                r'^#{1,6}\s+.+$',              # Markdown headers
                r'^[A-Z][^.!?]*[:]\s*$',       # Title-like lines
                r'^\d+\.\s+[A-Z][^.!?]*$',     # Numbered sections
                r'^[A-Z][A-Z\s]+$'             # ALL CAPS headers
            ]

class TextSplitter:
    """Intelligent text file splitter with section awareness"""
    
    def __init__(self, config: Optional[SplitConfig] = None):
        self.config = config or SplitConfig()
        self._compiled_patterns = [re.compile(pattern, re.MULTILINE) 
                                 for pattern in self.config.heading_patterns]
    
    def split_file(self, input_path: str) -> List[str]:
        """Split a text file into sections based on configuration"""
        input_path = Path(input_path)
        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")
            
        # Create output directory if it doesn't exist
        output_dir = Path(self.config.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Read entire file content
        content = input_path.read_text(encoding='utf-8')
        
        # Find all section boundaries
        sections = self._find_sections(content)
        
        # Split content into files
        output_files = []
        for idx, (start, end) in enumerate(sections, 1):
            section_content = content[start:end]
            
            # Generate output filename
            output_filename = f"{input_path.stem}_section_{idx:03d}{input_path.suffix}"
            output_path = output_dir / output_filename
            
            # Write section to file
            output_path.write_text(section_content, encoding='utf-8')
            output_files.append(str(output_path))
            
        return output_files
    
    def _find_sections(self, content: str) -> List[Tuple[int, int]]:
        """Find optimal section boundaries based on headers and size constraints"""
        # Find all potential section starts
        section_starts = set()
        section_starts.add(0)  # Always include start of file
        
        # Find all matches for heading patterns
        for pattern in self._compiled_patterns:
            for match in pattern.finditer(content):
                section_starts.add(match.start())
        
        # Sort section starts
        section_starts = sorted(list(section_starts))
        
        # Build optimal sections
        sections = []
        current_start = 0
        current_size = 0
        
        for next_start in section_starts[1:] + [len(content)]:
            section_size = next_start - current_start
            
            if current_size + section_size > self.config.max_section_size:
                # If adding this section would exceed max size, finalize current section
                if current_size >= self.config.min_section_size:
                    sections.append((current_start, current_start + current_size))
                    current_start = next_start
                    current_size = 0
                else:
                    # If current section is too small, extend it
                    current_size += section_size
            else:
                current_size += section_size
        
        # Add final section if needed
        if current_size > 0:
            sections.append((current_start, current_start + current_size))
        
        return sections

class BatchSplitter:
    """Handles batch processing of multiple files"""
    
    def __init__(self, splitter: TextSplitter):
        self.splitter = splitter
    
    def process_directory(self, input_dir: str, file_pattern: str = "*.txt") -> dict:
        """Process all matching files in a directory"""
        input_dir = Path(input_dir)
        results = {}
        
        for file_path in input_dir.glob(file_pattern):
            try:
                output_files = self.splitter.split_file(str(file_path))
                results[str(file_path)] = {
                    'status': 'success',
                    'output_files': output_files
                }
            except Exception as e:
                results[str(file_path)] = {
                    'status': 'error',
                    'error': str(e)
                }
        
        return results

def main():
    # Example usage
    config = SplitConfig(
        max_section_size=8192,
        min_section_size=1024,
        output_dir="split_docs"
    )
    
    splitter = TextSplitter(config)
    batch_processor = BatchSplitter(splitter)
    
    # Process single file
    try:
        output_files = splitter.split_file("example.txt")
        print(f"Split into {len(output_files)} files:")
        for file in output_files:
            print(f"  - {file}")
    except FileNotFoundError:
        print("Please provide a valid input file")
    
    # Process directory
    results = batch_processor.process_directory("docs", "*.md")
    for input_file, result in results.items():
        print(f"\nProcessed {input_file}:")
        if result['status'] == 'success':
            print(f"  Created {len(result['output_files'])} sections")
        else:
            print(f"  Error: {result['error']}")

if __name__ == "__main__":
    main()
