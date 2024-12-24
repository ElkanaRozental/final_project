def is_not_none(*args) -> bool:
    return all(x is not None for x in args)