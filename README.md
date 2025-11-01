# Python Programming Assignment 4

## 🎯 作业目标
通过 5 道编程题目，巩固 Python 中的：

- 字符串基本操作（如格式化、查找、替换等）；

- 正则表达式；

### 任务 1：字符串格式化

编写函数 `format_score_card(name, course, score)`

- 使用字符串格式化生成成绩单；
- 成绩保留两位小数；
  - 若成绩 < 60，输出“未通过”； 
  - 若成绩 ≥ 90，输出“优秀”； 
  - 若成绩 <90 且 >=80，输出“良好”；
  - 若成绩 <80 且 >= 60 输出“合格”；
  - 否则输出“非法成绩”。

### 任务 2：文本分析

编写函数 `analyze_sentence(text, word)`
   - 同时使用字符串方法：`find()`、`rfind()`、`index()`、`rindex()`、`count()`、`split()`、`rsplit()`、`partition()`、`rpartition()`；
   - 返回字典：
     - `first_index`: 单词第一次出现的位置（找不到为 -1）；
     - `last_index`: 单词最后一次出现的位置（找不到为 -1）；
     - `count`: 出现次数；
     - `left_part`: 使用 `partition(word)` 得到的 **word 左侧** 部分；
     - `right_part`: 使用 `rpartition(word)` 得到的 **word 右侧** 部分；
     - `split_words`: 使用 `split()`（按任意空白）得到的单词列表；
     - `rsplit_words`: 使用 `rsplit()`（按任意空白，从右侧最多分割 1 次）得到的列表。
   - 若 `word` 不在 `text` 中，`left_part` 与 `right_part` 设为原文本。

### 任务 3：字符串清洗与加密

编写函数 `clean_and_translate(text)`
- 依次完成：
    1) 使用 `strip()` 去掉两端空白；
    2) 使用 `rstrip('!?.')` 去掉右侧末尾的 `! ? .`；
    3) 使用 `lstrip('#*@')` 去掉左侧多余的 `# * @`；
    4) 使用 `replace(' ', '_')` 将空格替换为下划线；
    5) 使用 `str.maketrans()` 和 `translate()` 构建字符映射：把元音字母 `aeiouAEIOU` 全部替换为 `*`，把数字 `0-9` 全部替换为 `#`。
- 返回清洗和映射后的新字符串。

### 任务 4：文件名整理与格式对齐

编写函数 `format_filename(name)`
- 要求：
    1) 去除前后空白；
    2) 若不以 `"file_"` 开头则补上，若不以 `".txt"` 结尾则补上；
    3) 主体部分（去掉前缀与后缀）必须全为字母或字母数字（`isalnum()`），否则返回 `"Invalid File Name!"`；
    4) 使用 `center()`、`ljust()`、`rjust()` 输出一个信息框，包含标题、文件名与状态行；
        - 若主体全为字母（`isalpha()`），状态显示 `Valid`；否则显示 `Invalid`。
- 涉及方法：`startswith()`、`endswith()`、`isalnum()`、`isalpha()`、`center()`、`ljust()`、`rjust()`

### 任务 5：正则表达式

编写函数 `parse_log_line(line)`
- 使用正则表达式从日志行中提取：
    - `date`（`YYYY-MM-DD`）
    - `time`（`HH:MM:SS`）
    - `level`（如 `INFO`/`ERROR`/`WARN`/`DEBUG` 等全大写）
    - `user`（位于 `user=` 之后的用户名，仅字母数字下划线）
    - `ip`（IPv4 地址）
    - 日志中字段顺序可能不同，但函数应能正确提取；缺失的字段返回 `None`。

## 本地运行与测试

### 运行单题

```bash
python src/q1_format.py
```

### 运行全部测试

```bash
pip install -r requirements.txt
pytest -q
```

    GitHub Classroom 会自动运行这些测试，检测程序输出是否正确。

## 注意事项

- 请勿修改 `tests/` 文件夹里的内容。
- 代码要加注释，变量命名清晰。
- 所有题目必须使用函数封装； 
- 禁止抄袭（系统可检测相似度）； 
- 提交前确认测试全部通过。


    出题人：柳文章 安徽大学人工智能学院
    出题时间：2025.11.1
