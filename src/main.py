"""Command-line interface for the CrisisCore Text Splitter."""
from src.text_splitter import CrisisCoreSplitter
import argparse
import sys
import os
import logging


def setup_logging():
    """Configure logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(message)s',
        handlers=[logging.StreamHandler(sys.stdout)]
    )


def parse_args():
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description='CrisisCore-Systems Text Splitting Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('file', help='Input file path')
    parser.add_argument('-s', '--size', type=int, default=1024 * 1024,
                        help='Maximum chunk size in bytes (default: 1MB)')
    return parser.parse_args()


def main():
    """
    Main entry point for the command-line interface.

    Returns:
        int: Exit code (0 for success, 1 for error).
    """
    setup_logging()
    logger = logging.getLogger(__name__)

    try:
        args = parse_args()
        if not os.path.exists(args.file):
            logger.error('Error: Input file not found')
            return 1

        splitter = CrisisCoreSplitter(args.file, args.size)
        splitter.split_file()
        return 0
    except Exception as e:
        logger.error(f'Error: {str(e)}')
        return 1


if __name__ == '__main__':
    sys.exit(main())
