import os
import sys
from datetime import datetime


def write_input(path: str) -> None:
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = input("Enter content line: ")
    number_of_line = 1
    if line == "stop":
        return
    else:
        with open(path, "a") as f:
            if os.path.exists(path):
                f.write("\n")
            f.write(now_str + "\n")
            while not line == "stop":
                f.write(f"{number_of_line} {line}\n")
                line = input("Enter content line: ")
                number_of_line += 1


def create_file() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        f_position = sys.argv.index("-f")
        d_position = sys.argv.index("-d")
        file_txt = sys.argv[f_position + 1]
        if d_position < f_position:
            directory = sys.argv[(d_position + 1): f_position]
        else:
            directory = sys.argv[d_position + 1:]
        directory_path = os.path.join(*directory)
        os.makedirs(directory_path, exist_ok=True)
        path = os.path.join(directory_path, file_txt)
        write_input(path)
    elif "-d" in sys.argv and "-f" not in sys.argv:
        directory = sys.argv[sys.argv.index("-d") + 1:]
        directory_path = os.path.join(*directory)
        os.makedirs(directory_path, exist_ok=True)
    elif "-f" in sys.argv and "-d" not in sys.argv:
        file_txt = sys.argv[sys.argv.index("-f") + 1]
        write_input(file_txt)


if __name__ == "__main__":
    create_file()
