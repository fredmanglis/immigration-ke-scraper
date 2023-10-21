"""Parse file and output content."""
import sys
from pathlib import Path

import click
from pytesseract import image_to_string

from parsing.parse import parse_lines

if __name__ == "__main__":
    @click.command()
    @click.argument("filepath", type=click.STRING)
    def main(filepath):
        """Entry point."""
        if not Path(filepath).exists():
            print(f"{filepath}: No such file.")
            sys.exit(1)

        print(filepath)
        print("Tracking Number,Date")
        for line in parse_lines(image_to_string(filepath).split("\n")):
            print('%s,%s' % line)
        

    main()
