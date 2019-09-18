# Gammatone 滤波器的实现
Gammatone滤波器冲击响应：

$$
\begin{equation}
\begin{aligned}
g(t) = \frac{at^{n-1}\cos(2\pi f_ct+\phi)}{e^{2\pi b t}}
\end{aligned}
\end{equation}
$$

其中:

- $f_c$：中心频率
- $b$ ：带宽，$1.019*ERB(f_c)$

## 历史由来

参考了Ma Ning的C语言实现，其doc中写到该算法是基于Cooke的工作。Lyon关于all pole gammatone filter的文档[^Lyon1996]总结了gammatone滤波器的历史，根据该文档，

- 1988年，Holdsworth利用frequency-shifting 滤波器，用all-pole IIR lowpass filter实现了Gammatone滤波器的近似
- 1991年，Darling对Holdsworth的方法进行简化
- 1991年，Cooke对Gammatone滤波器的各种近似实现进行对了详细的比较

## 实现方法

### IIR [^Darling]

符号未和参考文章统一

令 $B=2\pi b$，$\omega_c=2\pi f_c$，且暂不考虑$a,\phi$

则上式可以简化为
$$
\begin{equation}
\begin{aligned}
g(t)=\frac{t^{n-1}\cos(\omega_c t+)}{e^{B t}}={t^{n-1}}\frac{\cos(\omega_c t)}{e^{Bt}}
\end{aligned}
\end{equation}
$$

因为
$$
\begin{equation}
\begin{aligned}
\mathcal{L}\left(\frac{\cos(\omega_c t)}{e^{B t}}\right)=\frac{s+B}{(s+B)^2+\omega_c^2}
\end{aligned}
\end{equation}
$$
而
$$
\begin{equation}
\begin{aligned}
\mathcal{L}(t^nf(t))=\int{t^nf(t)e^{(-st)}dt}=(-1)^{n}\int{f(t)\frac{\partial e^{(-st)}}{\partial s}dt}=(-1)^{n}\frac{\partial^n F(s)}{\partial s^n}
\end{aligned}
\end{equation}
$$
因此
$$
\begin{equation}
\begin{aligned}
G(s)= (-1)^{n-1} \frac{\partial^{n-1} \mathcal{L}\left(\frac{cos(\omega_c t)}{e^{Bt}}\right)}{\partial s^{n-1}}=(-1)^{n-1} \frac{\partial^{n-1} \frac{s+B}{(s+B)^2+\omega_c^2}}{\partial s^{n-1}}
\end{aligned}
\end{equation}
$$
对于4阶Gammatone滤波器，n=4，只需要求3阶导数。逐次求导的结果如下：
- 一阶导数
  $$
  \begin{equation}
  \begin{aligned}
  \frac{\partial \frac{s+B}{(s+B)^2+\omega_c^2}}{\partial s}=\frac{1}{(s+B)^2+\omega_c^2}+(-2)\frac{(s+B)^2}{\left((s+B)^2+\omega_c^2\right)^2}
  \end{aligned}
  \end{equation}
  $$
- 二阶导数
  $$
  \begin{equation}
  \begin{aligned}
  \frac{\partial^2 \frac{s+B}{(s+B)^2+\omega_c^2}}{\partial s^2}=&(-2)\frac{(s+B)}{((s+B)^2+\omega_c^2)^2}+(-4)\frac{(s+B)}{((s+B)^2+\omega_c^2)^2}+\\&\quad 8\frac{(s+B)^2}{\left((s+B)^3+\omega_c^2\right)^3}\\
  =&(-6)\frac{(s+B)}{((s+B)^2+\omega_c^2)^2}+8\frac{(s+B)^3}{\left((s+B)^2+\omega_c^2\right)^3}\\
  \end{aligned}
  \end{equation}
  $$
- 三阶导数
  $$
  \begin{equation}
  \begin{aligned}
  \frac{\partial^3 \frac{s+B}{(s+B)^2+\omega_c^2}}{\partial s^3}=&\frac{-6}{((s+B)^2+\omega_c^2)^2}+48\frac{(s+B)^2}{\left((s+B)^3+\omega_c^2\right)^3}-48\frac{(s+B)^4}{\left((s+B)^2+\omega_c^2\right)^4}\\
  =&\frac{-6\left((s+B)^2+\omega_c^2\right)^2+48(s+B)^2\left((s+B)^2+\omega_c^2\right)-48(s+B)^4}{\left((s+B)^2+\omega_c^2\right)^4}\\
  =&\frac{6(-B^4-4B^3s-6B^2s^2-4Bs^3-s^4+6B^2\omega_c^2+12Bs\omega_c^2+6s^2\omega_c^2-\omega_c^4)}{(B^2+2Bs+s^2+\omega_c^2)^4}\\
  =&\frac{6((s-(-B+(3+2^{3/2})^{1/2}\omega_c)(s-(-B-(3+2^{3/2})^{1/2}\omega_c)(s-(-B+(3-2^{3/2})^{1/2}\omega_c(s-(-B-(3-2^{3/2})^{1/2}\omega_c))}{\left[(s-(j\omega_c-B))(s-(-j\omega_c-B))\right]^4}\\
  \end{aligned}
  \end{equation}
  $$
由三阶导数的结果可以看出，Gammatone滤波器可以看作四个滤波器及联
$$
\begin{equation}
\begin{aligned}
G_1(s)&=\frac{s-(-B+(3+2^{3/2})^{1/2}\omega_c)}{(s-(j\omega_c-B))(s-(-j\omega_c-B))}\\
G_2(s)&=\frac{s-(-B-(3+2^{3/2})^{1/2}\omega_c)}{(s-(j\omega_c-B))(s-(-j\omega_c-B))}\\
G_3(s)&=\frac{s-(-B+(3-2^{3/2})^{1/2}\omega_c)}{(s-(j\omega_c-B))(s-(-j\omega_c-B))}\\
G_4(s)&=\frac{s-(-B-(3-2^{3/2})^{1/2}\omega_c)}{(s-(j\omega_c-B))(s-(-j\omega_c-B))}
\end{aligned}
\end{equation}
$$
接下来分别计算这个四个滤波器对应数字滤波器的迭代公式
1. $G_1(s)$

    根据冲击响应不变法
    $$
    \begin{equation}
    \begin{aligned}
    G_1(s) &= \frac{s-(-B+(3+2^{3/2})^{1/2}\omega_c)}{(s-(j\omega_c-B))(s-(-j\omega_c-B))}=\frac{r_1}{(s-(j\omega_c-B))}+\frac{r_2}{(s-(-j\omega_c-B))}\\
    \end{aligned}
    \end{equation}
    $$
    因为
    $$
    \begin{equation}
    \begin{aligned}
    \begin{cases}
    r_1+r_2 = 1\\
    r_1(-j\omega_c-B)+r_2(j\omega_c-B)=-B+(3+2^{3/2})^{1/2}\omega_c
    \end{cases} \Rightarrow
    \begin{cases}
    r_1=\frac{1+j(3+2^{3/2})^{1/2}}{2}\\
    r_2=\frac{1-j(3+2^{3/2})^{1/2}}{2}\\
    \end{cases}
    \end{aligned}
    \end{equation}
    $$
    其中 $r_1$ 和 $r_2$ 共轭对称，即$r_1^*=r_2$
    $$
    \begin{equation}
    \begin{aligned}
    G_1(z)&=\frac{Tzr_1}{z-e^{T(j\omega_c-B)}}+\frac{Tzr_2}{z-e^{-T(j\omega_c-B)}}\\
    &=\frac{Tz(r_1(z-e^{T-(j\omega_c-B)})+r_2(z-e^{T(j\omega_c-B)}))}{(z-e^{T(j\omega_c-B)})(z-e^{T(-j\omega_c-B)})}\\
    &=\frac{Tz(z-e^{-TB}(r_1e^{-jT\omega_c}+r_2e^{jT\omega_c}))}{z^2-(e^{T(j\omega_c-B)}e^{T(-j\omega_c-B)})z+e^{-2BT}}\\
    &=\frac{Tz(z-2e^{-BT}\mathcal{R}(r_1e^{-jT\omega_c}))}{z^2-2e^{-BT}cos(T\omega_c)z+e^{-2BT}}\\
    &=T\frac{z^2-2ze^{-BT}\mathcal{R}(\frac{1+j(3+2^{3/2})^{1/2}}{2}e^{-jT\omega_c})}{z^2-2e^{-BT}cos(T\omega_c)z+e^{-2BT}}\\
    &=T\frac{z^2-2ze^{-BT}(\cos(T\omega_c)+(3+2^{3/2})^{1/2}\sin(T\omega_c))}{z^2-2e^{-BT}cos(T\omega_c)z+e^{-2BT}}\\
    &=T\frac{1-2e^{-BT}(\cos(T\omega_c)+(3+2^{3/2})^{1/2}\sin(T\omega_c))z^{-1}}{z-2e^{-BT}cos(T\omega_c)z^{-1}+e^{-2BT}z^{-2}}\\
    \end{aligned}
    \end{equation}
    $$

2. $G_2(z)$

    类似的
    $$
    \begin{equation}
    \begin{aligned}
    \begin{cases}
    r_1+r_2=1\\
    r_1(-j\omega_c-B)+r_2(j\omega_c-B)=-B-(3+2^{3/2})^{1/2}\omega_c
    \end{cases}\Rightarrow
    \begin{cases}
    r1 = \frac{1-j(3+2^{3/2})^{1/2}}{2}\\
    r_2=\frac{1+j(3+2^{3/2})^{1/2}}{2}
    \end{cases}
    \end{aligned}
    \end{equation}
    $$
    $r_1,r2$依然是共轭的
    $$
    \begin{equation}
    \begin{aligned}
    G_2(z)&=\frac{Tz(z-2e^{-BT}\mathcal{R}(r_1e^{-jT\omega_c}))}{z^2-2e^{-BT}cos(T\omega_c)z+e^{-2BT}}\\
    &=T\frac{z^2-2ze^{-BT}\mathcal{R}\left(\frac{1-j(3+2^{3/2})^{1/2}}{2}e^{-jT\omega_c}\right)}{z^2-2e^{-BT}cos(T\omega_c)z+e^{-2BT}}\\
    &=T\frac{z^2-2ze^{-BT}\left(\cos{(T\omega_c)}-(3+2^{3/2})^{1/2}\sin{(T\omega_c)}\right)}{z^2-2e^{-BT}cos(T\omega_c)z+e^{-2BT}}\\
    &=T\frac{1-2e^{-BT}\left(\cos{(T\omega_c)}-(3+2^{3/2})^{1/2}\sin{(T\omega_c)}\right)z^{-1}}{1-2e^{-BT}cos(T\omega_c)z^{-1}+e^{-2BT}z^{-2}}\\
    \end{aligned}
    \end{equation}
    $$
    $G_3(z),G_4(z)$ 的形式与 $G_1(z),G_2(z)$相对应，可直接写出

3. $G_3(z)$

  $$
  \begin{equation}
  \begin{aligned}
  G_3(z)=T\frac{1-2e^{-BT}\left(\cos{(T\omega_c)}+(3-2^{3/2})^{1/2}\sin{(T\omega_c)}\right)z^{-1}}{1-2e^{-BT}cos(T\omega_c)z^{-1}+e^{-2BT}z^{-2}}\\
  \end{aligned}
  \end{equation}
  $$

4. $G_4(z)$
    $$
    \begin{equation}
    \begin{aligned}
    G_4(z)=T\frac{1-2e^{-BT}\left(\cos{(T\omega_c)}-(3-2^{3/2})^{1/2}\sin{(T\omega_c)}\right)z^{-1}}{1-2e^{-BT}cos(T\omega_c)z^{-1}+e^{-2BT}z^{-2}}\\
    \end{aligned}
    \end{equation}
    $$

  ## 中心频率处的增益和相移

  $$
  \begin{equation}
  \begin{aligned}
  G(s)_{s=j\omega_c}&=\frac{6(j\omega_c+B-(3+2^{3/2})^{1/2}\omega_c)(j\omega_c+B+(3+2^{3/2})^{1/2}\omega_c)(j\omega_c+B-(3-2^{3/2})^{1/2}\omega_c)(j\omega_c+B+(3-2^{3/2})^{1/2}\omega_c)}{\left[B(2j\omega_c+B)\right]^4}\\
  &=\frac{6\left[(j\omega_c+B)^2-(3+2^{3/2})\omega_c^2\right]\left[(j\omega_c+B)^2-(3-2^{3/2})\omega_c^2\right]}{\left[B(2j\omega_c+B)\right]^4}\\
  &=\frac{6\left[2jB\omega_c+B^2-(4+2^{3/2})\omega_c^2\right]\left[2jB\omega_c+B^2-(4-2^{3/2})\omega_c^2\right]}{(2jB\omega_c+B^2)^4}\\
  &=\frac{}{B}
  \end{aligned}
  \end{equation}
  $$
