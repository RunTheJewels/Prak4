import numpy as np
from scipy.special import factorial
from scipy.integrate import simps
import matplotlib.pyplot as plt
import matplotlib.animation as ani

def f(x):
	if (-1<x<1):
		return x
	elif (-3<x<=-1):
		return -x-2
	elif (-5<x<=-3):
		return x+4
	elif (1<=x<3):
		return -x+2
	elif (3<=x<5):
		return x-4

def h(x):
	if (-1<x<1):
		return 1
	elif (-3<x<=-1):
		return -1
	elif (-5<x<=-3):
		return 1
	elif (1<=x<3):
		return -1
	elif (3<=x<5):
		return 1

def g(x):
	return np.exp(x)

def mult(a,b):
	return a*b

def fourier(f=f,x0=0.0,x1=1.0,n=100,steps=20):
	mid=(x1-x0)/2.0
	xs=np.linspace(x0,x1,n,endpoint=True)
	ys=map(f,xs)
	a=np.empty([steps+1])
	b=np.empty([steps+1])
	b[0]=0.0
	a[0]=1.0/mid*simps(ys,x=xs)/2.0
	tmp=np.empty([n])
	for i in xrange(1,steps+1):
		print zip(map(lambda q: np.sin(i*q),xs),ys)
		for j in xrange(0,n):
			tmp[j]=np.sin(xs[j]*i)*ys[j]
		b[i]=1.0/mid*simps(tmp,x=xs)
		for j in xrange(0,n):
			tmp[j]=np.cos(xs[j]*i)*ys[j]
		a[i]=1.0/mid*simps(tmp,x=xs)
	print a,b
	solution=np.empty([steps+1,n])
	solution.fill(a[0])
	for i in xrange(1,steps+1):
		for j in xrange(0,n):
			for k in xrange(i,steps+1):
				solution[k,j]+=a[i]*np.sin(xs[j]*i)+b[i]*np.cos(xs[j]*i)
	def _graph_animate(t):
		line.set_ydata(solution[t])
		return line
	fig, ax = plt.subplots()
	ax.plot(xs, ys, c='black')
	line, = ax.plot(xs, solution[0])
	anm = ani.FuncAnimation(fig, _graph_animate, frames=steps+1, interval=100, repeat=False)
	plt.show()

fourier(f=h,x0=-4.5,x1=4.5,n=101)