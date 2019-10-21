def Plot(sm):
    compound = [[0, []]]
    depth = 0
    comp_branch = 0
    symbolc = -1
    ringc =False
    inorgc =False    
    for i in range(0, len(sm)):        
        if sm[i] == '(':
            if ringc:
                compound[comp_branch][1][symbolc] += '%'
                ringc =False
            comp_branch +=1
            depth +=1
            symbolc = -1   
            compound.append([depth, []])
        elif sm[i] ==')':
            if ringc:
                compound[comp_branch][1][symbolc] += '%'
                ringc =False
            comp_branch +=1
            depth -=1 
            symbolc = -1
            compound.append([depth, []])
        else:
            if not ringc and sm[i] == '%':
                ringc =True
                compound[comp_branch][1].append('%')
                symbolc += 1
            elif ('1'<= sm[i] <='9') and not ringc:
                ringc =True
                compound[comp_branch][1].append('%')
                symbolc += 1
                compound[comp_branch][1][symbolc] += sm[i]
            elif ('1'<= sm[i] <='9') and ringc:
                compound[comp_branch][1][symbolc] += sm[i]
            elif ringc and sm[i] == '%':
                print('Encountered unneeded "%" at i around', i)
                print('Plz check this SMILES for mistakes! Proceed?')
                if input() != 'Y':
                    return 'stopped'
            else:
                if ringc:
                    ringc = False
                    compound[comp_branch][1][symbolc] += '%'
                if sm[i] == '[':
                    inorgc =True
                    symbolc += 1
                    compound[comp_branch][1].append('')
                elif ('A'<= sm[i] <='Z') and inorgc:
                    compound[comp_branch][1][symbolc] += sm[i]
                elif ('a'<= sm[i] <='z') and inorgc:
                    compound[comp_branch][1][symbolc] += sm[i]
                elif sm[i] == ']':
                    inorgc =False
                elif ('A'<= sm[i] <='Z') or ('a'<= sm[i] <='z') and not inorgc:
                    compound[comp_branch][1].append('')
                    if sm[i] != 'r' and sm[i] != 'l':
                        symbolc += 1
                    compound[comp_branch][1][symbolc] += sm[i]
                    
    
    return compound


#import pubchempy as pcp
#canonsm = input().canonical_smiles
canonsm = input()
print(Plot(canonsm))
i = input()