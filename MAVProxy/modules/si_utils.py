def map_range(x, in_min, in_max, out_min, out_max):
    """
    Maps an input with a specified input range to a specified output range

    Parameters
    ----------
    x: float, int
        Input to be mapped
    in_min: float, int,
        Minimum of input range
    in_max: float, int,
        Maximum of input range
    out_min: float, int,
        Minimun of output range
    out_max: float, int,
        Maximum of output range

    Return
    -------
    out: float
        Scaled input value
    """

    x = float(x)
    in_min = float(in_min)
    in_max = float(in_max)
    out_min = float(out_min)
    out_max = float(out_max)
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
