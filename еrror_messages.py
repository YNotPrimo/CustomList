class RemoveError(Exception):
    """No, you can't remove that. Index is out of the list."""
    pass


class GetError(Exception):
    """No, you can't get that. Index is out of the list."""
    pass


class InsertError(Exception):
    """No, you can't do that. Index is out of the list."""
    pass
