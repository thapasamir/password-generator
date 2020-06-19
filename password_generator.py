import random
import string
name = input("Enter your name::")
psw_length = input(f'hello {name} of long paassword do you want?')
INT_pas=int(psw_length)
if INT_pas < 6 and INT_pas > 6:
    print("password must be above 6 character and below 12 character")


password =''.join([random.choice(string.ascii_letters+string.digits+string.punctuation)for i in range(INT_pas)])
print(password)
f= open("yourpassword.txt", "w+")
f.write(f'This is your password::{password}')