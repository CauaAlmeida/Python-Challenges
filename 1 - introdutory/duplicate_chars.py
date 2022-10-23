def removeDuplicates(your_str):
    final = ''
    for char in your_str:
        if char not in final:
            final += char
    return final


string = input("Type the string you want to remove duplicate characters from: ")

no_duplicates = removeDuplicates(string)

print(no_duplicates)
