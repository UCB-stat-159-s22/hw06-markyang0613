import numpy as np
from scipy import signal
from scipy.interpolate import interp1d
from scipy.signal import butter, filtfilt, iirdesign, zpk2tf, freqz
import h5py
import json

%matplotlib inline
%config InlineBackend.figure_format = 'retina'
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

from ligotools import readligo as rl

import numpy as np
import os
import fnmatch

def test_loaddata():
    strain, time, dq = rl.loaddata('ligo_data/H-H1_LOSC_4_V1-842653696-4096.hdf5', 'H1')
    # if (strain == True & time == True & dq == True):
    #     assert "Test_loaddata passed"
    #     print("Test 0 Passed")
        
def test_getseg():
    # segList = getsegs(842657792, 842658792, 'H1')
    # for (start, stop) in segList:
    #     strain, meta, dq = getstrain(start, stop, 'H1')
    #     if (strain == False 
        

