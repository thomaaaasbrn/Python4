def secure_archive(nom: str, action: str = "r", content: str = "") -> tuple:
    try:
        with open(nom, action) as f:
            if action == "w":
                f.write(content)
                return (True, "Content successfully written to file")
            else:
                content = f.read()
                return (True, content)
    except OSError as e:
        return (False, str(e))


if __name__ == "__main__":
    print("Using 'secure_archive' to read from a nonexistent file:")
    s1 = secure_archive("/not/existing/file", "r")
    print(f"{s1}")
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    s2 = secure_archive("/etc/shadow", "r")
    print(f"{s2}")
    print()
    print("Using 'secure_archive' to read from a regular file:")
    s3 = secure_archive("test.txt", "r", "test.txt")
    print(f"{s3}")
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    s4 = secure_archive("new_file.txt", "w", s3[1])
    print(f"{s4}")
    print()
