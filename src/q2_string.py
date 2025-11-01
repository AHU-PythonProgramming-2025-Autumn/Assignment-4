"""
出题者：柳文章，安徽大学人工智能学院
出题日期：2025.11.1

任务：编写函数 `analyze_sentence(text, word)`
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
"""


def analyze_sentence(text: str, word: str) -> dict:
    """
    综合使用字符串方法：
    find(), rfind(), index(), rindex(), count(),
    split(), rsplit(), partition(), rpartition()

    返回结构：
    {
        "first_index": int,     # 找不到为 -1
        "last_index": int,      # 找不到为 -1
        "count": int,
        "left_part": str,       # partition(word)[0]
        "right_part": str,      # rpartition(word)[2]
        "split_words": list,    # split() 按任意空白
        "rsplit_words": list    # rsplit(None, 1) 从右最多分割一次
    }
    """
    # TODO:

if __name__ == "__main__":
    text = "Yes ,  I   like Python programming! "
    word = "Python"
    print(analyze_sentence(text, word))
