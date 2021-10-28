---
layout: post
title:  "github pages summaries"
categories: tools
tags: blog
author: Todd
description: collections of problems I countered in using githb pages
---

有时本地jekyll渲染的结果与github page的显示结果不同，可能是markdown解析器有些差别（有时间再去确定）

<!-- TOC -->

- [latex公式显示](#latex%E5%85%AC%E5%BC%8F%E6%98%BE%E7%A4%BA)
- [源码显示](#%E6%BA%90%E7%A0%81%E6%98%BE%E7%A4%BA)

<!-- /TOC -->

## latex公式显示

  [`Kramdown`](https://kramdown.gettalong.org/index.html)默认使用[`Mathjax`](https://www.mathjax.org/)渲染latex公式，其实只是将latex公式解析为html语句，例如：

  <table border="1" align="center">
  <thead>
  <tr align="center"> <td>Equation</td> <td>Latex</td> <td>html</td></tr>
  </thead>
  <tr>
  <td>
  $$\begin{equation}
  \begin{aligned}
  y=\frac{\sin(x)}{x}
  \end{aligned}
  \end{equation}$$
  </td>
  <td><pre> <code>
  $$\begin{equation}<br>
  \begin{aligned}<br>
  y=\frac{\sin(x)}{x}<br>
  \end{aligned}<br>
  \end{equation}$$
  </code> </pre></td>
  <td><pre><code>
  <script type="math/tex; mode=display" id="MathJax-Element-1"\><br>
  \begin{equation}<br>
  \begin{aligned}<br>
  y=\frac{\sin(x)}{x}<br>
  \end{aligned}<br>
  \end{equation}</script>
  </code></pre></td>
  </tr>
  </table>

  只是这样，并不能显示公式，还需要在待显示latex公式之前加入
  ```html
  <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
  ```
  也可以加入到`default.html`中，对全部文件都有效

## 源码显示

  ```html
  <pre><code>
  source code to be shown
  </code></pre>
  ```
