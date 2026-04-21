def reverse(lst):
    if len(lst) == 0:
        return []
    return [lst[-1]] + reverse(lst[:-1])

if __name__ == "__main__":
    print(reverse([1, 2, 3, 4, 5]))