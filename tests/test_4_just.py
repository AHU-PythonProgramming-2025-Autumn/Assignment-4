from src.q4_just import format_filename


def test_format_filename_basic_add_prefix_suffix():
    out = format_filename(" report1 ")
    expected = (
        "+------------------------------+\n"
        "|       File Information       |\n"
        "| File Name:  file_report1.txt |\n"
        "| Status:              Invalid |\n"
        "+------------------------------+"
    )
    assert out == expected


def test_format_filename_keep_when_ready_and_alpha_core():
    out = format_filename("file_Data.txt")
    expected = (
        "+------------------------------+\n"
        "|       File Information       |\n"
        "| File Name:     file_Data.txt |\n"
        "| Status:                Valid |\n"
        "+------------------------------+"
    )
    assert out == expected


def test_format_filename_illegal_chars():
    assert format_filename("file_$$data!.txt") == "Invalid File Name!"
