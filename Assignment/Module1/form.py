mystr="form"
name=input("Enter your username:")
age=input("Enter your age:")
email=input("Enter your email:")
password=input("Enter your password:")
confirm_pass=input("Enter your confirm password:")
mobile_number=input("Enter your phone no::")


if name.isalpha():
  print("DONE")
else :
  print("error")


if age.isdigit():
 print("done")
else :
 print("error" )


if email.islower():
   print("done")
else:
  print("error")

if password==confirm_pass:
  print("done")
else:
   print("error")

length_of_no=len(mobile_number)
if mobile_number.isdigit() and length_of_no==10:
  print("done")
else :
  print("error")