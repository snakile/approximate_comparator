from insignificant_digit_cutter import cut_insignificant_digits_recursively

def is_almost_equal(first, second, places):
    '''returns True if first and second equal. 
    returns true if first and second aren't equal but have exactly the same
    structure and values except for a bunch of floats which are just almost
    equal (floats are almost equal if they're equal when we consider only the
    [places] most significant digits of each.'''
    if first == second: return True
    cut_first = cut_insignificant_digits_recursively(first, places)
    cut_second = cut_insignificant_digits_recursively(second, places)
    return cut_first == cut_second