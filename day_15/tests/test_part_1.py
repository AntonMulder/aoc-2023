import pytest

from day_15.part_1 import run
from utils.io import read


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("HASH", 52),
        (read("data/example_1.txt"), 1320),
    ],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
