import sys
from typing import List, Optional


def main() -> Optional[List[str]]:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return None

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        f = open(filename, "r")
        content = f.read()
        f.close()
        print("---")
        print(content)
        print("---")
        return content.splitlines()
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{filename}': {e}")
        return None


if __name__ == "__main__":
    lines = main()
    if lines is not None:
        transformed = [line + "#" for line in lines]
        print("\n".join(transformed))

        new_file = input("Enter new file name (or empty): ")

        if new_file == "":
            print("Not saving data.")
        else:
            print(f"Saving data to: '{new_file}'")
            try:
                n = open(new_file, "w")
                n.write("\n".join(transformed) + "\n")
                n.close()
                print(f"Data saved in file '{new_file}'.")
            except (FileNotFoundError, PermissionError) as e:
                print(f"Error opening file '{new_file}': {e}")
