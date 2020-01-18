def parse_temperature(arg):
    decomp = False
    dgr = chr(176)
    templist = []
    for el in arg:
            op = el['Value']
            if 'StringWithMarkup' in op.keys():
                op = op['StringWithMarkup'][0]['String']
                if 'ecomposes' in op:
                    decomp = True
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
                    templist.append(op)
            elif 'Number' in op.keys():
                if 'C' in op['Unit']:
                    templist.append(float(op['Number'][0]))
                elif 'F' in op['Unit']:
                    templist.append((float(op['Number'][0])-32)*5/9)
                else:
                    try:
                        templist.append(float(op['Number'][0]))
                    except:
                        pass
    if templist != []:
        templist = str(sum(templist)/len(templist))
        if decomp:
            templist += ' and decomposes'
        return templist
    else:
        return 'MissingInfo'