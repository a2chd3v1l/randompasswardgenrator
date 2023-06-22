#! /usr/bin/env python
import random
import argparse
from string import ascii_letters, digits, punctuation


parser = argparse.ArgumentParser(description="Generate a random password of length n . ")
parser.add_argument("-l", "--length",dest="length", help="Length of password")
args = parser.parse_args()

words = ascii_letters + digits + punctuation
def passward(words,n=8) :
    passwd = "".join(random.sample(words,n))
    print(f'Your password is : {passwd}')

if __name__ == "__main__":
    if args.length:
        passward(words,n=int(args.length))
    else:
        passward(words)
