from src.q3_clean_and_translate import clean_and_translate


def test_clean_and_translate_basic():
    text = "   ##Hello World 123!!!   "
    assert clean_and_translate(text) == "H*ll*_W*rld_###"


def test_clean_and_translate_leading_symbols_and_digits():
    text = "@@Python 3.10!"
    # 去左侧 @@，去右侧 !，空格->下划线，然后元音与数字映射
    assert clean_and_translate(text) == "Pyth*n_#.##"
    # 说明：上面一行只是为了强调流程；实际断言以右侧字符串为准


def test_clean_and_translate_only_spaces_and_vowels():
    text = "   apple "
    assert clean_and_translate(text) == "*ppl*"


def test_clean_and_translate_mixed_punctuations():
    text = "  ***Email me at 000...  "
    # 左侧 *** 会被 lstrip 移除（因为包含 *），右侧没有 !?. 末尾序列，空格->下划线，数字映射
    result = clean_and_translate(text)
    assert result == "*m**l_m*_*t_###"
