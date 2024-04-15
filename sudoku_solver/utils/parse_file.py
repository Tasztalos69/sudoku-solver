from pathlib import Path

accepted = [str(x) for x in range(1, 10)]


def parse_file(file_name: str = "input.txt") -> [[int | None]]:
    """Parses the input from a file."""

    with Path.open(Path(file_name)) as file:
        rows = list(filter(lambda r: r != "\n", file.readlines()))
        return [[int(c) if c.strip() in accepted else None for c in row.split(" ")] for row in rows]
