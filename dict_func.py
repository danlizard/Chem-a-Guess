def prep_length(smiles):
    length = 0
    depth = 1
    for sym in smiles:
        if sym == '(':
            depth +=1 
        elif sym == ')':
            depth -=1 
        elif sym in 'QWERTYUIOPASDFGHJKLZXCVBNM' and depth == 1:
            length +=1
    return length

def prep_group(smiles):
    num = '1234567890%'
    addsym = '+=-#()[]*^@$:'
    cyclist = []
    maxit = 0
    atomc = 0
    for i in range(len(smiles)):
        if smiles[i] not in num and smiles[i] not in addsym:
            atomc+=1
        elif smiles[i] in num:
            j =i
            while j+1<len(smiles) and (smiles[j+1] in num):
                j+=1
            op = int(smiles[i:j+1])
            if op <= maxit:
                cyclist[op-1].append(atomc)
            else:
                maxit+=1
                cyclist.append([atomc])
    smiles = ''.join(smiles.split('%'))
    for i in range(0, 10):
        smiles = ''.join(smiles.split(str(i)))
    return smiles, cyclist

def placeholder_branch(line, mode):
    uppercase = 'QWERTYUIOPASDFGHJKLZXVBNM'
    stat = line
    line = line.replace('^', 'C')
    for i in range(len(line)-2):
        op = '('+'C'*i+')'
        while op in line:
            x = line.find(op)
            if mode == 'rep':
                line = line[:x] + '^'*(i+2) + line[x+i+2:]
            elif mode == 'del':
                line = line[:x] + line[x+i+2:]
    return(line)

def group_extract(stat, line, operline, gr, grdict):
    loclist = []
    locop = ''.join(line.split('^'))
    uppercase = 'QWERTYUIOPASDFGHJKLZXCVBNM^~'
    lowercase = 'qwertyuiopasdfghjklzxcvbnm'
    if gr in line:
        while gr in line:
            site = line.find(gr)
            i = 0
            for el in stat[:site+1]:
                if el in uppercase:
                    i+=1    
            loclist.append([i, grdict[gr]])
            operline = operline.replace(gr[1:],"^"*len(gr[1:]), 1)
            line = line.replace(gr[1:],"^"*len(gr[1:]), 1)
            operline = ''.join(operline.split('^'))
            operline = ''.join(operline.split('()'))
    else:
        site = locop.find(gr)
        i = 0
        for el in stat[:site+1]:
            if el in uppercase:
                i+=1    
        loclist.append([i, grdict[gr]])
        operline = operline.replace(gr[1:],"^"*len(gr[1:]), 1)
        line = line.replace(gr[1:],"^"*len(gr[1:]), 1)
        operline = ''.join(operline.split('^'))
        operline = ''.join(operline.split('()'))
    return operline, line, loclist

def ident_group(smiles, groupdict, absdict):
    uppercase = 'QWERTYUIOPASDFGHJKLZXCVBNM^'
    lowercase = 'qwertyuiopasdfghjklzxcvbnm'
    funclist = []
    opersmiles = smiles
    stat = smiles
    while any(gr in opersmiles for gr in groupdict.keys()):
        for gr in groupdict.keys():
            while gr in opersmiles:
                opersmiles, smiles, loclist = list(group_extract(stat, smiles, opersmiles, gr, groupdict))
                for el in loclist:
                    funclist.append(el)
                opersmiles = ''.join(opersmiles.split('^'))
                opersmiles = ''.join(opersmiles.split('()'))
                opersmiles = placeholder_branch(opersmiles, 'del')
                smiles = placeholder_branch(smiles, 'rep')
    while any(gr in opersmiles for gr in absdict.keys()):
        for gr in absdict.keys():
            if gr == opersmiles:
                return funclist
            while gr in opersmiles:
                site, localsite = smiles.find(gr), opersmiles.find(gr)
                atomid = localsite-1
                while opersmiles[atomid] not in uppercase:
                    atomid-=1
                if atomid<len(opersmiles)-1:
                    if opersmiles[atomid+1] in lowercase:
                        atom = opersmiles[atomid]+opersmiles[atomid+1]
                    else:
                        atom = opersmiles[atomid]                    
                else:
                    atom = opersmiles[atomid]
                i = 0
                for el in smiles[:site+1]:
                    if el in uppercase:
                        i+=1
                funclist.append([i, absdict[gr]+'-'+atom])
                opersmiles = opersmiles.replace(gr,"^"*len(gr), 1)
                smiles = smiles.replace(gr,"^"*len(gr), 1)
                opersmiles = ''.join(opersmiles.split('^'))
                opersmiles = ''.join(opersmiles.split('()'))
    return funclist

 
if __name__ == '__main__':
    from dicts_forfunc import *
    smiles, cyclist = prep_group(input())
    print(ident_group(smiles, func_dict, wildcard_dict), cyclist)
    
'''
fix CCCCNCC(C1=CC=C(C=C1)O)O
'''