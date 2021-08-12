def swap_case(s):
    swapped = []
    for i in range(0, len(s)):
        if s[i].isalnum():
            if s[i].islower():
                temp = s[i].upper()
                swapped.append(temp)
            else:
                temp = s[i].lower()
                swapped.append(temp)
        else: swapped.append(s[i])
    return "".join(char for char in swapped)