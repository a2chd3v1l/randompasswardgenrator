import random
from string import ascii_letters, digits, punctuation


n = int(input("Length of passward is : "))
word = ascii_letters + digits + punctuation

def passward() :
    i = 0
    end = "" 
    while i < n :
       passw = random.choice(word)
       end+= passw
       i += 1
    print(f'Your password is : {end}')   

if __name__ == "__main__":
    passward()
