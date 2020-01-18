def local_retr(cid):
    op = get_first_layer_props(cid, ['CanonicalSMILES', 'IUPACName'])
    smiles = op['CanonicalSMILES']
    name = op['IUPACName']
    qual = get_second_layer_props(cid, ['Melting Point', 'Boiling Point'])
    if 'Boiling Point' in qual.keys():
        boiltemp = str(parse_temperature(qual['Boiling Point']))
    else:
        return 'MissingInfo'
    if 'Melting Point' in qual.keys():
        melttemp = str(parse_temperature(qual['Boiling Point']))
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
    errorlist = ['MissingInfo']
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
            if arg in errorlist:
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
    from localparse import *
    import pubchempy as pcp
    print('CIDs to start and end with')
    cidstart, cidend = map(int,input().split())
    print('Specifications or none if none are needed')
    specs = input()
    local_Core(cidstart, cidend, specs)
    stopper = input()