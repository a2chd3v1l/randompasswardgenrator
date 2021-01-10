def passward() :
    import random
    n = int(input('Length of passward :'))
    word = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
    i = 0 
    end = ""
    while i < n :
       passw = random.choice(word)
       end += passw
       i += 1
    print(f'Your password is :{end}')   

if __name__ == "__main__":
    passward()
        