class stack:
    def __init__(self) -> None:
        self.s=[]
    def push(self,ch):
        self.s.append(ch)
    def pop1(self):
        return self.s.pop()
    
class Bracket1:
    
    def matching(self,sentance):
        st=stack()
        for i in sentance:
            if (i=='{' or i=='(' or i =='['):
                st.push(i)

            else:
                if(i=='}'):
                    temp=st.pop1()
                    if(temp!='{'):
                        return 0
                if(i==')'):
                    temp=st.pop1()
                    if(temp!='('):
                        return 0
                if(i==']'):
                    temp=st.pop1()
                    if(temp!='['):
                        return 0
                    
        if(len(st.s)==0):
            print("all the brackets are matching ")
            return True
        else:
            print("the brackets are not matching ")
            return False
b=Bracket1()

ex=input("enter the sentence")
m=b.matching(ex)
print(m)
