# %%
#######################################
def get_hash(obj: "(object | list | tuple)"):
    """Returns a hash of the given object or returns the hash of each object in a given collection.

    Example:
        >>> thelist = ["slowdown's",
        ...  'acrylic',
        ...  'tainting',
        ...  'Pruitt',
        ...  'pharmacopeias',
        ...  'bordello',
        ...  'theorem',
        ...  'balky',
        ...  'Sappho',
        ...  'copiers']\n

        >>> get_hash( thelist )\n
        [2233647814837143449, 5906085328952193911, -2262468258438027459, -6801245114894821716, 1638203867347057992, -6751225304581886214, 8827831766081086454, 707996717450372103, 5002529142143650073, -1818107816829694179]

    Args:
        obj (object | list | tuple): Reference a single onject or a collection of objects

    Returns:
        int: Returns an integer or a collection of integers.
    """
    if isinstance(obj, list):
        results = [hash(e) for e in obj]
    elif isinstance(obj, tuple):
        results = tuple([hash(e) for e in obj])
    else:
        try:
            results = hash(obj)
        except Exception:
            print('An exception has occurred...')
            return
    return results

    