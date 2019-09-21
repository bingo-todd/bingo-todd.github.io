---
layout: post
title:  "Gammatone-filter"
categories: Work
tags: github
author: Todd
description: Gammatone filter
---

<!-- TOC -->

- [Gammatone-filters](#gammatone-filters)
  - [Basic ideas [^Holdsworth1988]](#basic-ideas-%5Eholdsworth1988)
  - [Usage](#usage)
  - [Buildin examples](#buildin-examples)
  - [About efficiency](#about-efficiency)

<!-- /TOC -->

# Gammatone-filters
Python implementation of Gammatone filter.

The filtering part of code is written in C.

## Basic ideas [^Holdsworth1988]
The impulse response of Gammatone filter is defined as follow

$$
g(t) = \frac{at^{n-1}\cos(2\pi f_ct+\phi)}{e^{2\pi b t}}
$$

in which

- $f_c$: center frequency
- $b$= : bandwidth,

$g(t)$ can be regarded as the mutliplication result of two parts,

$$
\begin{equation}
\begin{aligned}
g(t)&=a \times \underbrace{t^{n-1}e^{-2\pi bt}}_\text{r(t)} \times \underbrace{cos(2\pi f_c t+\phi)}_{s(t)}\\
\end{aligned}
\end{equation}
$$

Multiplication in time domain = convolution in frequency domain, so

$$
\begin{equation}
\begin{aligned}
R(f)=FT(t^{n-1}e^{-2\pi b t})
&=\frac{1}{(j2\pi)^{n-1}}\frac{\partial^{n-1} FT(e^{-2\pi bt})}{\partial f^{n-1}}\\
&=\frac{1}{(j2\pi)^{n-1}}\frac{\partial^{n-1}\frac{1}{2\pi b+j2\pi f}}{\partial f^{n-1}}\\
&=\frac{1}{(j2\pi)^{n-1}}\frac{(j)^{n-1}(n-1)!}{2\pi}\frac{1}{(b+jf)^n}\\
&=\frac{(n-1)!}{(2\pi b)^n}\frac{1}{(1+jf/b)^n} \label{eq:1}
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
S(f)=FT\left(cos(2\pi f_ct+\phi)\right)
&=e^{j\phi}\delta(f-f_c)+e^{-j\phi}\delta(f+f_c)
\end{aligned}
\end{equation}
$$

Combine equation (2) and (3), we can get $G(f)$

$$
\begin{equation}
\begin{aligned}
G(f)&=a \times R(f)*S(f)\\
&=a \times e^{j\phi}\frac{(n-1)!}{(2\pi b)^n}\frac{1}{(1+j(f-f_c)/b)^n}+ae^{-j\phi}\frac{(n-1)!}{(2\pi b)^n}\frac{1}{(1+j(f+f_c)/b)^n}\\
&=a\frac{(n-1)!}{(2\pi b)^n}\left[e^{j\phi}\left(\frac{1}{(1+j(f-f_c)/b)}\right)^n+e^{-j\phi}\left(\frac{1}{(1+j(f+f_c)/b)}\right)^n\right]
\end{aligned}
\end{equation}
$$

As shown in the following diagram,$G(f)$ consists of two symmetric parts. For simplicity, only positive frequency side is considered

<center><img src="/assets/images/Gammatone-filters/gtf-ir-spectrum.png" width="60%"></center>

Further more, Gammatone filter can be regarded as low-pass filter with frequency shitfted by fc. Now, equalently, we can first shift input signal by -fc and filter it with a lowpass filter, finally shift the frequency by fc.

<center><img src=/assets/images/Gammatone-filters/diagram.png ></center>
![diagram](/assets/images/Gammatone-filters/diagram.png)

 The detailed derivation is in [README.pdf](README.pdf)

## Usage

  ```Python
  from GTF import GTF
  gt_filter = GTF(fs=44100,low_cf=80,high_cf=5000,N_band=32)
  x_filtered = gt_filter.filter_c(x,is_aligned=0)# not aligned
  ```

## Buildin examples

  In termial
  ```shell
  python GTF.py example
  ```
  ```Python
  #definition of example func
  def example():
      fs = 16e3
      gt_filter = GTF(fs,freq_low=80,freq_high=5e3,N_band=16)

      # delays and gains
      fig = plt.figure()
      gt_filter.cal_delay_gain_cfs(is_plot=True,fig=fig)
      fig.savefig('/assets/images/Gammatone-filters/delay_gain.png')

      # impulse response direct from equation
      ir_equation = gt_filter.get_ir_equation()
      ir_equation = ir_equation/np.max(np.abs(ir_equation))

      # ir: filter impulse signal
      ir = gt_filter.get_ir(is_gain_norm=False,is_aligned=False)
      ir = ir/np.max(np.abs(ir))

      #
      ir_norm = gt_filter.get_ir(is_gain_norm=True,is_aligned=False)

      # ir phase compensated
      ir_norm_aligned = gt_filter.get_ir(is_gain_norm=True,is_aligned=True,delay_common=0)

      # plot ir
      if not os.path.exists('/assets/images/Gammatone-filters'):
          os.mkdir('/assets/images/Gammatone-filters')

      fig_ir_eq = gt_filter.plot_ir_spec(ir_equation)
      fig_ir_eq.savefig('/assets/images/Gammatone-filters/ir_equation.png')

      fig_ir = gt_filter.plot_ir_spec(ir)
      fig_ir.savefig('/assets/images/Gammatone-filters/ir.png')

      fig_norm = gt_filter.plot_ir_spec(ir_norm)
      fig_norm.savefig('/assets/images/Gammatone-filters/ir_norm.png')

      fig_ir_norm_aligned = gt_filter.plot_ir_spec(ir_norm_aligned)
      fig_ir_norm_aligned.savefig('/assets/images/Gammatone-filters/ir_norm_aligned.png')

      gt_filter.filter_spectrum()
  ```
- Spectrum of Gammatone filter

  Only filter with cf=4kHz is ploted

  <center><img src="/assets/images/Gammatone-filters/filter_spectrum.png"></center>

- Delays and gains at cfs

  <center><img src="/assets/images/Gammatone-filters/delay_gain.png"></center>

  Basically, the phase delay at center frequency approximates 0.

- Impulse response of Gammatone filters

  - Max-amplitude normalized

    <center><img src="/assets/images/Gammatone-filters/ir.png"></center>

  - Gain normalization

    <center><img src="/assets/images/Gammatone-filters/ir_norm.png"></center>

  - Phase compensation

    Phase compensation is actually to align impulse response peaks of all filter[^Brown1994].

    <center><img src="/assets/images/Gammatone-filters/ir_norm_aligned.png"></center>

    <!-- Next, I want to make summary about signal recovery after filtered by Gammatone filters.[Flag] -->

## About efficiency

  The key filter part is both written in c and python, and apparentlly, the c implementation is much fast

  Efficiency test
  ```shell
  $$ python GTF.py efficiency

   time consumed(s)
      c         :0.39
      python    :36.23
  ```



[^Holdsworth1988]: Holdsworth, John, Roy Patterson, and Ian Nimmo-Smith. Implementing a GammaTone Filter Bank

[^Brown1994]: G. J. Brown and M. P. Cooke (1994) Computational auditory scene analysis. Computer Speech and Language, 8, pp. 297-336
