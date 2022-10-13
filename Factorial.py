class ElementNotFoundException(Exception):
    pass
class InvalidInputException(Exception):
    pass

def search(list,element, index=0): 
    """
    The function takes an ordered list, an element to search for, and an index. It then divides the list in two,
    and checks if the element is in the left or right half of the list. If it's in the left half, it
    recursively calls itself on the left half of the list, and if it's in the right half, it recursively
    calls itself on the right half of the list. If the element is not in the list, it raises an
    exception.
    
    :param list: the list to search through
    :param element: the element to search for
    :param index: the index of the element in the original list, defaults to 0 (optional)
    :return: The index of the element in the list
    """
    if len(list) < 1 and element is not None:
        raise InvalidInputException()
    list_divider = len(list)//2
    if element != list[0] and len(list) == 1: 
        raise ElementNotFoundException()
    if element == list[0]:
        return index
    if element >= list[list_divider]:
        right_list = list[list_divider:]
        return search(right_list, element, list_divider+index)
    if element < list[list_divider]:
        left_list = list[:list_divider]
        return search(left_list,element, index)

