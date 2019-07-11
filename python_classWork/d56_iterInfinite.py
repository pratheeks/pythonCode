class Demo:
    def __iter__(self):
        self.n=1
        return self
    def __next__(self):
        nos=self.n
        self.n+=2
        return nos
d1=Demo()
i=iter(d1)
print(next(i))
print(next(i))
