a_string = input("Enter the string")
string_set = set(a_string)
punctuation_set = set(string.punctuation)

if string_set.intersection(punctuation_set):
     print("Has a special character")