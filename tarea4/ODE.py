# tarea4/ODE.py

""" Algunos ejemplos se muestran a continuación

Examples:
    >>> euler(f, t1, 0.0)
    [ 0.          0.          1.18623077 -0.15217513 -0.86222182]
    >>> rk2(fc, t, 0.0)
    [ 0.          0.73137159  0.34943373 -0.05274473 -1.14619757]
    >>> rk4(fc, t, 0.0)
    [ 0.          0.60218291  0.15942164  0.11425799 -0.77075997]

El módulo contiene las siguientes funciones:

- `euler(f, t, x)` - Devuelve la solución de la EDO calculada con el método de euler.
- `rk2(f, t, x)` - Devuelve la solución de la EDO calculada con el método de Runge-Kutta de segundo orden.
- `rk4(f, t, x)` - Devuelve la solución de la EDO calculada con el método de Runge-Kutta de cuarto orden



"""

def euler(f, t, xi):
    """Resuelve la EDO utilizando el método de Euler.

    Examples:
        >>> t = np.linspace(0.0, 5.0, 5)
        >>> def f(x,t): return -(x**3) + np.sin(t)
        >>> euler(f, t1, 0.0)
        [ 0.          0.          1.18623077 -0.15217513 -0.86222182]


    Args:
        f (function): Una EDO de la forma dx/dt=f(x,t)
        t (array): Grilla temporal de pasos equidistantes
        xi (int): Condición inicial en "t=0"

    Returns:
        x (array): Un arreglo que corresponde a las soluciones de la ecuación diferencial en los tiempos t
    """
    h = t[1]-t[0]
    x = np.zeros(t.size)
    x[0] = xi

    for i in range(t.size-1):
        x[i+1] = x[i]+h*f(x[i],t[i])

    return x

def rk2(f, t, xi):
    """Implementa el método de Runge-Kutta de 2do orden.

    Examples:
        >>> t = np.linspace(0.0, 5.0, 5)
        >>> def f(x,t): return -(x**3) + np.sin(t)
        >>> rk2(fc, t, 0.0)
        array([ 0.          0.73137159  0.34943373 -0.05274473 -1.14619757])

    Args:
       f (function): Una EDO de la forma dx/dt = f(x,t)
       t (array): Grilla temporal de pasos equidistantes
       xi (int): Condición inicial en t=0


    Returns:
       x (array): Un arreglo que corresponde a las soluciones de la ecuación diferencial en los tiempos t
    """

    h = t[1]-t[0]
    x = np.zeros(t.size)
    x[0] = xi

    for i in range(t.size-1):
        k1 = h * f(x[i],t[i])
        k2 = h * f(x[i]+(k1/2),t[i]+(h/2))
        x[i+1] = x[i] + k2

    return x


def rk4(f, t, xi):
    """Implementa el método de Runge-Kutta de 4to orden.

    Examples:
        >>> t = np.linspace(0.0, 5.0, 5)
        >>> def f(x,t): return -(x**3) + np.sin(t)
        >>> rk4(fc, t, 0.0)
        array([ 0.          0.60218291  0.15942164  0.11425799 -0.77075997])

    Args:
       f (function): Una EDO de la forma dx/dt = f(x,t)
       t (array): Grilla temporal de pasos equidistantes
       xi (int): Condición inicial en t=0


    Returns:
       x (array): Devuelve un arreglo con las soluciones de la EDO en los tiempos t


    """
    h = t[1]-t[0]
    x = np.zeros(t.size)
    x[0] = xi

    for i in range(t.size-1):
        k1 = h * f(x[i],t[i])
        k2 = h * f(x[i]+(k1/2),t[i]+(h/2))
        k3 = h * f(x[i]+(k2/2),t[i]+(h/2))
        k4 = h * f(x[i]+k3,t[i]+h)
        x[i+1] = x[i]+(1/6)*(k1+2*k2+2*k3+k4)

    return x

