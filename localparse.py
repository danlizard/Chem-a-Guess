def parse_SMILES(arg):
    return arg['Value']['StringWithMarkup'][0]['String']

def parse_IUPAC(arg):
    return arg['Value']['StringWithMarkup'][0]['String']

def parse_temp(arg):
    num = '1234567890-.'
    decomp = False
    dgr = chr(176)
    templist = []
    for el in arg:
        good = True
        op = el['Value']
        if 'Number' in op.keys():
            if 'C' in op['Unit']:
                templist.append(float(op['Number'][0]))
            elif 'F' in op['Unit']:
                templist.append((float(op['Number'][0])-32)*5/9)
            else:
                try:
                    templist.append(float(op['Number'][0]))
                except:
                    pass         
        elif 'StringWithMarkup' in op.keys():
            op = op['StringWithMarkup'][0]['String']
            if 'ecomposes' in op:
                decomp = True
            if dgr in op:
                op, un = op.split(dgr)
                if un[0] == 'F':
                    good = False
            val = False
            for sym in op:
                if sym in num:
                    if val:
                        templist[-1]+=sym
                    else:
                        templist.append(sym)
                        val = True
                elif val:
                    if '-' in templist[-1]:
                        if (templist[-1].split('-')[0]).strip(' ') != '':
                            f,s = templist[-1].split('-')
                            if f == '':
                                templist[-1] = '-' + s.strip(' ')
                            else:
                                templist[-1] = float(f)
                                templist.append(s)
                    templist[-1] = float(templist[-1])
                    if not good:
                        templist[-1] = (templist[-1]-32)*5/9
                    val = False
            if val:
                if '-' in templist[-1]:
                        if (templist[-1].split('-')[0]).strip(' ') != '':
                            f,s = templist[-1].split('-')
                            if f == '':
                                templist[-1] = '-' + s.strip(' ')
                            else:
                                templist[-1] = float(f)
                                templist.append(s)
                templist[-1] = float(templist[-1])
                if not good:
                    templist[-1] = (templist[-1]-32)*5/9
                val = False
    if templist == []:
        temp = 'NaN'
    else:
        temp = str(sum(templist)/len(templist))
        if decomp:
            temp+=' and decomposes'
    return temp