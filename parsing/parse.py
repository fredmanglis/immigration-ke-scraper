"""Parse the contents"""
import re
from datetime import date, datetime

def __parse_date__(text: str) -> date:
    """Convert last part of line into a datetime object."""
    return datetime.strptime(text.split(",")[-1].strip(), "%dRD %B %Y").date()

def parse_lines(lines: list[str]) -> tuple[tuple[int, date]]:
    """
    Parse list of strings into a sequence of (`Tracking NO`, `Date`) tuples.
    """
    pattern = re.compile(r'(^[0-9]+)([ \)\|]+)([0-9]+) \| (.*)')
    return tuple(
        (int(mtch[2]), __parse_date__(mtch[3]))
        for mtch in (
                match.groups()
                for match in
                (pattern.search(line) for line in lines)
                if bool(match)))
