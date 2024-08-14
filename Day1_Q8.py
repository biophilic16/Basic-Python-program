#to check wheather palindrome or not
def palindrome(string):
    rstring=''.join(reversed(string))
    if string==rstring:
        print("Palindrome")
    else:
        print("Not a Palindrome")    

string=input("Enter the string:")
palindrome(string)        