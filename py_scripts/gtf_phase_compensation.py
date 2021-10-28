import matplotlib.pyplot as plt
import numpy as np
import sys
import os

fig_dir = "..\assets\images\gtf_phase_compensation"
if not os.path.exists(fig_dir):
    os.makedirs(fig_dir)

def savefig(fig,fig_name):
    fig_fpath = os.path.join(fig_dir,fig_name)
    fig.savefig(fig_fpath)

sys.path.append('E:\github\Gammatone-filters')
from gtf import gtf
fs = 16e3
gtf_filter = gtf(fs=fs,freq_low=80,freq_high=1e3,n_band=4)
# gtf_filter.cfs = np.flip(gtf_filter.cfs)

irs = gtf_filter.get_ir()
# print(irs.shape)
irs_env_aligned = gtf_filter.get_ir(is_env_aligned=True,
                                    delay_common=0)
irs_all_aligned = gtf_filter.get_ir(is_env_aligned=True,
                                    is_fine_aligned=True,
                                    delay_common=0)

ir_len = 1000
ir_times = np.arange(ir_len)/fs*1000
fig = plt.figure()
axes = fig.subplots(1,1)
axes.plot(ir_times,np.flipud(irs[:,:ir_len]).T,linewidth=3)
axes.set_xlabel('time(ms)')
axes.legend(['{:.0f} Hz'.format(cf) for cf in gtf_filter.cfs])
fig.savefig(os.path.join(fig_dir,'gtf_irs.png'))

fig = plt.figure()
axes = fig.subplots(1,1)
axes.plot(ir_times,np.flipud(irs_env_aligned[:,:ir_len]).T,linewidth=3)
axes.set_xlabel('time(ms)')
axes.legend(['{:.0f} Hz'.format(cf) for cf in gtf_filter.cfs])
fig.savefig(os.path.join(fig_dir,'gtf_irs_env_aligned.png'))

fig = plt.figure()
axes = fig.subplots(1,1)
axes.plot(ir_times,np.flipud(irs_all_aligned[:,:ir_len]).T,linewidth=3)
axes.set_xlabel('time(ms)')
axes.legend(['{:.0f} Hz'.format(cf) for cf in gtf_filter.cfs])
fig.savefig(os.path.join(fig_dir,'gtf_irs_all_aligned.png'))
