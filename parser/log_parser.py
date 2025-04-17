import re
from typing import Dict

LOG_PATTERN = re.compile(
    r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3} (?P<level>[A-Z]+) django\.request: .*? (?P<url>/\S+)"
)

def parse_log_file(file_path: str) -> Dict[str, Dict[str, int]]:
    result: Dict[str, Dict[str, int]] = {}
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            match = LOG_PATTERN.search(line)
            if match:
                level = match.group("level")
                url = match.group("url")
                if url not in result:
                    result[url] = {}
                result[url][level] = result[url].get(level, 0) + 1
    return result
