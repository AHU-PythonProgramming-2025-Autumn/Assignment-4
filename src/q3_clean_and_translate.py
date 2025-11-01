"""
出题者：柳文章，安徽大学人工智能学院
出题日期：2025.11.1

任务：编写函数 `clean_and_translate(text)`
- 依次完成：
    1) 使用 `strip()` 去掉两端空白；
    2) 使用 `rstrip('!?.')` 去掉右侧末尾的 `! ? .`；
    3) 使用 `lstrip('#*@')` 去掉左侧多余的 `# * @`；
    4) 使用 `replace(' ', '_')` 将空格替换为下划线；
    5) 使用 `str.maketrans()` 和 `translate()` 构建字符映射：把元音字母 `aeiouAEIOU` 全部替换为 `*`，把数字 `0-9` 全部替换为 `#`。
- 返回清洗和映射后的新字符串。
"""


def clean_and_translate(text: str) -> str:
    """
    依次使用 strip、rstrip、lstrip、replace、maketrans、translate
    完成文本清洗与字符映射：
      - 去两端空白
      - 去右侧 !?. 末尾标点
      - 去左侧 #*@ 前缀符号
      - 空格替换为下划线
      - 元音 -> '*'，数字 -> '#'
    """
    # TODO:


if __name__ == '__main__':
    text = "   ##Hello World 123!!!   "
    print(clean_and_translate(text))
