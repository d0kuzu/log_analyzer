import argparse
import os
import sys
from concurrent.futures import ProcessPoolExecutor
from report.factory import get_report
from parser.log_parser import parse_log_file

def validate_files(file_paths: list[str]) -> None:
    for path in file_paths:
        if not os.path.isfile(path):
            print(f"Файл не найден: {path}", file=sys.stderr)
            sys.exit(1)

def main() -> None:
    parser = argparse.ArgumentParser(description="Анализ логов Django")
    parser.add_argument("logs", nargs="+", help="Пути к логам")
    parser.add_argument("--report", required=True, help="Название отчета")
    args = parser.parse_args()

    validate_files(args.logs)

    with ProcessPoolExecutor() as executor:
        results = list(executor.map(parse_log_file, args.logs))

    merged = {}
    for partial in results:
        for handler, levels in partial.items():
            if handler not in merged:
                merged[handler] = {}
            for level, count in levels.items():
                merged[handler][level] = merged[handler].get(level, 0) + count

    report = get_report(args.report)
    report.generate(merged)

if __name__ == "__main__":
    main()
