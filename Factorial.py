class ElementNotFoundException(Exception):
    pass
class InvalidInputException(Exception):
    pass

def search(list,element, index=0): 
    if len(list) < 1 and element is not None:
        raise InvalidInputException()
    # divide list in two
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

