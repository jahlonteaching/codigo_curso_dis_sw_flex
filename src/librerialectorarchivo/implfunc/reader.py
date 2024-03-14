from typing import Callable

type ReaderFunction = Callable[[], str]


def create_reader(file_path: str) -> ReaderFunction:
    def read() -> str:
        with open(file_path, mode='r', encoding='utf8') as file:
            while c := file.read(1):
                yield c
    return read
