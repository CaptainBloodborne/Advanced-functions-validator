def validate(low_bound: int, upper_bound: int):
    """ Checks if set_pixel params out of bound

    Parameters
    ----------
    low_bound : int
        the lower allowed limit for setting pixel
    upper_bound : int
        the max allowed limit for setting pixel
    """
    def decorator(func: callable):
        def wrapper(*args, **kwargs):
            for pixel in args:
                if pixel not in range(low_bound, upper_bound + 1):
                    return "Function call is not valid!"
            return func(*args)
        return wrapper
    return decorator


@validate(10, 100)
def set_pixel(red: int, green: int, blue: int) -> str:
    """A function for creating a pixel.
    Parameters
    ----------
    red : int
        number for red rgb range
    green : int
        number for green rgb range
    blue : int
        number for blue rgb range

    Returns
    ---------
    str
        Status for creating pixel

    """
    return "Pixel created!"
