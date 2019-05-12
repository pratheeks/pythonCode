#f = open("python.txt",encoding='utf-8')
#print(f)
##f.close()
#print(f)
#print(f.read())
#
#
#try:
#    f = open("python.txt",encoding='utf-8')
#    print(f)
#finally:
#    f.close()
#    print(f)
#    


with open("python.txt","w",encoding='utf-8') as f:
    print(f.write("This is python class.\n"))
    print(f.write("Thank you"))