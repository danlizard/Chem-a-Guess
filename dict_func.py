def iter_group(smiles, groupdict, absdict):
    funclist = []
    opersmiles = smiles
    while any(gr in smiles for gr in groupdict.keys()):
        for gr in groupdict.keys():
            while gr in opersmiles:
                funclist.append([opersmiles.find(gr), groupdict[gr]])
                opersmiles = opersmiles.replace(gr,"^"*len(gr))
        opersmiles = ''.join(opersmiles.split('^'))
        opersmiles = ''.join(opersmiles.split('()'))