import numbers


def main(numbers):
    """
    A list called numbers is given. Return the items in the odd index.
    Args:
        numbers(list): parameter
    Returns:
        list: return answer.
    """
    numbers=[0,1,2,3,4,5]
    return numbers[::2]

print(main(numbers))
