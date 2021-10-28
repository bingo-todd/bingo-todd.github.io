import matplotlib.pyplot as plt
import numpy as np
import os
import sys
sys.path.append('E:/github/Gammatone-filters/')
from gtf import gtf

fig_dir = '../assets/images/gtf_baseband_implementation/'
if not os.path.exists(fig_dir):
    os.makedirs(fig_dir)

def savefig(fig,fig_name):
    fig_fpath = os.path.join(fig_dir,fig_name)
    fig.savefig(fig_fpath)

def main():
    fs = 16e3
    gtf_filter = gtf(fs=fs,cf_low=50,cf_high=5e3,n_band=16)

    # spectrum of one gtf
    fig = gtf_filter.plot_filter_spectrum()
    savefig(fig,'filter_spectrum.png')

    # delay and gain at cfs
    fig = gtf_filter.plot_delay_gain_cfs()
    savefig(fig,'delay_gain_cfs.png')

    # no gain normalized
    irs = gtf_filter.get_ir(is_gain_norm=False)
    fig = gtf_filter.plot_ir_spec(irs)
    savefig(fig,'irs.png')
    # gain normalized
    irs_norm = gtf_filter.get_ir(is_gain_norm=True)
    fig = gtf_filter.plot_ir_spec(irs_norm)
    savefig(fig,'irs_norm.png')

if __name__ == '__main__':
    main()
