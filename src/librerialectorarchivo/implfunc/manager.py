from src.librerialectorarchivo.implfunc.filter import filter_upper_to_lower, filter_space_to_dash
from src.librerialectorarchivo.implfunc.reader import create_reader, ReaderFunction


_FILTERS = {
    'u': filter_upper_to_lower,
    's': filter_space_to_dash,
}


def build_reader(file_: str, filters: str = '') -> ReaderFunction:
    """
    Create a reader function with the given filters
    :param file_: The file to read
    :param filters: The filters to apply
    :return: A reader function
    """
    reader: ReaderFunction = create_reader(file_)
    if filters:
        for filter_ in filters:
            reader = _FILTERS[filter_](reader)
    return reader


def register_filter(function: ReaderFunction, code: str):
    """
    Register a new filter
    :param function: The filter function
    :param code: The filter name
    """
    _FILTERS[code] = function