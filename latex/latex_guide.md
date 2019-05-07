

#### --------------------------------------------------
#### reference sections
Firstly, label the section as below sample:
```latex
\section{Introduction} \label{introduction}
...
```
Then reference to section akind:
```latex
...
As mentioned in section \ref{introduction}
...
```

#### reference equations, figures or tables
```latex
\begin{equation} \label{eq:1}
\sum_{i=0}^{\infty} a_i x^i
\end{equation}
 
The equation \ref{eq:1} is a typical power series.
```

Source: https://www.overleaf.com/learn/latex/Cross_referencing_sections_and_equations

#### --------------------------------------------------
#### math symbols(sum, product)
Sum:
```latex
\sum_{lower}^{upper}
$\sum_{n=1}^{\infty} 2^{-n} = 1$
```
![](https://cdn.sharelatex.com/learn-scripts/images/a/ac/Sum2.png)

Product:
```latex
\prod_{lower}^{upper}
$\prod_{i=a}^{b} f(i)$
```
![](https://cdn.sharelatex.com/learn-scripts/images/6/64/Prod2.png)

#### --------------------------------------------------
#### [Handbook from overleaf](https://www.overleaf.com/learn/latex/Integrals,_sums_and_limits)
#### [LaTeX mathematical symbols](https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols)