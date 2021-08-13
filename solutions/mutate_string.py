def mutate_string(string, position, character):
    if position == 0:
        return character + string[1:]
    return string[0:position] + character + string[position + 1:]