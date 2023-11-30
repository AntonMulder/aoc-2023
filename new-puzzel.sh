#/bin/bash

day=$1

token=''

new_dir="day_$day"

### Check if a directory does not exist ###
if [ ! -d $new_dir ]
then
    # Create root dir
    mkdir -p $new_dir
    touch ""$new_dir/__init__.py""

    # Create test folder and files
    mkdir -p "$new_dir/tests/data"
    touch "$new_dir/tests/__init__.py"
    touch "$new_dir/tests/test_part_1.py"
    touch "$new_dir/tests/data/example_1.txt"

    {
      echo "import pytest"
      echo ""
      echo "from day_$day.part_1 import run"
      echo "from utils.io import read"
      echo ""
      echo ""
      echo "@pytest.mark.parametrize("
      echo "    \"test_input, expected\","
      echo "    [(read(\"data/example_1.txt\"), None)],"
      echo ")"
      echo "def test_run(test_input, expected):"
      echo "    assert run(test_input) == expected"
    } >> "$new_dir/tests/test_part_1.py"

    touch "$new_dir/tests/test_part_2.py"

    {
      echo "import pytest"
      echo ""
      echo "from day_$day.part_2 import run"
      echo "from utils.io import read"
      echo ""
      echo ""
      echo "@pytest.mark.parametrize("
      echo "    \"test_input, expected\","
      echo "    [(read(\"data/example_1.txt\"), None)],"
      echo ")"
      echo "def test_run(test_input, expected):"
      echo "    assert run(test_input) == expected"
    } >> "$new_dir/tests/test_part_2.py"

    # Create solution files
    touch "$new_dir/part_1.py"
    {
      echo "from utils.io import read"
      echo ""
      echo ""
      echo "def run(puzzle_input):"
      echo "    return -1"
      echo ""
      echo ""
      echo "if __name__ == \"__main__\":"
      echo "    print(run(read(\"data/puzzle_input.txt\")))"
    } >> "$new_dir/part_1.py"

    touch "$new_dir/part_2.py"
    cat "$new_dir/part_1.py" >> "$new_dir/part_2.py"

    status_code=$(curl -s --head -w %{http_code} https://adventofcode.com/2022/day/$day/input -o /dev/null)
    if [ $status_code = "400" ]
    then
      # Create data dir
      mkdir "$new_dir/data"
      # Get puzzle input
      curl -s "https://adventofcode.com/2022/day/$day/input" -H "Cookie: session=$token" -o "$new_dir/data/puzzle_input.txt"
    fi
else
    echo "Directory $new_dir already exists"
fi
