import sys
from typing import List, Optional


def main() -> Optional[List[str]]:
    if len(sys.argv) != 2:
        sys.stderr.write("ERROR: Usage: ft_ancient_text.py <file>\n")
        return None

    filename = sys.argv[1]
    sys.stdout.write("=== Cyber Archives Recovery ===\n")
    sys.stdout.write(f"Accessing file '{filename}'\n")

    try:
        f = open(filename, "r")
        content = f.read()
        f.close()
        sys.stdout.write("---\n")
        sys.stdout.write(content + "\n")
        sys.stdout.write("---\n")
        return content.splitlines()
    except (FileNotFoundError, PermissionError) as e:
        sys.stderr.write(f"ERROR: Error opening file '{filename}': {e}\n")
        return None


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
                n = open(new_file, "w")
                n.write("\n".join(transformed) + "\n")
                n.close()
                sys.stdout.write(f"Data saved in file '{new_file}'\n")
            except (FileNotFoundError, PermissionError) as e:
                sys.stderr.write(f"ERROR: Error opening file '{new_file}': {e}\n")