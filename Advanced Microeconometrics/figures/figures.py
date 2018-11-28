import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def Q(x, a = 1,b = 0,c = 0):
    return a* np.power(x,2) + b*x + c


def plot(xmin, xmax,x):
    A1 = 10
    A2 = 10
    B1 = -2
    B2 = -50
    C1 = 10
    C2 = 100

    e1 = 0.3
    e2 = -0.3

    plt.rc('text', usetex = True)
    plt.plot(np.linspace(xmin, xmax),
        [Q(theta,A1,B1,C1) for theta in np.linspace(xmin, xmax)],
        color = 'b',
        label = r'$Q_0(\theta)$')
    plt.plot(np.linspace(xmin, xmax),
        [Q(theta,A2,B2,C2) for theta in np.linspace(xmin, xmax)],
        color = 'black',
        label = r'$Q_N(\theta)$')
    plt.arrow(x+ e2, Q(x,A2,B2,C2) + e2,
              -1,-50,
              color = 'r',
              head_length = 30,
              head_width = 0.5)
    plt.text(-6.8,620, r'p', color = 'r')
    plt.axvline(-B1/(2*A1), color = 'black', linestyle = ':')
    plt.axvline(-B2/(2*A2), color = 'black', linestyle = ':')
    plt.text(-B1/(2*A1) + e1, 1000, r'$\theta_0$')
    plt.text(-B2/(2*A2) + e1, 1000, r'$\hat{\theta}_N$')
    plt.xlabel(r'\theta')
    plt.legend()
    cur_axes = plt.gca()
    cur_axes.axes.get_xaxis().set_ticks([])
    cur_axes.axes.get_yaxis().set_ticks([])
    plt.savefig('notes/figures/extremumconv.pdf')
    plt.show()


plot(-10,10, -5)




def f(x,a,b,c,d):
    return a*np.power(x,3) + b*np.power(x,2) + c*x + d


def mvtplot(xmin, xmax):
    a = 0.5
    b = 0.5
    c = -4
    d = 0

    x0 = -3.5
    x1 = 3

    l = 1
    s = (f(x1,a,b,c,d) - f(x0,a,b,c,d)) / (x1 - x0)
    # parameters of first derivative
    A = 3*a
    B = 2*b
    C = c-s

    xc = (-B + np.sqrt(np.power(B,2) -4*A*C)) / (2*A)
    span = np.linspace(xmin,xmax,1000)
    plt.plot(span,
            f(span, a,b,c,d),
            color = 'black')
    plt.scatter([x0, x1], [f(x0,a,b,c,d),f(x1,a,b,c,d)],
    color = 'b')
    plt.plot([x0, x1], [f(x0,a,b,c,d),f(x1,a,b,c,d)],
    color = 'b')
    plt.plot([xc-l, xc+l], [f(xc,a,b,c,d) - l*s ,f(xc,a,b,c,d)+l*s],
    color = 'b',
    linestyle = ':')
    plt.plot([xc, xc], [-15,f(xc,a,b,c,d)],
    color = 'black',
    linestyle = ':')
    plt.plot([x0, x0], [-15,f(x0,a,b,c,d)],
    color = 'black',
    linestyle = ':')
    plt.plot([x1, x1], [-15,f(x1,a,b,c,d)],
    color = 'black',
    linestyle = ':')
    plt.text( 0.658,0.07, r'$\theta^+$',transform=plt.gcf().transFigure)
    plt.text( 0.155,0.07, r'$\hat{\theta}_N$',transform=plt.gcf().transFigure)
    plt.text( 0.79,0.07, r'$\theta_0$',transform=plt.gcf().transFigure)
    plt.axis(xmin=xmin, xmax=xmax, ymin=-15,ymax=15)
    cur_axes = plt.gca()
    cur_axes.axes.get_xaxis().set_ticks([])
    cur_axes.axes.get_yaxis().set_ticks([])
    plt.savefig('notes/figures/mvt.pdf')
    plt.show()





mvtplot(-4,4)




def rho(z, tau):
    if z < 0:
        return (tau - 1)*z
    else:
        return tau*z



def rhoplot(minx,maxx, inc):
    tau = 0.3
    s1 = -5
    s2 = 3
    plt.plot(np.linspace(minx,maxx, inc),
    [rho(x, tau) for x in np.linspace(minx,maxx, inc)],
    color = 'b'
    )
    plt.axvline(0, color = 'black', linewidth = 1)
    plt.axis(xmin=minx, xmax=maxx, ymin=0)
    cur_axes = plt.gca()
    cur_axes.axes.get_xaxis().set_ticks([])
    cur_axes.axes.get_yaxis().set_ticks([])

    plt.step([s1,s1+1], [rho(s1, tau), rho(s1+1, tau)],
    color = 'b')
    plt.step([s2,s2+1], [rho(s2, tau), rho(s2+1, tau)],
    color = 'b')
    plt.text( 0.505,0.07, r'$z$',transform=plt.gcf().transFigure)
    plt.text( 0.59,0.225, r'$\tau$',transform=plt.gcf().transFigure)
    plt.text( 0.258,0.445, r'$1-\tau$',transform=plt.gcf().transFigure)
    plt.savefig('notes/figures/rho.pdf')
    plt.show()



rhoplot(-10,10,1000)
