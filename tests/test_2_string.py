# tests/test_string_tasks.py
from src.q2_string import analyze_sentence


def test_analyze_sentence_basic_two_occurrences():
    text = "Python is great and Python is powerful"
    word = "Python"
    res = analyze_sentence(text, word)
    expected = {
        "first_index": 0,
        "last_index": 20,
        "count": 2,
        "left_part": "",
        "right_part": " is powerful",
        "split_words": ["Python", "is", "great", "and", "Python", "is", "powerful"],
        "rsplit_words": ["Python is great and Python is", "powerful"]
    }
    assert res == expected


def test_analyze_sentence_not_found():
    text = "I love coding"
    word = "Java"
    res = analyze_sentence(text, word)
    expected = {
        "first_index": -1,
        "last_index": -1,
        "count": 0,
        # 未找到时，left_part 与 right_part 均为原文
        "left_part": text,
        "right_part": text,
        "split_words": ["I", "love", "coding"],
        "rsplit_words": ["I love", "coding"]
    }
    assert res == expected


def test_analyze_sentence_single_occurrence_with_spaces():
    text = "  data  science   rock  "
    word = "science"
    res = analyze_sentence(text, word)
    expected = {
        "first_index": 8,
        "last_index": 8,
        "count": 1,
        "left_part": "  data  ",
        "right_part": "   rock  ",
        "split_words": ["data", "science", "rock"],
        "rsplit_words": ["  data  science", "rock"],
    }
    assert res == expected


def test_analyze_sentence_partition_edges():
    text = "xx-KEY-yy-KEY-zz"
    word = "KEY"
    res = analyze_sentence(text, word)
    expected = {
        "first_index": 3,
        "last_index": 10,
        "count": 2,
        "left_part": "xx-",
        "right_part": "-zz",
        "split_words": ["xx-KEY-yy-KEY-zz"],
        "rsplit_words": ["xx-KEY-yy-KEY-zz"],
    }
    assert res == expected
