import numpy as np
from scipy.misc import derivative
from scipy.special import factorial
import matplotlib.pyplot as plt
import matplotlib.animation as ani

def f(x):
	return np.cos(x)*x+1.43*np.log(x)

def taylor(f=f,x0=0,x1=1,n=100,a=0.5,power=10):
	if ((a>=x1) or (a<=x0)):
		raise Exception("a must between x0 and x1!")
	vector=np.vectorize(f)
	xs=np.linspace(x0,x1,n,endpoint=True)
	der=np.zeros((power+1))
	der[0]=f(a)
	for i in xrange(1,power+1):
		der[i]=derivative(func=f,x0=a,dx=0.1,n=i,order=2*i+1)
	solution=np.empty([power+1,n])
	solution.fill(der[0])
	for i in xrange(1,power+1):
		for j in xrange(0,n):
			for k in xrange(i,power+1):
				solution[k,j]+=der[i]/factorial(i)*(xs[j]-a)**i
	def _graph_animate(t):
			line.set_ydata(solution[t])
			return line
	fig, ax = plt.subplots()
	ax.plot(xs, vector(xs),c='black')
	line, = ax.plot(xs, solution[0])
	anm = ani.FuncAnimation(fig, _graph_animate, frames=power+1, interval=300, repeat=False)
	plt.show()

x0=0
x1=10
a=5
n=100
p=20
taylor(x0=x0,x1=x1,n=n,f=f,power=p,a=a)