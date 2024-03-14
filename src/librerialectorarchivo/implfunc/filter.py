import functools

from src.librerialectorarchivo.implfunc.reader import ReaderFunction


def filter_upper_to_lower(reader: ReaderFunction) -> ReaderFunction:
    @functools.wraps(reader)
    def read() -> str:
        for c in reader():
            if c.isupper():
                c = c.lower()
            yield c
    return read


def filter_space_to_dash(reader: ReaderFunction) -> ReaderFunction:
    @functools.wraps(reader)
    def read() -> str:
        for c in reader():
            if c == ' ':
                c = '_'
            yield c
    return read