
有时本地jekyll渲染的结果与github page的显示结果不同，可能是markdown解析器有些差别（有时间再去确定）

下边是我遇到过的一些问题
- latex公式显示

  github page默认使用Kramdown解析器，[`Kramdown`](https://kramdown.gettalong.org/index.html)默认使用[`Mathjax`](https://www.mathjax.org/)渲染latex公式。
  ```html
  <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
  ```
