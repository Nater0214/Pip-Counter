# main.py
# Pip counter
# Count pips on dice or dominoes


# Imports
import argparse


# Definitions
def main(file_path: str) -> int:
    """Main"""
    
    print(file_path)


# Run
if __name__ == "__main__":
    
    arg_parser = argparse.ArgumentParser(prog="Pip Counter",add_help=True)
    arg_parser.add_argument("-i", type=str, help="Input file", required=True)
    args = arg_parser.parse_args()
    main(args.i)