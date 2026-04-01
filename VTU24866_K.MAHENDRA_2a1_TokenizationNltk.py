s = input("Enter a string: ")

middle = len(s) // 2

result = s[middle-1 : middle+2]
print("Result:", result)