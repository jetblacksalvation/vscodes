#implement a queue with functions, and given arguements 
#psuedo code --- function= list()
#list.pushback(functoin, kwargs)

#class queue:
#    __init__(self, arg1, *argv):
        
class func_queue:

    def __init__(self, funcList, argsList):
        self.funcList: list = funcList
        self.argsList: list = argsList
        
    def re(self):
        self.funcList[0](self.argsList[0])
        self.funcList.remove(self.funcList[0])
        self.argsList.remove(self.argsList[0])
        
    def call(self):
        self.func(self.args)

def var_print(*args):
    temp = list(args)
    print(temp)
        
def var_add(*args):
    temp = list(args)
    print(temp)
        
        
        
#call stuff here 
bruh = func_queue([var_print, var_add],[["bruh", 32, "hello world"],[3,4]])
bruh.re()
bruh.re()