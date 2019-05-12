'''
import textwrap

def wrap(string, max_width):
    result = textwrap.fill(string,max_width)
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
'''

#without using textwrap:
string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
max_width = 2
print(range(0,len(string),max_width))
print(list(range(0,len(string),max_width)))
for i in range(0,len(string),max_width):
    print(i)
    x = ''.join(string[i:i+max_width])
    print(x)