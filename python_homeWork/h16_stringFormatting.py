def print_Formatted(n):
    x=len(bin(n)[2:])
    for i in range(1,n+1):
        oc=oct(i)[2:]
        he=hex(i)[2:].upper()
        bi=bin(i)[2:]
        print(str(i).rjust(x),oc.rjust(x),he.rjust(x),bi.rjust(x))
#def print_Formatted(n):
#    x=len(bin(n)[2:])
#    for i in range(1,n+1):
#        oc=oct(i)[2:]
#        he=hex(i)[2:].upper()
#        bi=bin(i)[2:]
#        print(i,oc,he,bi)
print_Formatted(17)

