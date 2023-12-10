import pytest

from day_10.part_2 import run
from utils.io import read


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (read("data/example_3.txt"), 8),
        (read("data/example_4.txt"), 4),
    ],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
