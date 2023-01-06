# Static heat distribution problem

General problem:

$$
\dfrac{\partial}{\partial x}\left(k(x, z)\dfrac{\partial u}{\partial x}\right) +
\dfrac{\partial}{\partial z}\left(k(x, z)\dfrac{\partial u}{\partial z}\right)
= f(x, z)
$$

Simplified problem:

$$
\dfrac{\partial^2 u}{\partial x^2} + \dfrac{\partial^2 u}{\partial z^2} = F(x, z) = - \dfrac{f(x, z)}{k}
$$

Finite differences methods:
- Seidel
- Thomas (tridiagonal) - faster and more accurate

Monte-carlo methods:
- Fixed random walk - works fine
- Float random walk - fast but innacurate near heating source
- Semi-float random walk - works fine with step size $\approx 1$

![Finite differences solution example](/seidel1.png)
