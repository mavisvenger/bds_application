# bds_application

Find the roots of the function
f(x) = x^4 − x − 2
with all of the methods (Method 1-3) described above.

Terminate iteration process if |f(xn+1)| ≤ 10−8. Print out all computed values of xn and the number of iterations needed to obtain the required accuracy.
The code of the solution must contain the following functions:

• iter(x0,f,df,ddf,eps,maxit),
• euler(x0,f,df,ddf,eps,maxit),
• halley(x0,f,df,ddf,eps,maxit).

Here x0 is the initial guess, f is the function from the equation f(x) = 0, df is the first derivative of f, ddf is the second derivative of f, eps is from the termination condition |f(xn+1)| ≤ ε, and maxit is the upper bound for the number of iterations. The functions iter, euler and halley must return the last approximation and the number of iterations needed to obtain the required accuracy.
