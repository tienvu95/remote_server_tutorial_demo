from pathlib import Path


def add_numbers(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    total = add_numbers(2, 3)
    print(f"Hello from the remote server. 2 + 3 = {total}")

    try:
        import jupyterlab
        print("jupyterlab was installed successfully!")
    except ImportError:
        print("jupyterlab was not installed successfully. Did you create and activate your virtual environment?")
