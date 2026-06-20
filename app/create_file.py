import os
import sys
from datetime import datetime


def write_input(path: str) -> None:
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = input("Enter content line: ")
    with open(path, "a") as f:
        f.write(now_str + "\n")
        while not line == "stop":
            f.write(line + "\n")
            line = input("Enter content line: ")


def create_file() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        d_position = sys.argv.index("-d")
        f_position = sys.argv.index("-f")
        if d_position < f_position:
            directory = sys.argv[(d_position + 1) : f_position]
        elif d_position > f_position:
            directory = sys.argv[(d_position + 1):]
        directory_path = os.path.join(*directory)
        os.makedirs(directory_path)
        file_txt = sys.argv[f_position + 1]
        path = os.path.join(directory_path, file_txt)
        write_input(path)
    elif "-d" in sys.argv and "-f" not in sys.argv:
        directory = sys.argv[(sys.argv.index("-d") + 1):]
        directory_path = os.path.join(*directory)
        os.makedirs(directory_path)
    elif "-f" in sys.argv and "-d" not in sys.argv:
        file_txt = sys.argv[sys.argv.index("-f") + 1]
        write_input(file_txt)


if __name__ == "__main__":
    create_file()
