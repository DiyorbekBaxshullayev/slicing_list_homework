def main(list1):
    """
    A list of several elements is given. Return the three elements from the beginning.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    return list1[:3]

a=[1,2,3,4,5,6,7,8,9,10]
print(main(a))