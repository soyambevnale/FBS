def checkpalindrome(st):
    rev_str=''
    for char in st:
        rev_str=char+rev_str
        print(rev_str)
        
    if (st==rev_str):
        print("Given string is palindrome .")
    else:
        print("Given string is not palindrome .")
        
str='racecar'
checkpalindrome(str)