#!/bin/python3

def timeConversion(s):
        if s[-2]=='A' and s[:2]!='12':
            print(s[-2])
        elif s[-2]=='A' and s[:2]=='12':
            t=int(s[:2])-12
            print(str(t)+'0'+s[2:-2])
        elif s[-2]=='P' and s[:2]!='12':
            t=int(s[:2])+12
            print(str(t)+s[2:-2])
        else:
            print(s[:-2])
    
if __name__ == '__main__':

    s = input()

    result = timeConversion(s)
