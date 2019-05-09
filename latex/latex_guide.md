

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
#### figure
```latex
\begin{figure}[ht]
	\vskip 0.2in
	\begin{center}
		\centering{\includegraphics[width=\columnwidth]{fig/train_curves}}
		\caption{Operation modes and Types of grip}
		\label{fig:train_curves}
	\end{center}
	\vskip -0.2in
\end{figure}
```

#### full page width figure
```latex
\begin{figure*}[ht]
	\vskip 0.2in
	\begin{center}
		\centering{\includegraphics[width=\linewidth]{fig/overall_process}}
		\caption{Illustration of system's overall process}
		\label{fig:overall_process}
	\end{center}
	\vskip -0.2in
\end{figure*}
```

#### vertical figures
```latex
\begin{figure}
	\vskip 0.2in
	\begin{center}
		\vfill
		\subfigure[1st example]{\includegraphics[width=\columnwidth]{fig/0_1_tp}}
		\vfill
		\subfigure[2nd example]{\includegraphics[width=\columnwidth]{fig/1_0_tp}}
		\vfill
		\subfigure[3rd example]{\includegraphics[width=\columnwidth]{fig/1_1_tp}}
		\vfill
		\caption{Comparison between labels and predictions: the left ones are ground truths from auto-labeling process, and the right ones are segmentation results from point cloud deep network. We can see that the auto-labeled labels(left side) contain a lot of noise, but the predictions(right side) are clean. This illustrate the quality of point cloud segmentation network.}
		\label{fig:compare_segmentation}
	\end{center}
	\vskip -0.2in
\end{figure}
```

#### vertical figures
```latex
\begin{figure}
	\vskip 0.2in
	\begin{center}
		\hfill
		\subfigure[1st example]{\includegraphics[width=\columnwidth]{fig/0_1_tp}}
		\hfill
		\subfigure[2nd example]{\includegraphics[width=\columnwidth]{fig/1_0_tp}}
		\hfill
		\subfigure[3rd example]{\includegraphics[width=\columnwidth]{fig/1_1_tp}}
		\hfill
		\caption{Comparison between labels and predictions: the left ones are ground truths from auto-labeling process, and the right ones are segmentation results from point cloud deep network. We can see that the auto-labeled labels(left side) contain a lot of noise, but the predictions(right side) are clean. This illustrate the quality of point cloud segmentation network.}
		\label{fig:compare_segmentation}
	\end{center}
	\vskip -0.2in
\end{figure}
```

#### [Handbook from overleaf](https://www.overleaf.com/learn/latex/Integrals,_sums_and_limits)
#### [LaTeX mathematical symbols](https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols)