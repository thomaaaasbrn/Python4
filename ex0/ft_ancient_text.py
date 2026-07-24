import sys


def ancient_test() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    try:
        print("=== Cyber Archives Recovery ===")
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
    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__name__":
    ancient_test()
