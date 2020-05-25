passwordFile = open('passWords.txt')
secretPassword = passwordFile.read()
print('Enter Password.')
typedPassword = input()
if typedPassword == secretPassword:
    print('Access Granted')
    if typedPassword == '12345':
        print("That password is one that an idiots puts on their luggage")
else:
    print("Access Denied")