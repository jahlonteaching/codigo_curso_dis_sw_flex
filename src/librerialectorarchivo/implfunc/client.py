"""
This module represent the client application
"""
from src.librerialectorarchivo.implfunc.reader import ReaderFunction
from src.librerialectorarchivo.implfunc.manager import build_reader, register_filter


# Client own filter
def filter_question_to_exclamation(reader_func: ReaderFunction) -> ReaderFunction:
    """
    Filter that change exclamation marks to question marks
    :param reader_func: The reader function
    :return: A new reader function
    """
    def read() -> str:
        for ch in reader_func():
            if ch == '¿':
                ch = '¡'
            if ch == '?':
                ch = '!'
            yield ch
    return read


if __name__ == '__main__':
    # Register the filter
    register_filter(filter_question_to_exclamation, 'x')
    reader: ReaderFunction = build_reader("test.txt", "")
    for c in reader():
        print(c, end='')
