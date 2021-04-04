import sys
from io import StringIO

import pytest

from src.restart import restart


sys.path.insert(1, "C:\\Users\\venge\\Projects\\rps\\src\\restart.py")


@pytest.mark.parametrize("prompt, expected", [
    (StringIO('y\n'), True),
    (StringIO('Y\n'), True),
    (StringIO('n\n'), False),
    (StringIO('\n'), False),
    (StringIO('foo\n'), False),
    (StringIO('0\n'), False),
    (StringIO('!\n'), False)
])
def test_restart_true(monkeypatch, prompt, expected):
    monkeypatch.setattr('sys.stdin', prompt)
    assert restart() == expected
