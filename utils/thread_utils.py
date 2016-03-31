def chunkate(x):
    _x = x
    res = []
    while _x > 5:
        res.append(5)
        _x -= 5
    res.append(_x)
    return res
