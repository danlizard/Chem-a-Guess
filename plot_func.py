def plotc(sm):
    compound = [[0, []]]
    depth = 0
    comp_branch = 0
    symbolc = -1
    cyclec =0
    ringc =False
    inorgc =False    
    for i in range(0, len(sm)):        
        if sm[i] == '(':
            ringc =False
            inorgc =False
            comp_branch +=1
            depth +=1
            symbolc = -1   
            compound.append([depth, []])
        elif sm[i] ==')':
            ringc =False
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
        return "Error due to uneven cycle "
    else:
        return compound, cyclec//2

def basic_funct(comp, cyclec):
    comp_branch = 0
    specbondlist = []
    positc = -1
    mainleng = [0]
    maintog = True
    for branch in range(len(comp)):
        for opern in range(len(comp[branch][1])):
            oper = comp[branch][1][opern]
            if 'A'<= oper[0] <='Z':
                positc +=1
                if comp[branch][0] == 0:
                    mainleng[0] +=1
                    if not maintog: 
                        mainleng[-1].append(opern)
                        maintog = True
                elif maintog:
                    mainleng.append([opern])
                    maintog = False                
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
        d_o_branchpos = 0
        checkbranch = 0
        cyclength = 0
        cycle = False
        for branch in range(len(comp)):
            if checkbranch ==2:
                local_d_o[0] = comp[branch][0]
                if local_d_o[0]>depthop and not local_d_o[1]:
                    local_d_o[1] = True
                    branchst = positc
                elif comp[branch][0]<comp[branch-1][0]:
                    if comp[branch][0]<depthop:
                        depthop = comp[branch][0]
                        d_o_branchpos = 0
                    else:
                        cyclength -= branchpos
                        d_o_branchpos -= branchpos
                        if local_d_o[0] == depthop and local_d_o[1]:
                            cyclength -= d_o_branchpos
                            d_o_branchpos = 0
                            local_d_o[1] = False
                        cyclist[cyclid-1].append([branchst+1, branchend])
            elif checkbranch ==1:
                if comp[branch][0]<comp[branch-1][0]:
                    cyclength = branchstcyc+1
                    start = start -branchstcyc
                    if depthop>0:
                        depthop -=1
                checkbranch =2
            branchpos = 0
            for opern in range(len(comp[branch][1])):
                oper = comp[branch][1][opern]
                if 'A'<= oper[0] <='Z':
                    positc +=1
                    branchpos +=1
                    if checkbranch != 0:
                        if comp[branch][0]>depthop:
                            d_o_branchpos +=1
                    print(d_o_branchpos, positc)
                    if cycle:
                        cyclength += 1
                if '%' in oper:
                    if int(oper.split('%')[1]) == cyclid:
                        if not cycle:
                            cyclength = 1        
                            start = positc
                            branchstcyc = branchpos
                            depthop = comp[branch][0]
                            local_d_o = [depthop, False]
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
    return specbondlist, cyclist, mainleng
    

if __name__ == "__main__" :
    canonsm = input()
    compound, cyclec = plotc(canonsm)
    print(compound)
    print(cyclec)
    print(basic_funct(compound, cyclec))