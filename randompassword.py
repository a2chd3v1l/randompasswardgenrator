def passward() :
    import random
    n = int(input("Length of passward is : "))
    word = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%({)}<>:;~[]/|"
    i = 0
    end = "" 
    while i < n :
       passw = random.choice(word)
       end+= passw
       i += 1
    print(f'Your password is : {end}')   

if __name__ == "__main__":
    passward()
        
