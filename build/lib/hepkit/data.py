import ROOT
import numpy as np
import pandas as pd
import root_numpy as rnp

def Pandafy(fileName, tree):
    df = pd.DataFrame(rnp.root2array(fileName,tree))
    return df

def RootLs(fileName):
    tFile = ROOT.TFile(fileName)
    for key in tFile.GetListOfKeys():
        print "%s \"%s\"" %(key.GetClassName(), key.GetName())
        if "TDirectory" in key.GetClassName():
            first = tFile.Get(key.GetName())
            for subKey in first.GetListOfKeys():
                print "|_%s \"%s\"" %(subKey.GetClassName(), subKey.GetName())
                if "TDirectory" in subKey.GetClassName():
                    second = tFile.Get(subKey.GetName())
                    for subSubKey in second.GetListOfKeys():
                        print "| |_%s \"%s\"" %(subSubKey.GetClassName(), subSubKey.GetName())

