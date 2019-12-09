def plotc(sm):
    compound = [[0, []]]
    depth = 0
    comp_branch = 0
    symbolc = -1
    atomlist = []
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
                    atomlist.append('')
                elif ('A'<= sm[i] <='Z') and inorgc:
                    compound[comp_branch][1][symbolc] += sm[i]
                    if i+4 < len(sm):
                        if (']' not in sm[i:i+5]) and ('[' not in sm[i:i+5]):
                            inorgc = False
                    atomlist[-1] += sm[i]
                elif ('a'<= sm[i] <='z') and inorgc:
                    compound[comp_branch][1][symbolc] += sm[i]
                    if i+4 < len(sm):
                        if ']' not in sm[i:i+5] and '[' not in sm[i:i+5]:
                            inorgc = False                  
                    atomlist[-1] += sm[i]
                elif sm[i] == ']':
                    inorgc = False
                elif ('A'<= sm[i] <='Z') or ('a'<= sm[i] <='z') and not inorgc:
                    compound[comp_branch][1].append('')
                    if sm[i] != 'r' and sm[i] != 'l':
                        symbolc += 1
                    compound[comp_branch][1][symbolc] += sm[i]
                    atomlist.append(sm[i])
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
        return compound, cyclec//2, atomlist


def basic_funct(comp, cyclec):
    comp_branch = 0
    specbondlist = []
    positc = -1
    mainleng = [0]
    specatoms = []
    maintog = True
    for branch in range(len(comp)):
        for opern in range(len(comp[branch][1])):
            oper = comp[branch][1][opern]
            if 'A'<= oper[0] <='Z':
                positc +=1
                if oper[0] in ['N', 'O']:
                    specatoms.append([positc, oper[0]])
                if comp[branch][0] == 0 and maintog:
                    mainleng[0] +=1
                elif comp[branch][0]>0 and maintog:
                        mainleng.append([positc])
                        maintog = False
                elif comp[branch][0] == 0 and not maintog:
                    mainleng[-1].append(positc-1)
                    maintog = True              
                    mainleng[0] +=1
            if oper in ['=', '#']:
                if oper == '=':
                    keyword = 'd-'
                elif oper== '#':
                    keyword = 't-'
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
    return specbondlist, cyclist, mainleng, specatoms
    

def add_funct(bonds, cycles, skel, specat, atoms, comp):
    funclist = [skel[0]]
    conjug = []
    construct = []
    mainline = ''
    mainop = []
    for i in range(1, len(skel)):
        mainop.append(range(skel[i][0], skel[i][1]))
    for pos in atoms:
        neg = False
        for rng in mainop:
            if pos in rng:
                neg = True
        if not neg:
            mainline += pos
    funclist.append(mainline)
    typ, ap1, ap2= bonds[0][0].split('-')
    loc = bonds[0][1]
    a1, a2 = ap1, ap2
    if len(bonds)>1:
        conj = False
        for i in range(1, len(bonds)):
            if bonds[i][1] == bonds[i-1][1]+2:
                if not conj:
                    conjug.append([bonds[i-1][1]])
                    conj = True
            elif conj:
                conj = False
                conjug[-1].append(bonds[i][1]+1)
    for i in range(len(bonds)):
        ap1, ap2 = a1, a2
        typ, a1, a2 = bonds[i][0].split('-')
        loc = bonds[i][1]
        construct.append(loc)
        construct.append([typ, a1, a2])
    for oper in specat:
        locat, atom = oper[0], oper[1]
        if locat-1 in construct:
            sec = construct.pop(construct.index(locat-1)+1)
            construct.pop(construct.index(locat-1))
            if locat-1 in construct:
                funclist.append([(locat-1), atom+sec[1]+sec[0]+sec[2]])
                while locat-1 in construct:
                    sec = construct.pop(construct.index(locat-1)+1)
                    construct.pop(construct.index(locat-1))
                    funclist.append([(locat-1), atom+sec[1]+sec[0]+sec[2]])
            else:
                funclist.append([locat-1, sec[1]+sec[0]+sec[2]])
            specat.pop(specat.index(oper))
    for i in range(0, len(construct), 2):
        funclist.append([construct[i], construct[i+1][1]+construct[i+1][0]+construct[i+1][2]])
    for i in range(0, len(specat)):
        funclist.append([specat[i][0]-1, atoms[specat[i][0]-1]+'s'+specat[i][1]])
    return funclist


if __name__ == "__main__" :
    canonsm = input()
    compound, cyclec, atoms = plotc(canonsm)
    print(atoms)
    print(compound)
    print(cyclec)
    bonds, cycles, skel, specat = basic_funct(compound, cyclec)
    print(bonds)
    funclist = add_funct(bonds, cycles, skel, specat, atoms, compound)
    print(funclist)
    