def local_retr(cid):
    op = get_first_layer_props(cid, ['CanonicalSMILES', 'IUPACName'])
    smiles = op['CanonicalSMILES']
    name = op['IUPACName']
    qual = get_second_layer_props(cid, ['Melting Point', 'Boiling Point'])
    print(qual)
    if 'Boiling Point' in qual.keys():
        boiltemp = []
        for el in qual['Boiling Point']:
            op = el['Value']
            if 'StringWithMarkup' in op.keys():
                op = op['StringWithMarkup'][0]['String']
                if 'C' in op:
                    op = (''.join(op.split(' '))).split('°')[0]
                    if '-' in op:
                        op = op.split('-')
                        op = (float(op[0])+float(op[1]))/2
                    else:
                        op = float(op)
                    boiltemp.append(op)
            elif 'Number' in op.keys():
                if 'C' in op['Unit']:
                    boiltemp.append(float(op['Number'][0]))
        boiltemp = str(sum(boiltemp)/len(boiltemp))
    else:
        return 'MissingInfoError'
    if 'Melting Point' in qual.keys():
        melttemp = []
        for el in qual['Melting Point']:
            op = el['Value']
            if 'StringWithMarkup' in op.keys():
                op = op['StringWithMarkup'][0]['String']
                if 'C' in op:
                    op = (''.join(op.split(' '))).split('°')[0]
                    if '-' in op:
                        op = op.split('-')
                        op = (float(op[0])+float(op[1]))/2
                    else:
                        op = float(op)
                    melttemp.append(op)
            elif 'Number' in op.keys():
                if 'C' in op['Unit']:
                    melttemp.append(float(op['Number'][0]))              
        melttemp = str(sum(melttemp)/len(melttemp))
    else:
        return 'MissingInfoError'
    qual = 'Melting Point = '+melttemp+'; '+'Boiling Point = '+boiltemp
    return name+'^^'+smiles+'^^'+qual
"""
def opt_local_retr(cid, addit=None, opt='Melting Point, Boiling Point'):
    name = (pcp.Compound.from_cid(cid)).iupac_name
    smiles = get_first_layer_props(name, ['CanonicalSMILES'])
    if addit != None:
        easyquals = addit.split(', ')
        additionals = get_first_layer_props(name, easyquals)
    hardquals = opt.split(', ')
    qual = get_second_layer_props(name, hardquals)
    return smiles, additionals, qual
"""
"""
def local_onepack(namefile='names.txt', qualfile='quals.txt', funcfile='rawfuncs.txt', *args):
    if args == None:
        raise TypeError('EmptyPackageError')
    namefile = 'localdata\\' + namefile
    funcfile = 'localdata\\' + funcfile
    qualfile = 'localdata\\' + qualfile
    spdict = {
        'name':namefile,
        'qual':qualfile,
        'func':funcfile}
    space = args.pop(-1)
    current = open(spdict[space], 'a')
    current.write(args)
    current.close()
    return None
"""
def local_streampack(namepath, qualpath, funcpath, *arg):
    if arg == None:
        raise TypeError('EmptyPackageError')
    name, func, quals = arg
    print(name, file=namepath)
    print(quals, file=qualpath)
    print(func, file=funcpath)
    return None    

def local_Core(cidop, cidend, specs=None):
    if specs != None and 'functionalise' not in specs:
        raise NameError('Not_Implemented_Yet_Im_Sorry')
    error = 0
    namepath = 'localdata\\names.txt'
    funcpath = 'localdata\\rawfuncs.txt'
    qualpath = 'localdata\\quals.txt'
    currentname = open(namepath, 'a')
    currentfunc = open(funcpath, 'a')
    currentqual = open(qualpath, 'a')    
    while cidop<cidend:
        arg = local_retr(cidop)
        if 'Error' in arg:
            error +=1
        else:
            name, func, quals = arg.split('^^')
            local_streampack(currentname, currentqual, currentfunc, name, func, quals)
        cidop+=1
    currentname.close()
    currentfunc.close()
    currentqual.close()
    return error
    
if __name__ == '__main__':
    from pubchemprops import get_first_layer_props
    from pubchemprops import get_second_layer_props
    import pubchempy as pcp
    cidstart, cidend = map(int,input().split())
    print('Run with', local_Core(cidstart, cidend), 'errors')