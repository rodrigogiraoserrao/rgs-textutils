import pytest

from rgs_textutils import remove_punctuation

@pytest.mark.parametrize(
    ["text"],
    [
        ("HELLO",),
        ("hello",),
        ("         ",),
        ("Hello",),
    ]
)
def test_no_punctuation(text):
    assert remove_punctuation(text) == text

@pytest.mark.parametrize(
    ["text", "expected"],
    [
        ("hello!!!", "hello"),
        ("bananas...", "bananas"),
    ],
)
def test_removes_trailing_punctuation(text, expected):
    assert remove_punctuation(text) == expected
