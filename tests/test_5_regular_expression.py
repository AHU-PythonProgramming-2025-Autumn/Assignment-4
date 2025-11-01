# tests/test_regex_tasks.py
from src.q5_regular_expression import parse_log_line


def test_parse_log_line_basic_info():
    line = "[2025-11-01 14:32:10] [INFO] user=Alice ip=192.168.0.15 action=login success"
    out = parse_log_line(line)
    assert out == {
        "date": "2025-11-01",
        "time": "14:32:10",
        "level": "INFO",
        "user": "Alice",
        "ip": "192.168.0.15",
    }


def test_parse_log_line_error_level_different_order():
    # 顺序变动：ip 在前，user 在后
    line = "[2025-11-01 09:00:00] [ERROR] ip=10.0.0.8 action=timeout user=Bob"
    out = parse_log_line(line)
    assert out == {
        "date": "2025-11-01",
        "time": "09:00:00",
        "level": "ERROR",
        "user": "Bob",
        "ip": "10.0.0.8",
    }


def test_parse_log_line_missing_ip():
    line = "[2025-11-01 20:10:59] [WARN] user=Zoe action=logout"
    out = parse_log_line(line)
    assert out == {
        "date": "2025-11-01",
        "time": "20:10:59",
        "level": "WARN",
        "user": "Zoe",
        "ip": None,
    }


def test_parse_log_line_totally_invalid():
    line = "this is not a valid log"
    out = parse_log_line(line)
    assert out == {
        "date": None,
        "time": None,
        "level": None,
        "user": None,
        "ip": None}
