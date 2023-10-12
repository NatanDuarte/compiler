import argparse

from args import process_file_mode, process_interactive_mode


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Programa de exemplo com CLI.")
    parser.add_argument("-i", "--interactive", action="store_true", help="Modo interativo")
    parser.add_argument("-f", "--file", help="Arquivo de entrada (modo arquivo)")
    args = parser.parse_args()

    if args.interactive:
        process_interactive_mode()
    elif args.file:
        process_file_mode(args.file)
    else:
        print("""Você deve especificar um dos modos:
    -i (modo interativo)
    -f [ARQUIVO] (modo arquivo)""")
