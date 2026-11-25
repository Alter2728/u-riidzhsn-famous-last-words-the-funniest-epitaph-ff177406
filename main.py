import os

LINE = "'These mushrooms are safe.' They were. He wasn't."


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH") or "/output/entry.txt"
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(output_path, "r", encoding="utf-8", newline="") as f:
        content = f.read()
    assert 1 <= len(content) <= 150, f"char count out of range: {len(content)}"
    assert "\n" not in content and "\r" not in content, "output must be a single line"
    assert content.strip(), "output must not be only whitespace"


if __name__ == "__main__":
    main()
