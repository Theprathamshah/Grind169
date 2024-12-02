def isValidParentheses(string):
    stack = []
    for i in string:
        if i == '[' or i == '(' or i == '{':
            stack.append(i)
        elif len(stack) and i == '}' and stack[-1] == '{':
            stack.pop()
        elif len(stack) and  i == ']' and stack[-1] == '[':
            stack.pop()
        elif len(stack) and  i == ')' and stack[-1] == '(':
            stack.pop()
        else: 
            return False
    return True
        
string = input()

if(isValidParentheses(string)):
    print(f"Parentheses {string} is valid.")
else:
    print(f"Parentheses {string} are not valid")
