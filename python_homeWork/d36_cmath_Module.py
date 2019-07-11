#method1:
x=  1+2j
print(x.real,x.imag)
print((x.real**2+x.imag**2)**0.5)
import cmath
print(cmath.phase(x))

#method2:
print(*cmath.polar(x))