# Permitivity tissues
==============================
Permitivity Tissues is a code written in Python to calculate the frequency dependent permitivity (dielectric function) of selected tissues of human body.

The dielectric function implemented in this code is the Cole Cole's Model.

Requirements
================= 
You must have installed Python in your PC or Unix based OS, in specific the  Python- [Anaconda](https://store.continuum.io/cshop/anaconda/)  2.7 distribution . It's recomendable to have some Integrated Development Environment (IDE) used for programming in Python such as PyCharm.  It provides code analysis, graphical debugger, integrated unit tester.

Using Permitivity Tissues
================= 

To use this code, first download the .zip file and locate  all the content in a unique folder in the hard drive.
Once this is done you can open the script `run`. If you decided to use PyCharm you must create first a project and then open the script. 

First to modify is the temperature you want to get the data. In this code the are 2 temperatures 20ºC and 37º C. If you want to use 20ºC the comand `tissues = Tissue20()` must be set. In the case of 37ºC `tissues = Tissue37()` must be set.
In this script you will find a function with four input arguments:

```
param = Parameters(tissues.bone, wmin, wmax)
```

where the first argument is related to the kind of tissue, you can write brain_grey, brain_white, bone, cornea, retina, water, tongue(just in 37 ) after the dot and the tissues word, in the last display the word bone is set by default as an example; the second and third parameter are related to the minimum and maximum of the frequency which the permitivity is going to be calculated. Use for example 1e6 Hz as minimum and 1e9 as maximum . An example of calculation is the next
```
tissues = Tissue20()
param = Parameters(metals.brain_grey, 1e6, 1e9)
```

The code will display a plot and the corresponding data is saved in the folder `output`. And every time you run the code, the data and plots will be updated in this folder.





Theory
=============================
La función dieléctrica es entonces un parámetro que permite conocer cómo responde un material, en este caso un tejido, ante un campo externo.  Para modelar función dieléctrica en tejidos biológicos se consideran tres mecanismos de interacción, los cuales determinan tres regiones en el espectro de frecuencias: las dispersiones $\alpha$, $\beta$ y $\gamma$.
La dispersión $\gamma$, domina en la región de GHz y se considera es causada por la polarización de las moléculas de agua.  La dispersión $\beta$, típicamente se encuentra en una región entre cientos a miles de Hz. Se considera que es causada por la polarización de las membranas celulares que actúan como barreras ante el flujo de iones afuera y dentro de la célula. La dispersión $\alpha$ se asocia con la difusión iónica en la membrana celular [1].

En una manera simple, cada dispersión está caracterizada por un tiempo de relajación $\tau$ y la función dieléctrica adquiere dependencia en la frecuencia:
```math
$$
\begin{equation}
\epsilon(\omega)=\epsilon_{\infty}+\frac{\epsilon_S-\epsilon_{\infty}}{1+i\omega \tau},
\nonumber
\end{equation}
$$
```

donde $\tau$ es el tiempo de relajación para cada región de dispersión, $\epsilon_S$ corresponde a los valores de la permitividad  a frecuencias bajas $\omega \tau << 1$, $\epsilon_{infty}$ es el valor de la permitividad a frecuencias del campo.

La presencia de varios mecanismos de relajación con sus respectivos tiempos de relajación en un material  se puede modelar como [1]:
\begin{equation}
\epsilon(\omega)=\epsilon_{\infty}+\frac{\epsilon_S-\epsilon_{\infty}}{1+(i\omega \tau)^{1-\alpha}},
\nonumber
\end{equation}
 
La expresión anterior se conoce como la permitividad semi-empírica de Cole-Cole, en la cual el parámetro $\alpha$ se introduce para describir el aumento en la dispersión \cite{R4}.
De esta manera, está propuesto que el espectro de la función dieléctrica para un tejido conformado por $n$ materiales, se describa matemáticamente como:

\begin{equation}
\epsilon(\omega)=\epsilon_{\infty}+\sum_n \frac{\epsilon_{S,n}-\epsilon_{\infty,n}}{1+(i\omega \tau_n)^{1-\alpha_n}}+\frac{\sigma_i}{i\omega \epsilon_0},
\nonumber
\end{equation}

La cantidad que mide la facilidad con la que las cargas de conducción se mueven se conoce como conductividad $\sigma$.  La permitividad explícitamente se escribe como:
\begin{equation}
\hat{\epsilon}=\epsilon_0(\epsilon_R+i \epsilon_I), \ F/m,
\label{permit}
\end{equation}
 donde $\epsilon_0=8.85\times 10^{-12}F/M$ es la permitividad del vacío y $\epsilon_R$ y $\epsilon_I$  son las partes real e imaginaria de la permitividad. Convencionalmente al cociente $\frac{\hat{\epsilon}}{\epsilon_0}$ se le conoce como función dieléctrica $\epsilon$. Reescribiendo (\ref{permit}) e introduciendo la relación entre la conductividad y la parte imaginaria de la permitividad  $\epsilon_I=\frac{\sigma}{\omega \epsilon_0}$, se tiene entonces:
\begin{equation}
\epsilon(\omega)=\epsilon_R+i \frac{\sigma}{\omega \epsilon_0}.
\end{equation}
