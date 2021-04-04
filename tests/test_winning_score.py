import sys
from io import StringIO

import pytest

from src.winning_score import winning_score


sys.path.insert(1, "C:\\Users\\venge\\Projects\\rps\\src\\winning_score.py")


@pytest.mark.parametrize("prompt, expected", [
    (StringIO('1\n'), 1),
    (StringIO('2\n'), 2),
    (StringIO('3\n'), 3),
    (StringIO('15\n'), 15),
    (StringIO('453\n'), 453),
    (StringIO('9375\n'), 9375)
])
def test_winning_score(monkeypatch, prompt, expected):
    monkeypatch.setattr('sys.stdin', prompt)
    assert winning_score() == expected
