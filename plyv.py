# Calculate the value of a one-dimensional polynominal at spot x
# coef   : tuple,   arranged in descending power of x
# num    : int,     represent the most significant order of the polynominal
# x      : float,   independent variable
def plyv(coef,num,x)
    u=coef[-1]
	for i in xrange(num-2,0,-1)
	    u=u*x+coef[i]
    return u
