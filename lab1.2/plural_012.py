#!/usr/bin/env python3
import sys

for noun in sys.stdin:
    noun = noun.rstrip("\n")
    if noun.endswith("s") or noun.endswith("x") or noun.endswith("z") or noun.endswith("ch") or noun.endswith("sh") or noun.endswith("o"):
        print(f"{noun}es")
    elif noun.endswith("y") and len(noun) > 1 and noun[-2] not in "aeiou":
        print(f"{noun[:-1]}ies")
    elif noun.endswith("f"):
        print(f"{noun[:-1]}ves")
    elif noun.endswith("fe"):
        print(f"{noun[:-2]}ves")
    else:
        print(f"{noun}s")