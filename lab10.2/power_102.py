def power(m,n):
    if n == 0:
        return 1
    else:
        return m * power(m,n-1)
    
if __name__ == "__main__":
    print(power(2,5))