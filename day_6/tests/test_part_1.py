import pytest

from day_6.part_1 import run
from utils.io import readlines


@pytest.mark.parametrize(
    "test_input, expected",
    [(readlines("data/example_1.txt"), 288)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
