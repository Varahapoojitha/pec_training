#printing username and password
username=input()
passw=input()
if len(passw)<8:
  print('Please enter atleast 8 character length password')
else:
  print('Username:',username)
  print('Password:',passw)