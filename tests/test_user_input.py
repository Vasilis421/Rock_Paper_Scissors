import sys
from io import StringIO

import pytest

from src.user_input import get_user_input


sys.path.insert(1, "C:\\Users\\venge\\Projects\\rps\\src\\user_input.py")


@pytest.mark.parametrize("prompt, expected", [
    (StringIO('1\n'), 1),
    (StringIO('2\n'), 2),
    (StringIO('3\n'), 3),
    (StringIO('0\n'), False),
    (StringIO('-1\n'), False),
    (StringIO('4\n'), False),
    (StringIO('15\n'), False),
    (StringIO('849\n'), False)
])
def test_user_input_int(monkeypatch, prompt, expected):
    monkeypatch.setattr('sys.stdin', prompt)
    assert get_user_input() == expected


@pytest.mark.parametrize("prompt", [
StringIO('\n'),
StringIO('foo\n')
])
def test_user_input_str(monkeypatch, prompt):
    monkeypatch.setattr('sys.stdin', prompt)
    with pytest.raises(ValueError):
        get_user_input()
