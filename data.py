import numpy as np
import pandas as pd
import root_numpy as rnp

def Pandafy(fileName, tree):
    df = pd.DataFrame(rnp.root2array(fileName,tree))
    return df