str1=input("enter str1:")
substr=input("enter substr:")
count=0

if substr in str1:
    ss=str1.count(substr)
print("count of substring:",ss)
