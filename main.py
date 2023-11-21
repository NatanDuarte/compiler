import argparse

from args import process_file_mode, process_interactive_mode


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Zelda Compiler CLI.")
    parser.add_argument("-i", "--interactive", action="store_true", help="interactive mode")
    parser.add_argument("-f", "--file", help="file mode")
    args = parser.parse_args()

    if args.interactive:
        process_interactive_mode()
    elif args.file:
        process_file_mode(args.file)
    else:
        print("""Execution modes:
    -i (interactive mode)
    -f [PATH_TO_FILE] (file mode)""")
