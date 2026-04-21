def count(s):
    if len(s) == 0:
        return 0
    return 1 + count(s[1:])

if __name__ == "__main__":
    print(count("hello world"))