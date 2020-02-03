def manage_basic_parse(line, mode, func_dictrev, wildcard_dictrev, func_dict, wildcard_dict):
    Arr = line.split('\t')
    keyn = list(func_dictrev.keys())
    keya = list(wildcard_dictrev.keys())
    ind = len(keyn)
    data = [0]*(ind+len(keya)+2)
    if mode == 'retr':
        if 'SMILES' in Arr:
            data = Arr.index('SMILES')
            return data
        else:
            if 'Main Length' in Arr:
                return 'TableParsedError'
            else:
                return 'IncorrectFormError'
    else:
        smiles = Arr[mode]
        data[0] = prep_length(smiles)
        smiles, cycles = prep_group(smiles)
        data[1] = len(cycles)
        funcs = ident_group(smiles, func_dict, wildcard_dict)  #CCC1(C(=O)NC(=O)NC1=O)CCC(C)C
        for el in funcs:
            op = el[1]
            if 'Unidentified' in op:
                op = op.split('-')[0]
                data[keya.index(op)+ind+2] += 1
            else:
                data[keyn.index(op)+2] += 1
        for i in range(0, len(data)):
            data[i] = str(data[i])
        props = '\t'.join(data)
        return props

def manage_pack(data, line, filename, func_dictrev, wildcard_dictrev, typ):
    if typ == 'header':
        line += '\t'
        line += 'Length'
        line += '\t'
        line += 'Cycle_Count'
        for nam in func_dictrev.keys():
            line += '\t'
            line += nam
        for nam in wildcard_dictrev.keys():
            line += '\t'
            line += nam
    else:
        line = '\t'.join([line, data])
    print(line, file=filename)
    return None

def manage_Core(specs):
    database = 'localdata\\'
    resultpath = 'parsed_table.txt'
    printer = False
    if '>parse-' not in specs:
        raise NameError('File not specified!')
    else:
        filename = (specs.split('>parse-')[1]).split('<')[0] + '.txt'
    if '>changebaseto-' in specs:
        database = (specs.split('>changebaseto-')[1].split('<')[0])+'\\'
    if '>console' in specs:
        printer = True
    current = open(database+filename, 'r')
    result = open(database+resultpath, 'a')
    source = list(map(lambda el: el.rstrip('\n').rstrip('\r'), current.readlines()))
    lng = len(source)
    if printer:
        print('Working with', lng-1,'lines')
    manage_pack('None', source[0], result, func_dictrev, wildcard_dictrev, 'header')
    loc = manage_basic_parse(source.pop(0), 'retr', func_dictrev, wildcard_dictrev, func_dict, wildcard_dict)
    for i in range(lng):
        el = source[i]
        data = manage_basic_parse(el, loc, func_dictrev, wildcard_dictrev, func_dict, wildcard_dict)
        if 'Error' in data:
            if printer:
                print('Error at', i)
            else:
                pass
        else:
            manage_pack(data, el, result, func_dictrev, wildcard_dictrev, 'data')
        if printer:
            print('Parsed', i, 'out of', lng, 'entries:', el.split('\t')[0])
    current.close()
    result.close()
    return None
        
    
if __name__ == '__main__':
    from dict_func import *
    from dicts_forfunc import *
    manage_Core(input())