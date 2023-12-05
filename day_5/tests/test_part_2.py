import pytest

from day_5.part_2 import run
from utils.io import read


@pytest.mark.parametrize(
    "test_input, expected",
    [(read("data/example_1.txt"), 46)],
)
def test_run(test_input, expected):
    assert run(test_input) == expected
