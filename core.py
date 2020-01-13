from dicts_forfunc import *
import pubchempy as pcp
import pubchemprops as cheminf
import dict_func as func
## import plot_func as func
import GetPhysProps as qual


def base(cid):
    quals = qual.(cid)
    #smiles = ...
    """
    comp, cn = func.plotc(smiles)
    bondlist, cyclist = func.basic_funct(comp, cn)
    """