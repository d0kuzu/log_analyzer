from report.handlers import HandlersReport
from io import StringIO
import sys

def test_handlers_report_output(monkeypatch):
    data = {
        "/api/v1/test/": {"INFO": 2, "ERROR": 1},
        "/admin/": {"DEBUG": 1, "CRITICAL": 1}
    }
    report = HandlersReport()

    captured_output = StringIO()
    monkeypatch.setattr(sys, "stdout", captured_output)
    report.generate(data)
    output = captured_output.getvalue()

    assert "Total requests: 5" in output

    lines = output.strip().split("\n")
    table_lines = [line for line in lines if line.startswith("/")]

    rows = {}
    for line in table_lines:
        parts = line.split()
        handler = parts[0]
        counts = list(map(int, parts[1:6]))
        rows[handler] = {
            "DEBUG": counts[0],
            "INFO": counts[1],
            "WARNING": counts[2],
            "ERROR": counts[3],
            "CRITICAL": counts[4],
        }

    assert rows["/api/v1/test/"]["INFO"] == 2
    assert rows["/api/v1/test/"]["ERROR"] == 1
    assert rows["/admin/"]["DEBUG"] == 1
    assert rows["/admin/"]["CRITICAL"] == 1

