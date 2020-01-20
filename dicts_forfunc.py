func_dict = {
    'C(=O)N':'Amide',
    'C(=O)F':'Acyl_Halide-F',
    'C(=O)Cl':'Acyl_Halide-Cl',
    'C(=O)Br':'Acyl_Halide-Br',
    'C(=O)I':'Acyl_Halide-I',
    
    'C(=O)OC':'Ester',
    'C(=O)O':'Acid-C',
    'C(=O)':'Ketone',
    
    'C(O)':'Base-C',
    'C=O':'Aldehyde',
    
    'COC':'Ether',
    'CO':'Base-C',
    
    'C#N':'Nitrile',
    'C=N':'Imine',
    'C[N+](=O)[O-]':'Nitro',
    
    
    'CN()C':'Amine-T',
    'CNC':'Amine-S',
    'CN':'Amine-P',
    
    'C=C=C':'Allene',
    'C#C':'Alkine',
    'C=C':'Alkene',
    
    'CCl':'Org-Chloride',
    'C[F]':'Org-Fluoride',
    'CBr':'Org-Bromide',
    'C[I]':'Org-Iodide'
    }

wildcard_dict = {
    '(=O)O':'Acid-',
    '(=O)':'Oxyl-',
    '=O':'Oxyl-',
    '(O)':'Base-',
    'O':'Base-'    
    }