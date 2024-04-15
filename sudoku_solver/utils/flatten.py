def flatten(xss: list[list[any]]) -> list[any]:
    """Flattens a list.

    :link: https://stackoverflow.com/a/952952/11398687
    """
    return [x for xs in xss for x in xs]
