import pubchempy as pcp

def Find_Func(sm):
    functions = []
    cycles =True
    cyclnum = 1
    while cycles:
        try:
            cycle = sm[sm.find(str(cyclcnum))-1:sm.rfind(str(cyclcnum))]
            
        except:
            cycles =False
        return functions


canonsm = input()
A = Find_Func(canonsm)
print(*A)