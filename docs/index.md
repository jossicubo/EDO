# Métodos numéricos



## Método de Euler 
El método de Euler es muy sencillo, se basa en la expansión de Taylor de la función $x(t)$. Tenemos
$$
\text{Expansión Taylor} \Rightarrow x(t+h) = x(t) + h\frac{dx}{dt} + \overbrace{ \frac{h^2}{2} \frac{d^2x}{dt^2} } ^{\epsilon} + O(h^3).
$$
Es decir, que para avanzar en el tiempo la función por un paso $h$, el cual suponemos que es lo suficientemente pequeño, basta con utilizar la ecuación
$$
\boxed{x(t + h) = x(t) + hf(x,t).}

$$
El error asociado con la aproximación **está ligado a la cantidad de veces que hagamos la aproximación**, es decir, al número de pasos en el tiempo que utilicemos en nuestra solución. Es posible estimarlo haciendo:

$$
\sum\epsilon = \sum_{k=0}^{N-1}\frac{h^2}{2}\left. \frac{d^2x}{dt^2} \right|_{x_k, t_k} = \frac{h}{2}\sum_{k=0}^{N-1}h\left.\frac{df}{dt}\right|_{x_k, t_k}\\
\approx \frac{h}2\int_a^b\frac{df}{dt}d t = \frac{h}{2}\left[f_b - f_a\right].
$$


En la ecuación anterior asumimos que tomamos $N = (b-a)/h$ pasos temporales para llegar al punto final.

Por tanto, el error total de aproximación depende $h$ linealmente multiplicado por el intervalo en el cual realizamos la integración.

* Para algunas aplicaciones, esto es suficiente. Para otras, necesitamos una mejor aproximación.
* El algoritmo toma la siguiente forma:
  - Empezar con $t = t_0$, $x = x_0$
  - Discretizar el tiempo en pasos temporales de forma equidistante con espaciamiento $h$, donde cada punto en el tiempo está denotado con $t_i$
  - Para cada punto en el tiempo encontrar $x$ utilizando el resultado de la iteración previa: $x_i = x_{i-1} + hf(x_{i-1})$


## Método de Runge-Kutta 2$^{\rm do}$ Orden (RK2)
La idea del método RK2 es utilizar el punto medio para evaluar el método de Euler, como se indica en la figura. Mientras que el método de Euler se aplica en el punto $t$ para evaluar la derivada para aproximar la función en el punto $x = t + h$, el método RK2 utiliza el punto medio $t + h/2$. 

De esta forma, se alcanza una mejor aproximación para el mismo valor de $h$.

El método se deriva aplicando la serie de Taylor alrededor del punto medio $t + h/2$ para obtener el valor de la función en el punto $x(t + h)$. De manera que se obtiene:
$$
\boxed{x(t + h) = x(t) + hf[x(t + h/2), t + h/2] + O(h^3)}.
$$

El único problema es que requerimos conocer el valor de la función en el punto medio $x(t + h/2)$, el cual desconocemos.

Para aproximar este valor utilizamos el método de Euler con un paso $h/2$, $(x + h/2) = x(t) + \frac{h}{2}f(x,t)$. De esta manera, obtenemos las ecuaciones del método RK2:*
 $k_1 = hf(x,t),$*
 *$k_2 = hf\left(x + \frac{k_1}{2},t + \frac{h}{2}\right)$*
 *$x(t + h) = x(t) + k_2$
El error de aproximación de cada paso es de orden $O(h^3)$, mientras que el error global (con un análisis similar al que hicimos con el método de Euler) es de order $O(h^2)$.

## Método de Runge-Kutta de 4$^{\rm to}$ Orden

La metodología anterior se puede aplicar aún a más puntos ubicados entre $x(t)$ y $x(t + h)$ realizando expansiones de Taylor. De esta forma se pueden agrupar términos de orden $h^3$, $h^4$, etc; para cancelar dichas expresiones. 

El problema de hacer esto es que las expresiones se vuelven más complicadas conforme incrementamos el orden de aproximación. En general, la regla de dedo es que el $4^{\rm to}$ orden corresponde al mejor compromiso entre complejidad y error de aproximación. Este método es el más utilizado comunmente para resolver ODEs. 

Haciendo el álgebra se obtiene:
* $k_1 = hf(x, t)$,
* $k_2 = hf\left(x + \frac{k_1}{2}, t+\frac{h}2\right)$,
* $k_3 = hf\left(x + \frac{k_2}{2}, t+\frac{h}2\right)$,
* $k_4 = hf\left(x + k_3, t + h \right)$,
* $x(t+h) = x(t) + \frac{1}{6}(k_1 + 2 k_2 + 2k_3 + k_4)$.

Usualmente el método RK4 es el más utilizado para obtener soluciones. Es fácil de programar y devuelve resultados precisos. 

El error de aproximación es $O(h^5)$, mientras que el error global es aproximadamente del orden $O(h^4)$.






