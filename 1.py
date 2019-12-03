import pubchempy as pcp
import requests
import json
import re

def FindSection(l,nameofsec):
    for el in l:
      if el['TOCHeading']==nameofsec:
          return el

def GetInf(l):
    R=None
    try:
        R=l['Information'][0]['Value']['StringWithMarkup'][0]['String']
        X=re.search(r'(\d+(\.\d+)?)\s*°?([KFC])\b',R).groups()
       # print('qq3')
       # print(X)
        if X[2]=='C':
            R=float(X[0])
           # print('qq')
        elif X[2]=='F':
           # print(X[0],'xo')
            R=float(X[0])*100




    except:
        #print('Err:', l)
        pass
    print(R)
    return R



for i in range(1,15):

    response = requests.get('https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/'+str(i)+'/JSON/')
    obj = json.loads(response.text)

 #   print(obj)
    e=obj['Record']['Section']

    e2=FindSection(e,'Chemical and Physical Properties')
    try:
        e3=e2['Section']
    except:
     #break
     print('no')
     continue

    e4=FindSection(e3,'Experimental Properties')
    try:
      e5=e4['Section']
    except:
     #break
     print('no')
     continue



    #print(e5)
    Melt=FindSection(e5,'Melting Point')
    Boil=FindSection(e5,'Boiling Point')
    Solu=FindSection(e5,'Solubility')
    Inf={'Melt':GetInf(Melt),'Boil':GetInf(Boil)}
    print(Inf)

#,'Solu':GetInf(Solu)









#print(obj['Record']['Section'][3]['Section'][1]['Section'][4]['Information'][4])#[4]['Value']['StringWithMarkup'][0]['String'])

#https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/2244/JSON/
