#string split & join:
def split_and_join(line):
    # write your code here
    line=line.split(' ')
    print(line)
    return '-'.join(line)
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# basic
def print_full_name(a, b):
    print("Hello {} {}! You just delved into python. ".format(first_name,last_name))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)