str = input("Enter the string to check palindrome:")
str = str.casefold()                                  #for caseless compare

if(str == str[::-1]):
   print("Yes, it is Palindrome")
else:
    print("No,it is Palindrome")