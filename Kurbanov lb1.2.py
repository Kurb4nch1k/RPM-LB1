s = input()
paris = {')': '(', ']': '[', '}': '{'}

for c in s:
    if c in paris:
        if not paris[c] in s:
            print('False')
            break

print('True' if not paris.values() <= s else 'False')
