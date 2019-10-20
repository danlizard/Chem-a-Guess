def Plot(sm):
    compound = [[0, '']]
    depth = 0
    comp_branch = 0
    for i in range(0, len(sm)):
        ringc =False
        elemc =False
        if sm[i] == '(':
            comp_branch +=1
            depth +=1
            if ringc:
                compound[comp_branch][1] += '%'
                ringc =False
            if elemc:
                compound[comp_branch][1] += ']'
                elemc =False
            compound.append([depth, ''])
        elif sm[i] ==')':
            comp_branch +=1
            depth -=1
            if ringc:
                compound[comp_branch][1] += '%'
                ringc =False
            if elemc:
                compound[comp_branch][1] += ']'
                elemc =False            
            compound.append([depth, ''])
        else:
            if elemc:
                elemc = False
                compound[comp_branch][1] += ']'            
            if sm[i] == '%':
                ringc =True
                compound[comp_branch][1] += '%'
            if ('1'<= sm[i] <='9') and not ringc:
                ringc =True
                compound[comp_branch][1] += '%'
                compound[comp_branch][1] += sm[i]
            elif ('1'<= sm[i] <='9') and ringc:
                compound[comp_branch][1] += sm[i]
            elif ringc and sm[i] == '%':
                print('Encountered unneeded "%" at i around', i)
                print('Plz check this SMILES for mistakes! Proceed?')
                if input() != 'Y':
                    return 'stopped'
            else:
                if ringc:
                    ringc = False
                    compound[comp_branch][1] += '%'
                if sm[i] == '[':
                    elemc =True
                    compound[comp_branch][1] += '['
                elif ('A'<= sm[i] <='Z') and elemc:
                    compound[comp_branch][1] += sm[i]
                elif ('a'<= sm[i] <='z') and elemc:
                    compound[comp_branch][1] += sm[i]
                    if i != len(sm)-1:
                        if sm[i+1] != ']':
                            elemc =False
                            compound[comp_branch][1] += ']'
                elif sm[i] == ']':
                    elemc =False
                    compound[comp_branch][1] += ']'
                elif ('a'<= sm[i] <='z') and elemc:
                    elemc =False
                    compound[comp_branch][1] += sm[i]
                    compound[comp_branch][1] += ']'
                elif ('A'<= sm[i] <='Z') or ('a'<= sm[i] <='z') and not elemc:
                    compound[comp_branch][1] += '['
                    compound[comp_branch][1] += sm[i]
                    if i != len(sm)-1:
                        if 'a'<= sm[i+1] <='z':
                            elemc =True
                        else:
                            compound[comp_branch][1] += ']' 
                    else:
                        compound[comp_branch][1] += ']'
    
    return compound


#import pubchempy as pcp
#canonsm = input().canonical_smiles
canonsm = input()
print(Plot(canonsm))
i = input()