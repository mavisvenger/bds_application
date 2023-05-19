import numpy as np

def iter(x0, f, df, ddf, eps, maxit):
    step = 0
    step_1 = 0
    x = x0
    x_1 = x0
    for i in range(maxit):
        next_x = - (np.sqrt(abs(df(x)**2 - 2*f(x)*ddf(x))) + df(x) - ddf(x)*x)/ddf(x)
        if abs(f(next_x)) <= eps:
            break
        x = next_x
        step = i
    for i in range(maxit):
        next_x = (np.sqrt(abs(df(x_1)**2 - 2*f(x_1)*ddf(x_1))) - df(x_1) + ddf(x_1)*x_1)/ddf(x_1)
        if abs(f(next_x)) <= eps:
            break
        x_1 = next_x
        step_1 = i
    return x, x_1, step, step_1

def g(x):
    return x**4 - x - 2

def dg(x):
    return 4*x**3 - 1

def ddg(x):
    return 12*x**2

def euler(x0, f, df, ddf, eps, maxit):
    step = 0
    x = x0
    x_1 = x0
    condition = True
    for i in range(maxit):
        next_x = x - f(x)/df(x) - ddf(x)/2/df(x)*(f(x)/df(x))**2
        if abs(f(next_x)) <= eps:
            break
        x = next_x
        step = i
    return x, step

def halley(x0, f, df, ddf, eps, maxit):
    step = 0
    x = x0
    x_1 = x0
    condition = True
    for i in range(maxit):
        next_x = x - f(x)*df(x)/(df(x)**2 - 0.5*ddf(x)*f(x))
        if abs(f(next_x)) <= eps:
            break
        x = next_x
        step = i
    return x, step
    
print(iter(2, g, dg, ddg, 10E-8, 20))
print(euler(-2, g, dg, ddg, 10E-8, 20), euler(2, g, dg, ddg, 10E-8, 20))
print(halley(-2, g, dg, ddg, 10E-8, 20), halley(2, g, dg, ddg, 10E-8, 20))
