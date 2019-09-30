---
layout: post
title:  "Gammatone filter implementation"
categories: Work
tags: dsp
author: Todd
description: Gammatone filter implementation
---

冲击响应不变法设计IIR滤波器

对于模拟滤波器的冲击响应 $h(t)$，以时间间隔T对其进行采样，得到对应的数字滤波器，即

$$
\begin{equation}
\begin{aligned}
y=\frac{\sin(x)}{x}
\end{aligned}
\end{equation}
$$
