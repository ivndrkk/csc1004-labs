def sumup(n):
    if n == 0:
        return 0
    else:
        return n + sumup(n-1)
    
if __name__ == "__main__":
    print(sumup(5))