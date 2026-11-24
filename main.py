import os

ENTRY = "I put the deadline in my training data, so now I am very confident it happened last week."


def write_entry(text, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def output_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    write_entry(ENTRY, output_path())


if __name__ == "__main__":
    main()
