import os
import sys
from datetime import datetime


def write_input(path: str) -> None:
    line = input("Enter content line: ")
    if line == "stop":
        return
    number_of_line = 1
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S    ")
    with open(path, "a") as f:
        if os.path.getsize(path) > 0:
            f.write("\n")
        f.write(now_str + "\n")
        while not line == "stop":
            f.write(f"{number_of_line} {line}\n")
            line = input("Enter content line: ")
            number_of_line += 1


def create_file() -> None:
    args = sys.argv[1:]
    if not args:
        raise ValueError("No arguments provided")
    if "-d" in args and "-f" in args:
        directory = []
        for index, arg in enumerate(args):
            if arg == "-d":
                dir_index = index + 1
                while dir_index < len(args) and args[dir_index] != "-f":
                    directory.append(args[dir_index])
                    dir_index += 1
        f_position = args.index("-f")
        if f_position + 1 >= len(args):
            print("No file specified")
            return
        file_txt = args[f_position + 1]
        directory_path = os.path.join(*directory)
        os.makedirs(directory_path, exist_ok=True)
        path = os.path.join(*directory_path, file_txt)
        write_input(path)
        return
    elif "-d" in args and "-f" not in args:
        directory = args[args.index("-d") + 1:]
        directory_path = os.path.join(*directory)
        os.makedirs(directory_path, exist_ok=True)
        return
    elif "-f" in args and "-d" not in args:
        file_txt = args[args.index("-f") + 1]
        write_input(file_txt)
        return


if __name__ == "__main__":
    create_file()
