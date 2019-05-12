class A:
    pass
class B:
    pass
class C(A,B):
    pass

print(issubclass(C,A))
print(issubclass(C,B))
print(issubclass(A,C))


print(C.__mro__)
print(C.mro())
