def remove_duplicate(your_str):
   result = ''
   for char in your_str:
       if char not in result:
           result += char
   return result
 
user_input = input('what is your string:')
 
no_duplicate = remove_duplicate(user_input)
print('Without duplicate: ', no_duplicate)