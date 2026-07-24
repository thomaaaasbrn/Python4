def secure_archive(nom, action) -> None:
    try:
        with open("nouveau.txt", "w") as f:
            content = f.read()
            return (True, {content})
    except OSError as e:
        print(f"[Errno 2] No such file or directory: '{f}'")