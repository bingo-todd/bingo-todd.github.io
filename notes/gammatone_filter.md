## ERB计算
基底膜上每一个点都对应一个特征频率cf，以及带宽（通常使用等效矩形带宽ERB(f)表示）。
Glasberg和Moore给出的 $ERB(f)$ 计算公式如下
$$
\begin{equation}
\begin{aligned}
ERB(cf)=24.7(4.37\frac{cf}{1000}+1)
\end{aligned}
\end{equation}
$$

Slaney[^Slaney1993]则综合Glasberg and Moore, Lyon以及Greenwood的工作，给出通用表达式
$$
\begin{equation}
\begin{aligned}
ERB(cf)=\left(\left(\frac{f}{Q_{Ear}}\right)^{order}+BW_{min}^{order}\right)^{\frac{1}{order}}
\end{aligned}
\end{equation}
$$
> - $Q_{Ear}$: the asymptotic(渐进的) filter quality at large frequencies（中心频率较大时，可近似为滤波器的品质因数Q）
> - BW_{min}: the minimum bandwidth for low frequency channels

## 滤波器组的cf
假设给定滤波器组**中心频率**所需覆盖的频率范围，$cf_{low}~cf_{high}$，如何确定每个滤波器的cf？
- 给定前后滤波器带宽的关系Stepfactor

  Stepfactor为相邻滤波器通带not overlap的比例
  $$
  \begin{equation}
  \begin{aligned}
  Stepfactor=\begin{cases}
  0 \quad  &\text{前一滤波器的通带完全被后一滤波器的通带所覆盖}\\
  (0,1) \quad &\text{部分重叠}\\
  1 \quad &\text{刚好不重叠}\\
  (1,+\infty) \quad &\text{存在频率间隙}
  \end{cases}
  \end{aligned}
  \end{equation}
  $$

  滤波器的个数N可直接计算得到（order=1）：
  $$
  \begin{equation}
  \begin{aligned}
  N &= \int_{cf_{low}}^{cf_{high}}{\frac{1}{Stepfactor\times ERB(f)}df}\\
  &= \left.\frac{1}{Stepfactor}\log{ERB(f)}\frac{1}{(\partial ERB(f))/(\partial f)} \right|_{cf_{low}}^{f_{high}}\\
  &= \left.\frac{\log(\frac{f}{Q_{Ear}}+BW_{min})Q_{Ear}}{Stepfactor}\right|_{f_{low}}^{f_{high}}\\
  &= \left.\frac{\log(f+Q_{Ear} BW_{min})Q_{Ear}-Q_{Ear} \log{Q_{Ear}}}{Stepfactor}\right|_{cf_{low}}^{cf_{high}}\\
  &=\frac{Q_{Ear}}{Stepfactor}\log{\left(\frac{cf_{high}+Q_{Ear} BW_{min}}{cf_{low}+Q_{Ear} BW_{min}}\right)}
  \end{aligned}
  \end{equation}
  $$
  因此共需要 $\lceil{N}\rceil$ 个滤波器。$n_{th}$ 滤波器中心频率为
  $$
  \begin{equation}
  \begin{aligned}
  cf_{high} = (cf_{low}+Q_{Ear} BW_{min})e^{\frac{n_{th}Stepfactor}{Q_{Ear}}}-Q_{Ear} BW_{min}
  \end{aligned}
  \end{equation}
  $$
  cfArray = -(EarQ*minBW) + exp((1:N)'*(-log(highFreq + EarQ*minBW) + ...
		log(lowFreq + EarQ*minBW))/N) * (highFreq + EarQ*minBW);

- 给定滤波器个数N

  根据N与Stepfactor间的函数关系，有
  $$
  \begin{equation}
  \begin{aligned}
  Stepfactor = \frac{Q_{Ear}\log{\left(\frac{cf_{high}+Q_{Ear} BW_{min}}{cf_{low}+Q_{Ear} BW_{min}}\right)}}{N}
  \end{aligned}
  \end{equation}
  $$
  同样的方法，也可以计算每个滤波器的中心频率。

[^Slaney1993]: M. Slaney and others, “An efficient implementation of the Patterson-Holdsworth auditory filter bank,” Apple Computer, Perception Group, Tech. Rep, vol. 35, no. 8, 1993.
