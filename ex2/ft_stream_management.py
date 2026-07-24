import sys


def management() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    try:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{sys.argv[1]}'")
        f = open(sys.argv[1])
        content = f.read()

        print("---")
        print()
        print(f"{content}")
        print()
        print("---")

        f.close()
        print(f"File '{sys.argv[1]}' closed.")
        print()
        print("Transform data:")
        print()

        res = []
        lignes = content.split("\n")

        for ligne in lignes:
            res.append(ligne + "#")
        nouveau = "\n".join(res)

        print("---")
        print()
        print(nouveau)
        print()
        print("---")

        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()

        new_name = sys.stdin.readline().strip()

        if len(new_name) == 0:
            sys.stdout.write("Not saving data.\n")
        else:
            try:
                print(f"Saving data to '{new_name}'")
                f_new = open(new_name, "w")
                f_new.write(nouveau)
                f_new.close()
                print(f"Data saved in file '{new_name}'")

            except OSError as e:
                sys.stderr.write(f"[STDERR] Error "
                                 f"opening file '{new_name}': {e}\n")
                print("Data not saved.")

    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}\n")


if __name__ == "__main__":
    management()
