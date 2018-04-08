import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

''' f(x) = x^2 - 2 を定義する'''
'''f(x) = 0 の解は x = √2, -√2 となる '''
def func(x):
    return x**2 - 2.0

fig = plt.figure()

'''√2は1.4くらいということはわかっているので, 0~2とあたりをつける'''
a_int = 1.40625
b_int = 1.4375


x = np.linspace(-2,4,100)

def make_ini(x):
    plt.hlines(0.0, np.min(x)*1.2, np.max(x)*1.2, linestyles='dashed', lw=1)
    plt.vlines(0.0, np.min(func(x))*1.2, np.max(func(x)*1.2), linestyles='dashed', lw=1)
    plt.xlim(np.min(x)*1.2, np.max(x)*1.2)
    plt.ylim(np.min(func(x))*1.2, np.max(func(x))*1.2)
    plt.plot(x, func(x))

a = a_int
b = b_int

plt.cla()
make_ini(x)
plt.plot(a, func(a),"o", color='red')
plt.plot(b, func(b),"o", color='red')
plt.savefig('imag_19.png')

plt.cla()
make_ini(x)
c = (a + b)/2.
plt.plot(a, func(a),"o", color='red')
plt.plot(b, func(b),"o", color='red')
plt.plot(c, func(c), "o", color='green')
plt.savefig('imag_20.png')

plt.cla()
if func(c) * func(a) >= 0.:
    make_ini(x)
    plt.plot(a, func(a), "o", color='black')
    plt.plot(b, func(b), "o", color='red')
    plt.plot(c, func(c), "o", color='red')
    a = c

else:
    make_ini(x)
    plt.plot(a, func(a), "o", color='red')
    plt.plot(b, func(b), "o", color='black')
    plt.plot(c, func(c), "o", color='red')
    b = c
plt.savefig('imag_21.png')

print(a, b)
    




