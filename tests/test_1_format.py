from src.q1_format import format_score_card


def test_format_score_card_excellent():
    result = format_score_card("Alice", "Python编程", 95.678)
    expect = (
        "学生成绩单\n"
        "--------------------------\n"
        f"姓名   ：Alice\n"
        f"课程   ：Python编程\n"
        f"成绩   ：95.68分（优秀）\n"
        "--------------------------"
    )
    assert result == expect


def test_format_score_card_pass():
    result = format_score_card("Tom", "数据结构", 75)
    expect = (
        "学生成绩单\n"
        "--------------------------\n"
        f"姓名   ：Tom\n"
        f"课程   ：数据结构\n"
        f"成绩   ：75.00分（合格）\n"
        "--------------------------"
    )
    assert result == expect


def test_format_score_card_fail():
    result = format_score_card("Bob", "算法", 58)
    expect = (
        "学生成绩单\n"
        "--------------------------\n"
        f"姓名   ：Bob\n"
        f"课程   ：算法\n"
        f"成绩   ：58.00分（未通过）\n"
        "--------------------------"
    )
    assert result == expect


def test_format_score_card_good():
    result = format_score_card("Jack", "高等数学", 85)
    expect = (
        "学生成绩单\n"
        "--------------------------\n"
        f"姓名   ：Jack\n"
        f"课程   ：高等数学\n"
        f"成绩   ：85.00分（良好）\n"
        "--------------------------"
    )
    assert result == expect


def test_format_score_card_nan():
    result = format_score_card("Jim", "英语", -10)
    expect = (
        "学生成绩单\n"
        "--------------------------\n"
        f"姓名   ：Jim\n"
        f"课程   ：英语\n"
        f"成绩   ：-10.00分（非法成绩）\n"
        "--------------------------"
    )
    assert result == expect
