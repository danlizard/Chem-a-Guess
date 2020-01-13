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
            while smiles[j+1] in num:
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

def ident_group(smiles, groupdict, absdict):
    uppercase = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    lowercase = 'qwertyuiopasdfghjklzxcvbnm'
    funclist = []
    opersmiles = smiles
    stat = smiles
    while any(gr in smiles for gr in groupdict.keys()):
        for gr in groupdict.keys():
            while gr in opersmiles:
                site = smiles.find(gr)
                i = 0
                for el in stat[:site+1]:
                    if el in uppercase:
                        i+=1
                funclist.append([i, groupdict[gr]])
                opersmiles = opersmiles.replace(gr,"^"*len(gr), 1)
                smiles = smiles.replace(gr,"^"*len(gr), 1)
        opersmiles = ''.join(opersmiles.split('^'))
        opersmiles = ''.join(opersmiles.split('()'))
    while any(gr in smiles for gr in absdict.keys()):
        for gr in absdict.keys():
            while gr in opersmiles:
                site, localsite = smiles.find(gr), opersmiles.find(gr)
                atomid = localsite
                while opersmiles[atomid] not in uppercase:
                    atomid-=1
                if opersmiles[atomid+1] in lowercase:
                    atom = opersmiles[atomid]+opersmiles[atomid+1]
                else:
                    atom = opersmiles[atomid]
                i = 0
                for el in smiles[:site+1]:
                    if el in uppercase:
                        i+=1
                funclist.append([i, absdict[gr]+atom])
                opersmiles = opersmiles.replace(gr,"^"*len(gr), 1)
                smiles = smiles.replace(gr,"^"*len(gr), 1)
            opersmiles = ''.join(opersmiles.split('^'))
            opersmiles = ''.join(opersmiles.split('()'))
    return funclist

 
if __name__ == '__main__':
    from dicts_forfunc import *
    smiles, cyclist = prep_group(input())
    print(ident_group(smiles, func_dict, wildcard_dict))