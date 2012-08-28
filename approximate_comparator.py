from insignificant_digit_cutter import cut_insignificant_digits_recursively

def is_almost_equal(first, second, places=7):
    '''returns False if first and second aren't equal up to a desired precision.
    Given two data structures, returns True if all elements of these structures
    (in any nesting level) are either equal or almost equal.
    floats are almost equal if they're equal when we consider only the
    [places] most significant digits of each.
    '''
    if first == second: return True
    cut_first = cut_insignificant_digits_recursively(first, places)
    cut_second = cut_insignificant_digits_recursively(second, places)
    return cut_first == cut_second
