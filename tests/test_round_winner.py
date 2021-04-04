import sys

import pytest

from src.round_winner import round_winner


sys.path.insert(1, "C:\\Users\\venge\\Projects\\rps\\src\\round_winner.py")
action = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}


@pytest.mark.parametrize("player, computer, result", [
    (action["rock"], action["rock"], None),  # rock tie
    (action["paper"], action["paper"], None),  # paper tie
    (action["scissors"], action["scissors"], None),  # scissors tie
    (action["rock"], action["paper"], False),  # paper covers rock
    (action["rock"], action["scissors"], True),  # rock smashes scissors
    (action["paper"], action["rock"], True),  # paper covers rock
    (action["paper"], action["scissors"], False),  # scissors cut paper
    (action["scissors"], action["rock"], False),  # rock smashes scissors
    (action["scissors"], action["paper"], True)  # scissors cut paper
])
def test_round_winner(player, computer, result):
    assert round_winner(player, computer) == result
