def local_retr(cid):
    op = get_first_layer_props(cid, ['CanonicalSMILES', 'IUPACName'])
    smiles = op['CanonicalSMILES']
    name = op['IUPACName']
    qual = get_second_layer_props(cid, ['Melting Point', 'Boiling Point'])
    dgr = chr(176)
    decboil = False
    decmelt = False
    if 'Boiling Point' in qual.keys():
        boiltemp = []
        for el in qual['Boiling Point']:
            op = el['Value']
            if 'StringWithMarkup' in op.keys():
                op = op['StringWithMarkup'][0]['String']
                if 'ecomposes' in op:
                    decboil = True
                    if op == 'Decomposes':
                        op = 'Pass'
                if dgr in op:
                    op = op.split(dgr)
                    un = op[1][0]
                    op = op[0]
                    op = op.strip(' ')
                    op = op.split(':')[-1]
                    op = ''.join(op.split('>'))
                    op = ''.join(op.split('<'))
                    if ' to ' in op:
                        op = op.split(' to ')
                        op1, op2 = min(float(op[0]), float(op[1])), max(float(op[0]), float(op[1]))
                        if op1<0 and op2>0:
                            if abs(op1)<abs(op2):
                                op1 = abs(op1)
                            elif abs(op1)>abs(op2):
                                op2 = 0-op2
                        op = (op1+op2)/2
                    elif ' - ' in op or '-' in op:
                        if ' - ' in op:
                            op = op.split(' - ')
                        elif op[0] != '-':
                            op = op.split('-')
                        op1, op2 = min(float(op[0]), float(op[1])), max(float(op[0]), float(op[1]))
                        if op1<0 and op2>0:
                            if abs(op1)<abs(op2):
                                op1 = abs(op1)
                            elif abs(op1)>abs(op2):
                                op2 = 0-op2
                        op = (op1+op2)/2
                    else:
                        op = float(op)
                    if un == 'F':
                        op = (op-32)*5/9
                else:
                    if ' to ' in op:
                        op = op.split(' to ')
                        op1, op2 = min(float(op[0]), float(op[1])), max(float(op[0]), float(op[1]))
                        if op1<0 and op2>0:
                            if abs(op1)<abs(op2):
                                op1 = abs(op1)
                            elif abs(op1)>abs(op2):
                                op2 = 0-op2
                        op = (op1+op2)/2
                    elif ' - ' in op:
                        op = op.split(' - ')
                        op1, op2 = min(float(op[0]), float(op[1])), max(float(op[0]), float(op[1]))
                        if op1<0 and op2>0:
                            if abs(op1)<abs(op2):
                                op1 = abs(op1)
                            elif abs(op1)>abs(op2):
                                op2 = 0-op2
                        op = (op1+op2)/2
                    elif op != 'Pass':
                        op = float(op)
                if op != 'Pass':
                    boiltemp.append(op)
            elif 'Number' in op.keys():
                if 'C' in op['Unit']:
                    boiltemp.append(float(op['Number'][0]))
                elif 'F' in op['Unit']:
                    boiltemp.append((float(op['Number'][0])-32)*5/9)
                else:
                    try:
                        boiltemp.append(float(op['Number'][0]))
                    except:
                        pass
        if boiltemp != []:
            boiltemp = str(sum(boiltemp)/len(boiltemp))
            if decboil:
                boiltemp += ' and decomposes'
        else:
            return 'MissingInfo'
    else:
        return 'MissingInfo'
    if 'Melting Point' in qual.keys():
        melttemp = []
        for el in qual['Melting Point']:
            op = el['Value']
            if 'StringWithMarkup' in op.keys():
                op = op['StringWithMarkup'][0]['String']
                if 'ecomposes' in op:
                    decmelt = True
                    if op == 'Decomposes':
                        op = 'Pass'
                if dgr in op:
                    op = op.split(dgr)
                    un = op[1][0]
                    op = op[0]
                    op = op.strip(' ')
                    op = op.split(':')[-1]
                    op = ''.join(op.split('>'))
                    op = ''.join(op.split('<'))                    
                    if ' to ' in op:
                        op = op.split(' to ')
                        op1, op2 = min(float(op[0]), float(op[1])), max(float(op[0]), float(op[1]))
                        if op1<0 and op2>0:
                            if abs(op1)<abs(op2):
                                op1 = abs(op1)
                            elif abs(op1)>abs(op2):
                                op2 = 0-op2
                        op = (op1+op2)/2
                    elif ' - ' in op or '-' in op:
                        if ' - ' in op:
                            op = op.split(' - ')
                        elif op[0] != '-':
                            op = op.split('-')
                        op1, op2 = min(float(op[0]), float(op[1])), max(float(op[0]), float(op[1]))
                        if op1<0 and op2>0:
                            if abs(op1)<abs(op2):
                                op1 = abs(op1)
                            elif abs(op1)>abs(op2):
                                op2 = 0-op2
                        op = (op1+op2)/2
                    else:
                        op = float(op)
                    if un == 'F':
                        op = (op-32)*5/9
                else:
                    if ' to ' in op:
                        op = op.split(' to ')
                        op1, op2 = min(float(op[0]), float(op[1])), max(float(op[0]), float(op[1]))
                        if op1<0 and op2>0:
                            if abs(op1)<abs(op2):
                                op1 = abs(op1)
                            elif abs(op1)>abs(op2):
                                op2 = 0-op2
                        op = (op1+op2)/2
                    elif ' - ' in op:
                        op = op.split(' - ')
                        op1, op2 = min(float(op[0]), float(op[1])), max(float(op[0]), float(op[1]))
                        if op1<0 and op2>0:
                            if abs(op1)<abs(op2):
                                op1 = abs(op1)
                            elif abs(op1)>abs(op2):
                                op2 = 0-op2
                        op = (op1+op2)/2
                    elif op != 'Pass':
                        op = float(op)
                if op != 'Pass':
                    melttemp.append(op)
            elif 'Number' in op.keys():
                if 'C' in op['Unit']:
                    melttemp.append(float(op['Number'][0]))
                elif 'F' in op['Unit']:
                    melttemp.append((float(op['Number'][0])-32)*5/9)
                else:
                    try:
                        melttemp.append(float(op['Number'][0]))
                    except:
                        pass
        if melttemp != []:
            melttemp = str(sum(melttemp)/len(melttemp))
            if decmelt:
                melttemp += ' and decomposes'
        else:
            return 'MissingInfo'
    else:
        return 'MissingInfo'
    qual = 'Melting Point = '+melttemp+'; '+'Boiling Point = '+boiltemp
    return [name, smiles, qual]
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
def local_streampack(filepath, *arg):
    if arg == None:
        raise TypeError('EmptyPackageError')
    print(arg, file=filepath)
    return None    

def local_Core(cidop, cidend, specs=None):
    database = 'localdata\\'
    datapath = database+'datasheet.txt'
    prntr = False
    datalisting = True
    keeplog = False
    onlycrash = False
    if specs != None:
        if '>changebaseto-' in specs:
            database = (specs.split('>changebaseto-')[1].split('<')[0])+'\\'
        if '>console' in specs:
            prntr = True
        if '>nodata' in specs:
            datalisting = False
        if '>keeplogat-' in specs:
            logpath = database+(specs.split('>keeplogat-')[1].split('<')[0])+'.txt'
            logger = open(logpath, 'a')
            keeplog = True
        if '>writedatato-' in specs:
            datapath = database+(specs.split('>writedatato-')[1].split('<')[0])+'.txt'
        if '>onlycrashnotes' in specs:
            onlycrash = True
    minor = 0
    major = 0
    stat = cidend-cidop
    if datalisting:
        current = open(datapath, 'a')
    if keeplog:
        print('Current run: '+str(cidop)+' to '+str(cidend), file=logger)
        print('Specifications: '+specs, file=logger)
    while cidop<cidend:
        try:
            arg = local_retr(cidop)
            if 'Error' in arg:
                minor +=1
            else:
                arg = '	'.join(arg)
                if datalisting:
                    local_streampack(current, arg)
                if datalisting:
                    arg = 'Packed'
                else:
                    arg = 'Packaging denied specifically'
        except:
            major +=1
            arg = 'FUNCTION ERROR'
        if prntr and not onlycrash:
            print(cidop, 'as follows:')
            print(arg)
            print('')
        elif prntr and onlycrash:
            if arg == 'FUNCTION ERROR':
                print('Crash at CID', cidop)
        if keeplog and not onlycrash:
            print(str(cidop)+' as follows:', file=logger)
            print(arg, file=logger)
            print('', file=logger)
        elif keeplog and onlycrash:
            if arg == 'FUNCTION ERROR':
                print('Crashed at CID'+str(cidop), file=logger)
        cidop+=1
    if datalisting:
        current.close()
    if prntr:
        print('Encountered lack of info', minor, 'times')
        print('Encountered major problems', major, 'times')
        print('per', stat, 'runs')
    if keeplog:
        print('Encountered lack of info '+str(minor)+' times', file=logger)
        print('Encountered major problems '+str(major)+' times', file=logger)
        print('per '+str(stat)+' runs', file=logger)
        logger.close()
    return None
    
if __name__ == '__main__':
    from pubchemprops import get_first_layer_props
    from pubchemprops import get_second_layer_props
    import pubchempy as pcp
    print('CIDs to start and end with')
    cidstart, cidend = map(int,input().split())
    print('Specifications or none if none are needed')
    specs = input()
    local_Core(cidstart, cidend, specs)
    stopper = input()