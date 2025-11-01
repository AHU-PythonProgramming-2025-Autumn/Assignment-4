"""
出题者：柳文章，安徽大学人工智能学院
出题日期：2025.11.1

任务：编写函数 `format_filename(name)`
- 要求：
    1) 去除前后空白；
    2) 若不以 `"file_"` 开头则补上，若不以 `".txt"` 结尾则补上；
    3) 主体部分（去掉前缀与后缀）必须全为字母或字母数字（`isalnum()`），否则返回 `"Invalid File Name!"`；
    4) 使用 `center()`、`ljust()`、`rjust()` 输出一个信息框，包含标题、文件名与状态行；
        - 若主体全为字母（`isalpha()`），状态显示 `Valid`；否则显示 `Invalid`。
- 涉及方法：`startswith()`、`endswith()`、`isalnum()`、`isalpha()`、`center()`、`ljust()`、`rjust()`
"""


def format_filename(name: str) -> str:
    """
    文件名验证与格式化输出：
    - 去空白 -> 补前缀 file_ / 后缀 .txt
    - 主体：必须 isalnum()，否则返回 "Invalid File Name!"
    - 盒子布局：一行标题(居中)、剩下行冒号左边左对齐冒号右边右对齐)
    使用到：startswith, endswith, isalnum, isalpha, center, ljust, rjust
    例如：
        "+------------------------------+\n"
        "|       File Information       |\n"
        "| File Name:     file_Data.txt |\n"
        "| Status:                Valid |\n"
        "+------------------------------+"
    """
    # TODO:


if __name__ == "__main__":
    out = format_filename("file_Data.txt")
    print(out)
