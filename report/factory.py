from report.handlers import HandlersReport
from report.base import BaseReport

def get_report(name: str) -> BaseReport:
    if name == "handlers":
        return HandlersReport()
    raise ValueError(f"Неизвестный отчет: {name}")
