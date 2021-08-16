def timeConversion(s):
    a, b, c = s[0:len(s) - 2].split(":")
    if a == "12":
        if s[-2] == "A":
            a = "00"
    elif s[-2] == "P": a = str(int(a) + 12)
    return ":".join((a, b, c))