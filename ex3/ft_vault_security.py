from typing import Tuple


def secure_archive(
    file_name: str,
    action: int = 1,
    content_to_write: str = ""
) -> Tuple[bool, str]:
    content = ""
    try:
        if action == 1:
            with open(file_name, "r") as f:
                content = f.read()
            print(f"Archivo '{file_name}' cerrado automaticamente?: {f.closed}")
            return True, content

        elif action == 2:
            with open(file_name, "w") as f:
                f.write(content_to_write)
            print(f"Archivo '{file_name}' cerrado automaticamente?: {f.closed}")
            return True, "Content successfully written to file"

        return False, "Invalid action"

    except FileNotFoundError as e:
        print(f"Using '{file_name}' to read from a nonexistent file:")
        return False, str(e)

    except PermissionError as e:
        print(f"Using '{file_name}' to read from an inaccessible file:")
        return False, str(e)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    print()

    tupla = secure_archive("hola.txt")
    print(tupla)
    print()

    tupla = secure_archive("sinpermisos.txt")
    print(tupla)
    print()

    print("Using 'secure_archive' to read from a regular file:")
    tupla = secure_archive("siexiste.txt")
    print(tupla)
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    tupla = secure_archive("escribir.txt", 2, "estoy escribiendo")
    print(tupla)