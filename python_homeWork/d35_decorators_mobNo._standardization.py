def wrapper(f):
    def fun(l):
        # complete the function
        b=[]
        for i in l:
            # print(i,len(i))
            a='+91 '+(i[len(i)-10:len(i)-5])+' '+(i[len(i)-5:len(i)+1])
            b.append(a)
        # print(b)
        f(b)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 