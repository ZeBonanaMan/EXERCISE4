def remove_chars(word,number):
    if number >= len(word):
        return ""
    else:
        number_value = word[number:]
        return number_value

print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))