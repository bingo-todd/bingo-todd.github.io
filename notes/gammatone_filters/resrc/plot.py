import sys
sys.path.append('/home/st/Work_Space/module_st/Gammatone-filters/')
from APGTF import APGTF
#

gtf =  APGTF(fs=16e3,freq_low=80,freq_high=5e3,N_band=30)
