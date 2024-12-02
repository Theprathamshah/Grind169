string = input()

rev = string[::-1]
if(string == rev):
    print(f"String {string} is palindrome")
else:
    print(f"String {string} is not palindrome")
print()
print(string == rev)