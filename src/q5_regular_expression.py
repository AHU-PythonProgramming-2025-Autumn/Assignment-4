"""
出题者：柳文章，安徽大学人工智能学院
出题日期：2025.11.1

任务：编写函数 `parse_log_line(line)`
- 使用正则表达式从日志行中提取：
    - `date`（`YYYY-MM-DD`）
    - `time`（`HH:MM:SS`）
    - `level`（如 `INFO`/`ERROR`/`WARN`/`DEBUG` 等全大写）
    - `user`（位于 `user=` 之后的用户名，仅字母数字下划线）
    - `ip`（IPv4 地址）
    - 日志中字段顺序可能不同，但函数应能正确提取；缺失的字段返回 `None`。
"""

# src/regex_tasks.py
import re


def parse_log_line(line: str) -> dict:
    """
    使用正则表达式解析日志行，提取:
    - date: YYYY-MM-DD
    - time: HH:MM:SS
    - level: 大写字母日志级别
    - user: user= 后的用户名（\\w+）
    - ip: IPv4 地址
    字段缺失时对应返回 None。字段顺序可变。
    """
    # TODO:


if __name__ == "__main__":
    print(parse_log_line("[2025-11-01 14:32:10] [INFO] user=Alice ip=192.168.0.15 action=login"))
