import pytest

from day_8.part_2 import run
from utils.io import read


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (read("data/example_2.txt"), 6),
    ],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
