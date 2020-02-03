# ToDo: use OrderedDict
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

func_dictrev = {
    'Amide':'C(=O)N',
    'Acyl_Halide-F':'C(=O)F',
    'Acyl_Halide-Cl':'C(=O)Cl',
    'Acyl_Halide-Br':'C(=O)Br',
    'Acyl_Halide-I':'C(=O)I',
    
    'Ester':'C(=O)OC',
    'Acid-C':'C(=O)O',
    'Ketone':'C(=O)',
    
    'Base-C':'C(O)',
    'Aldehyde':'C=O',
    
    'Ether':'COC',
    'Base-C':'CO',
    
    'Nitrile':'C#N',
    'Imine':'C=N',
    'Nitro':'C[N+](=O)[O-]',
    
    
    'Amine-T':'CN()C',
    'Amine-S':'CNC',
    'Amine-P':'CN',
    
    'Allene':'C=C=C',
    'Alkine':'C#C',
    'Alkene':'C=C',
    
    'Org-Chloride':'CCl',
    'Org-Fluoride':'C[F]',
    'Org-Bromide':'CBr',
    'Org-Iodide':'C[I]'
}

wildcard_dict = {
    '(=O)O':'Unidentified Acid',
    '(=O)':'Unidentified Oxyl',
    '=O':'Unidentified Oxyl',
    '(O)':'Unidentified Base',
    'O':'Unidentified Base'        
    }

wildcard_dictrev = {
    'Unidentified Acid':'(=O)O',
    'Unidentified Oxyl':'(=O)',
    'Unidentified Oxyl':'=O',
    'Unidentified Base':'(O)',
    'Unidentified Base':'O'
}