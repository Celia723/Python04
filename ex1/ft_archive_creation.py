import sys
from typing import List, Optional


def main() -> Optional[List[str]]:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>\n")
        return None

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===\n")
    print(f"Accessing file '{filename}'\n")

    try:
        with open(filename, "r") as f:
            content = f.read()
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{filename}': {e}\n")
        return None

    print(content + "\n")
    return content.splitlines()


if __name__ == "__main__":
    lines = main()
    if lines is not None:
        transformed = [line + "#" for line in lines]
        print("\n".join(transformed) + "\n")

        new_file = input("Enter new file name (or empty): ")

        if new_file == "":
            print("Not saving data.\n")
        else:
            print(f"Saving data to: '{new_file}'\n")
            try:
                with open(new_file, "w") as n:
                    n.write("\n".join(transformed) + "\n")
                print(f"Data saved in file '{new_file}'.\n")
            except (FileNotFoundError, PermissionError) as e:
                print(f"Error opening file '{new_file}': {e}\n")
