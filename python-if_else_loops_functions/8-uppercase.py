#!/usr/bin/python3
def uppercase(str):
    ans = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            up_char = chr(ord(i) - 32)
            ans += "{}".format(up_char)
        else:
            ans += "{}".format(i)
    print("{}".format(ans))
