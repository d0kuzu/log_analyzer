from typing import Dict
from report.base import BaseReport

class HandlersReport(BaseReport):
    LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

    def generate(self, data: Dict[str, Dict[str, int]]) -> None:
        all_levels = {level: 0 for level in self.LEVELS}
        total_requests = 0

        handlers = sorted(data.keys())
        print(f"Total requests: {sum(sum(v.values()) for v in data.values())}\n")
        header = ["HANDLER"] + self.LEVELS
        print("{:<24s}".format(header[0]), end="")
        for level in self.LEVELS:
            print(f"{level:<8s}", end="\t")
        print()

        for handler in handlers:
            print(f"{handler:<24s}", end="")
            for level in self.LEVELS:
                count = data[handler].get(level, 0)
                print(f"{count:<8d}", end="\t")
                all_levels[level] += count
                total_requests += count
            print()

        print(f"{'':<24s}", end="")
        for level in self.LEVELS:
            print(f"{all_levels[level]:<8d}", end="\t")
        print()
