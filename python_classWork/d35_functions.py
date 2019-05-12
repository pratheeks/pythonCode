#keyword Function:
def demo(a,b):
    print("the value of a=",a)
    print("the value of b=",b)
#demo(10,20)
#demo(b=10,a=20)
#demo(10,b=20)
#demo(a=30,40)

#arbitrary Function:
def student_name(*name):
    for i in name:
        print(i)
student_name('p','u','r','s','a')


