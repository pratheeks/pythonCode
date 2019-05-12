'''N=3     #int(input())
for i in range (-(N-1),N):
    for j in range (-2*(N-1),2*(N-1)+1):
        if j%2==0 and (abs(j//2)+abs(i))< N:
              print (chr(abs(j//2)+abs(i)+ord('a')),end='')
        else:
              print('-',end='')
    print()'''
def print_rangoli(size):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', '1']
    letter = alpha[size]
    if alpha[size - 1] == "a":
        print("a")
    else:
        # middle part
        first_part = ""
        for i in alpha:
            if i == letter:
                break
            else:
                first_part = first_part + "-" + i
        second_part = first_part.replace("-a-", "")
        first_part = first_part[::-1]
        parts = first_part + second_part
        # haut part
        lenght = (len(parts) - 1) // 2
        haut_part = parts[0:1]
        first_lenght = 4
        second_lenght = len(parts) - 1
        for i in range(1, size):
            print(haut_part.center(len(parts), "-"))
            haut_part = parts[0:first_lenght] + parts[second_lenght:len(parts)]
            first_lenght += 2
            second_lenght -= 2

        print(parts)

        # bottom part
        if alpha[size - 1] == "b":
            for i in range(1, size):
                parts = parts.replace(parts[(len(first_part) - 2):(len(first_part) + 2)], "")
                parts = ("-" * 2) + parts + ("-")
                print(parts)
        else:
            for i in range(1, size):
                parts = parts.replace(parts[(len(first_part) - 2):(len(first_part) + 2)], "")
                parts = ("-" * 2) + parts + ("-" * 2)
                print(parts)
print_rangoli(3)
'''
def print_rangoli(size):
    width  = size*4-3
    string = ''
    for i in range(1,size+1):
        for j in range(0,i):
            string += chr(96+size-j)
            if len(string) < width :
                string += '-'
        for k in range(i-1,0,-1):    
            string += chr(97+size-k)
            if len(string) < width :
                string += '-'
        print(string.center(width,'-'))
        string = ''
    for i in range(size-1,0,-1):
        string = ''
        for j in range(0,i):
            string += chr(96+size-j)
            if len(string) < width :
                string += '-'
        for k in range(i-1,0,-1):
            string += chr(97+size-k)
            if len(string) < width :
                string += '-'
        print(string.center(width,'-'))       
print_rangoli(5)
        
'''
        
'''    
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

'''