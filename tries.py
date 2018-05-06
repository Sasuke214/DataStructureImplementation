class Tries:
    def __init__(self):
        self.children=[None]*26
        self.size=0

    def getCharIndex(self,c):
        return ord(c)-ord('a')

    def setChild(self,value,child):
        self.children[self.getCharIndex(value)]=child
        
    def getChild(self,value):
        return self.children[self.getCharIndex(value)]

    def insertInternal(self,val,pos):
        self.size+=1
        if len(val)==pos:
            return

        
        characterIndex=self.getCharIndex(val[pos])
        child=self.children[characterIndex]
        if child==None:
            child=Tries()
            self.setChild(val[pos],child)        

        return child.insertInternal(val,pos+1)

        
    def insert(self,value):
        self.insertInternal(value,0)
        
        
    def countSubstringInternal(self,substring,index):
        if len(substring)==index:
            return self.size

        characterIndex=self.getCharIndex(substring[index])
        child=self.getChild(substring[index])
        
        if child==None:
            return -1
        return child.countSubstringInternal(substring,index+1)
    
        
    def countSubstring(self,substring):
        return self.countSubstringInternal(substring,0)


t=Tries()
t.insert("hy")
t.insert("hello")
t.insert("helmeppo")
t.insert("hell")

print(t.countSubstring("hy"))
