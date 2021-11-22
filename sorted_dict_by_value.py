# %%
#######################################
def sorted_dict_by_value(dictionary: dict):
    """Takes a given dictionary and returns a list of tuple key/value pairs that are sorted based on the value.

    Example:
        >>> thedict = {0: 'aggrandizing',
        ...  1: 'arbitrate',
        ...  2: 'robustness',
        ...  3: "agape's",
        ...  4: "Tarazed's",
        ...  5: 'centenarians',
        ...  6: 'vendors',
        ...  7: 'Elma',
        ...  8: 'nasalizes',
        ...  9: 'ransomed'}
        
        >>> sorted_dict_by_value( thedict )\n
        [(7, 'Elma'), (4, "Tarazed's"), (3, "agape's"), (0, 'aggrandizing'), (1, 'arbitrate'), (5, 'centenarians'), (8, 'nasalizes'), (9, 'ransomed'), (2, 'robustness'), (6, 'vendors')]

    Args:
        dictionary (dict): Reference an existing dict object.

    Returns:
        list: Returns a list of key/value pair tuples.
    """
    if isinstance(dictionary, dict):
        results = sorted( [(k,v) for k,v in dictionary.items()], key=lambda x:x[1] )
    return results

