def String_pallindrome():
    txt=input('Enter a string: ')
    if txt==txt[::-1]:
        print('The string is pallindrome')
    else:
        print('the string is not pallindrome')
print(String_pallindrome())
