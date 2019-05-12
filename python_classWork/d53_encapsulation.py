class ICICI:
    def __init__(self):
        self.__fdint=6.8
        
    def disp(self):
        print("fixed deposit",self.__fdint)
        
    def setint(self,i):
        self.__fdint=i
        
C=ICICI()
C.disp()

C.__fdint=7.8
C.disp()

C.setint(7.1)
C.disp()