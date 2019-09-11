gammatone滤波器的冲激响应

$$
\begin{equation}
\begin{aligned}
g(t) = \frac{at^{n-1}\cos(2\pi f_ct+\phi)}{e^{2\pi b t}} \label{gtf_ir}
\end{aligned}
\end{equation}
$$

冲激响应示意图如下
![gtf_ir](images/2019/08/gtf-ir.png)

不同频带冲激响应的峰值位置有差异。相位补偿则是将其对其。

令 $g_amp(t)= \frac{t^{n-1}}{e^{2\pi b t}}$
$$
\begin{equation}
\begin{aligned}
\frac{\partial g_{amp}(t)}{\partial t} &= \frac{(n-1)t^{n-2}}{e^{2\pi bt}}-\frac{t^{n-1}2\pi b}{e^{2\pi bt}}\\
&=\frac{t^{n-2}}{e^{2\pi bt}}(n-1-2\pi bt)\\
&\triangleq 0
\end{aligned}
\end{equation}
$$
所以
$$
\begin{equation}
\begin{aligned}
\tau=\frac{(n-1)}{2\pi b}
\end{aligned}
\end{equation}
$$

对\eqref{gtf_ir}进行延时补偿，可以得到
$$
\begin{equation}
\begin{aligned}
g_{phase\_com}(t) = g_{amp}(t-\tau)\cos(2\pi f_ct+\phi)=
\end{aligned}
\end{equation}
$$

时域延时==频域乘以
$$
\begin{equation}
\begin{aligned}
F'(f)=\int{f(t-\tau)e^{-j2\pi ft}dt}=\int{f(t-\tau)e^{-j2\pi f(t-\tau)}e^{-j2\pi f\tau}dt}=F(f)e^{-j2\pi f\tau}
\end{aligned}
\end{equation}
$$



使用冲击响应不变法，对 $r(t)$ 进行采样，采样间隔为T，即：
$$
\begin{equation}
\begin{aligned}
r_d(i) = r(iT)= (iT)^{n-1}e^{-2\pi bTi}=T^{n-1}i^{n-1}e^{-2\pi bTi}\label{eq1}
\end{aligned}
\end{equation}
$$
令 $k=e^{-2\pi bT}$ ，上式就可以简化为
$$
\begin{equation}
\begin{aligned}
r_d(i)=T^{n-1}i^{n-1}k^{i}
\end{aligned}
\end{equation}
$$

因为
$$
\begin{equation}
\begin{aligned}
Z(if(i))&=\sum{if(i)z^{-i}}=-z\frac{\partial\sum{f(i)z^{-i}}}{\partial z}=z^{-1}\frac{\partial\sum{f(i)(z^{-1})^i}}{\partial z^{-1}}\\
\end{aligned}
\end{equation}
$$

$$
\begin{equation}
\begin{aligned}
Z(k^{-i})&=\frac{1}{1-kz^{-1}}
\end{aligned}
\end{equation}
$$
所以
$$
\begin{equation}
\begin{aligned}
Z(ik^i)&=z^{-1}\frac{\partial Z(k^{i})}{\partial z^{-1}}=z^{-1}\frac{\partial \frac{1}{1-kz^{-1}}}{\partial z^{-1}}=\frac{kz^{-1}}{(1-kz^{-1})^2}\\

Z(i^2k^i)&=z^{-1}\frac{\partial Z(iz^{i})}{\partial z^{-1}}=z^{-1}\frac{\frac{kz^{-1}}{(1-kz^{-1})^2}}{\partial z^{-1}}=z^{-1}\left[\frac{k}{(1-kz^{-1})^2}+\frac{2k^2z^{-1}}{(1-kz^{-1})^3}\right]\\

Z(i^3k^i)&=z^{-1}\frac{\partial Z(i^2k^{i})}{\partial z^{-1}}=z^{-1}\frac{z^{-1}\left[\frac{k}{(1-kz^{-1})^2}+\frac{2k^2z^{-1}}{(1-kz^{-1})^3}\right]}{\partial z^{-1}}\\
&=z^{-1}\left[\frac{k}{(1-kz^{-1})^2}+\frac{2k^2z^{-1}}{(1-kz^{-1})^3}\right]+z^{-2}\left[\frac{2k^2}{(1-kz^{-1})^3}+\frac{2k^2}{(1-kz)^3}+\frac{6k^3z^{-1}}{(1-kz^{-1})^4}\right]\\
&=\frac{z^{-1}k(1-kz^{-1})^2+2k^2z^{-2}(1-kz^{-1})+4k^2z^{-2}(1-kz^{-1})+6k^3z^3}{(1-kz^{-1})^4}\\
&=\frac{kz^{-1}+k^3z^{-3}-2k^2z^{-2}+2k^2z^{-2}-2k^3z^{-3}+4k^2z^{-2}-4k^3z^{-3}+6k^3z^{-3}}{(1-kz^{-1})^4}\\
&=\frac{k^3z^{-3}+4k^2z^{-2}+kz^{-1}}{(1-kz^{-1})^4}\\
&=\frac{kz^{-1}(1+4kz^{-1}+k^2z^{-2})}{(1-2kz^{-1}+k^2z^{-2})^2}\\
&=\frac{kz^{-1}(1+4kz^{-1}+k^2z^{-2})}{1-4kz^{-1}+2k^2z^{-2}+4k^2z^{-2}-4k^3z^{-3}+k^4z^{-4}}\\
&=\frac{kz^{-1}(1+4kz^{-1}+k^2z^{-2})}{1-4kz^{-1}+6k^2z^{-2}-4k^3z^{-3}+k^4z^{-4}}\\
\end{aligned}
\end{equation}
$$
最终得到Gammatone滤波器的公式
$$
\begin{equation}
\begin{aligned}
y(n)=&\underbrace{kx(n-1)+4k^2x(n-2)+k^3x(n-3)}_\text{x part}+\\
&\underbrace{(4ky(n-1)-6k^2y(n-2)+4k^3y(n-3)-k^4y(n-4))}_\text{y part}
\end{aligned}
\end{equation}
$$
