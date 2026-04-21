def smallest(lst):
    if len(lst) == 1:
        return lst[0]
    
    rest = smallest(lst[1:])
    
    if lst[0] < rest:
        return lst[0]
    return rest

if __name__ == "__main__":
    print(smallest([3, 1, 4, 1, 5, 9]))