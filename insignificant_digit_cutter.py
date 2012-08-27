def cut_insignificant_digits(number, places):
    '''cut the least significant decimal digits of a number, leaving only [places] decimal digits'''
    if  type(number) != float: return number
    number_as_str = str(number)
    end_of_number = number_as_str.find('.')+places+1
    if end_of_number > len(number_as_str): return number
    return float(number_as_str[:end_of_number])

def cut_insignificant_digits_lazy(iterable, places):
    for obj in iterable:
        yield cut_insignificant_digits_recursively(obj, places)

def cut_insignificant_digits_recursively(obj, places):
    '''return a copy of obj except that every float loses its least significant 
    decimal digits remaining only [places] decimal digits'''
    t = type(obj)
    if t == float: return cut_insignificant_digits(obj, places)
    if t in (list, tuple, set):
        return t(cut_insignificant_digits_lazy(obj, places))
    if t == dict:
        return {cut_insignificant_digits_recursively(key, places):
                cut_insignificant_digits_recursively(val, places)
                for key,val in obj.items()}
    return obj