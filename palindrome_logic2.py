s1 = input("Enter the string to check palindrome:")
s2 = ""
for i in s1:
    s2 = i+s2
    if(s1 == s2):
        print("Yes, it is Palindrome")
    else:
        print("No, it is Palindrome")
