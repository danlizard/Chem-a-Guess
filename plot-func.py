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
                ringc =False
            if inorgc:
                inorgc =False
            comp_branch +=1
            depth +=1
            symbolc = -1   
            compound.append([depth, []])
        elif sm[i] ==')':
            if ringc:
                ringc =False
            if inorgc:
                inorgc =False
            comp_branch +=1
            depth -=1 
            symbolc = -1
            compound.append([depth, []])
        else:
            if not ringc and sm[i] == '%':
                ringc =True
                compound[comp_branch][1][symbolc] += '%'
            elif ('0'<= sm[i] <='9') and not ringc:
                ringc =True
                compound[comp_branch][1][symbolc] += '%'
                compound[comp_branch][1][symbolc] += sm[i]
            elif ('0'<= sm[i] <='9') and ringc:
                compound[comp_branch][1][symbolc] += sm[i]
            elif ringc and sm[i] == '%':
                print('Encountered unneeded "%" at i around', i)
                print('Plz check this SMILES for mistakes! Proceed?')
                if input() != 'Y':
                    return 'stopped'
            else:
                if ringc:
                    ringc = False
                if sm[i] == '[':
                    inorgc =True
                    symbolc += 1
                    compound[comp_branch][1].append('')
                elif ('A'<= sm[i] <='Z') and inorgc:
                    compound[comp_branch][1][symbolc] += sm[i]
                    if i+4 < len(sm):
                        if ']' not in sm[i:i+5] and '[' not in sm[i:i+5]:
                            inorgc = False
                elif ('a'<= sm[i] <='z') and inorgc:
                    compound[comp_branch][1][symbolc] += sm[i]
                    if i+4 < len(sm):
                        if ']' not in sm[i:i+5] and '[' not in sm[i:i+5]:
                            inorgc = False                   
                elif sm[i] == ']':
                    inorgc = False
                elif ('A'<= sm[i] <='Z') or ('a'<= sm[i] <='z') and not inorgc:
                    compound[comp_branch][1].append('')
                    if sm[i] != 'r' and sm[i] != 'l':
                        symbolc += 1
                    compound[comp_branch][1][symbolc] += sm[i]
                elif sm[i] == '-' or sm[i] == '+' and inorgc:
                    if '1' <= sm[i+1] <= '9':
                        ringc = True
                    compound[comp_branch][1][symbolc] += sm[i]
                elif sm[i] == '=' or sm[i] == '#':
                    if not inorgc:
                        compound[comp_branch][1].append(sm[i])
                        symbolc += 1
                        inorgc = True
                    else:
                        compound[comp_branch][1][symbolc] += sm[i]
    return compound

#def Functionalize(comp):
    

#import pubchempy as pcp
#canonsm = input().canonical_smiles
canonsm = input()
compound = Plot(canonsm)
print(compound)
print(Functionalize(compound))
i = input()