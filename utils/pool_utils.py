from config import valueof


def get_pool_config(num_profiles):
    """Generates the process pool configuration information based off the number
    of records requested.

    Args:
        num_profiles(int): The number of profiles from the api request.

    Returns:
        p_config(tuple): A tuple containing the number of pools to be created
        and the depth of each of the pools.
    """
    if num_profiles < 10:
        return (3, 3)
    elif 10 <= num_profiles <= 20:
        return (4, 5)
    elif 20 < num_profiles <= 50:
        return (4, 5)
    elif 50 < num_profiles <= 100:
        return (5, 10)
    elif 100 < num_profiles <= 500:
        return (6, 12)


def chunkate(num_profiles, depth):
    _x = num_profiles
    res = []
    while _x > depth:
        res.append(depth)
        _x -= depth
    res.append(_x)
    return res
