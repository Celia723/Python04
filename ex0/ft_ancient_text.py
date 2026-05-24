import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    file = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file}'")

    try:
        with open(file, "r") as f:
            print("---")
            print()
            print(f.read())
            print()
            print("---")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{file}': {e}")


if __name__ == "__main__":
    main()
