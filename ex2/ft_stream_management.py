import sys
from typing import List, Optional


def main() -> Optional[List[str]]:
    if len(sys.argv) != 2:
        sys.stdout.write("Usage: ft_ancient_text.py <file>\n")
        return None

    filename = sys.argv[1]
    sys.stdout.write("=== Cyber Archives Recovery ===\n")
    sys.stdout.write(f"Accessing file '{filename}'\n")

    try:
        with open(filename, "r") as f:
            content = f.read()
    except (FileNotFoundError, PermissionError) as e:
        sys.stderr.write(f"Error opening file '{filename}': {e}\n")
        return None

    sys.stdout.write(content + "\n")
    return content.splitlines()


if __name__ == "__main__":
    lines = main()
    if lines is not None:
        transformed = [line + "#" for line in lines]
        sys.stdout.write("\n".join(transformed) + "\n")

        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        new_file = sys.stdin.readline().strip()

        if new_file == "":
            sys.stdout.write("Not saving data.\n")
        else:
            sys.stdout.write(f"Saving data to: '{new_file}'\n")
            try:
                with open(new_file, "w") as n:
                    n.write("\n".join(transformed) + "\n")
                sys.stdout.write(f"Data saved in file '{new_file