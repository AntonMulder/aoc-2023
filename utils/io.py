from typing import Iterator


def read(path: str) -> str:
    with open(path) as f:
        data = f.read()
    return data


def readlines(path: str) -> Iterator[str]:
    with open(path) as f:
        data = f.readlines()
    return (x.rstrip() for x in data)
