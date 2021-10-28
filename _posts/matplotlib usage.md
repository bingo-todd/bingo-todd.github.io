# 坐标轴tick变换

axis对象的`set_xscale`/`set_yscale`

可以使用buildin函数，或者自定义
自定义e.g.
```python
ax.set_xscale('function',functions=(forward_f,inverse_f))
```
同时指定坐标轴变换的正反函数

```python
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.subplots(1,1)
···
