import pubchempy as pcp
comp_1 = pcp.Compound.from_cid(int(input()))
print(comp_1.canonical_smiles)