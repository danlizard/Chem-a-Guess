def Plot(sm):
    compound = [[0, []]]
    depth = 0
    comp_branch = 0
    symbolc = -1
    cyclec =0
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
                cyclec +=1
            elif ('0'<= sm[i] <='9') and not ringc:
                ringc =True
                compound[comp_branch][1][symbolc] += '%'
                compound[comp_branch][1][symbolc] += sm[i]
                cyclec +=1
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
                        if (']' not in sm[i:i+5]) and ('[' not in sm[i:i+5]):
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
                    else:
                        compound[comp_branch][1][symbolc] += sm[i]
    if cyclec%2 != 0:
        print("Failed to locate an even amount of cycle ends, stopping")
        return "Cancel"
    else:
        return compound, cyclec//2

def Basic_Functionalize(comp, cyclec):
    comp_branch = 0
    specbondlist = []
    positc = -1
    # finding bonds
    for branch in range(len(comp)):
        for opern in range(len(comp[branch][1])):
            oper = comp[branch][1][opern]
            if 'A'<= oper[0] <='Z':
                positc +=1
            if oper in ['=', '#']:
                if oper == '=':
                    keyword = 'doub-'
                elif oper== '#':
                    keyword = 'trip-'
                if opern == 0:
                    if '%' in comp[branch-1][1][-1]:
                        keyword += comp[branch-1][1][-1].split('%')[0]
                    else:
                        keyword += comp[branch-1][1][-1]
                else:
                    if '%' in comp[branch][1][opern-1]:
                        keyword += comp[branch][1][opern-1].split('%')[0]
                    else:
                        keyword += comp[branch][1][opern-1]
                if '%' in comp[branch][1][opern+1]:
                    keyword += '-'+comp[branch][1][opern+1].split('%')[0]
                else:
                    keyword += '-'+comp[branch][1][opern+1]
                specbondlist.append([keyword, positc])
    cyclist = []
    for cyclid in range(1, cyclec+1):
        cyclist.append([])
        positc = -1
        checkbranch = 0
        cyclength = 0
        cycle = False
        for branch in range(len(comp)):
            if checkbranch ==2:
                if comp[branch][0]<comp[branch-1][0]:
                    if comp[branch][0]<depthop:
                        depthop = comp[branch][0]
                    else:
                        cyclength -= branchpos
                        cyclist[cyclid-1].append([branchst+1, branchend])
            elif checkbranch ==1:
                if comp[branch][0]<comp[branch-1][0]:
                    cyclength = branchst+1
                checkbranch +=1
            branchpos = 0
            branchst = positc
            for opern in range(len(comp[branch][1])):
                oper = comp[branch][1][opern]
                if 'A'<= oper[0] <='Z':
                    positc +=1
                    branchpos +=1
                    if cycle:
                        cyclength += 1
                if '%' in oper:
                    if int(oper.split('%')[1]) == cyclid:
                        if not cycle:
                            cyclength = 1        
                            start = positc
                            branchstcyc = branchpos
                            depthop = comp[branch][0]
                            cycle = True
                            if branch == 0:
                                checkbranch +=2
                            else:
                                checkbranch +=1
                        elif cycle:
                            cycle = False
                            end = positc
                            checkbranch +=1
            branchend = positc
        cyclist[cyclid-1].append([start, end, cyclength])
    return specbondlist, cyclist
    

#import pubchempy as pcp
#canonsm = input().canonical_smiles
canonsm = input()
compound, cyclec = Plot(canonsm)
print(compound)
print(cyclec)
print(Basic_Functionalize(compound, cyclec))
i = input()