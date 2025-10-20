from src.text_splitter import CrisisCoreSplitter
import argparse
import sys
import os

def parse_args():
    parser = argparse.ArgumentParser(
        description='CrisisCore-Systems Text Splitting Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('file', help='Input file path')
    parser.add_argument('-s', '--size', type=int, default=1024*1024,
                       help='Maximum chunk size in bytes (default: 1MB)')
    return parser.parse_args()

def main():
    try:
        args = parse_args()
        if not os.path.exists(args.file):
            print('Error: Input file not found')
            return 1

        splitter = CrisisCoreSplitter(args.file, args.size)
        splitter.split_file()
        return 0
    except Exception as e:
        print(f'Error: {str(e)}')
        return 1

if __name__ == '__main__':
    sys.exit(main())
