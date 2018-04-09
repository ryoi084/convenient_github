import numpy as np
import sys


error_abs = 1.E-15   #求めたい答えの精度


''' f(x) = x^2 - 2.0 '''
''' f(x) = 0 となるのは x = √2, -√2 '''
def func(x):
    return x**2 - 2.0


''' ここで初期値をいれる '''
a_ini = 0
b_ini = 2
c_old = 0.

''' f(a)*f(b) < 0 となるまで試行 '''
if func(a_ini)*func(b_ini) >= 0.:
    print("もう一度入力し直してください\n")
    sys.exit()
    

''' b > a となるように調整 '''
if b_ini-a_ini >= 0.:
    a = a_ini
    b = b_ini
elif b_ini-a_ini < 0.:
    b = a_ini
    a = b_ini


''' 二分法 '''
for i in np.arange(0, 1000):

    c = (a + b)/2.  #中点を計算

    if func(a)*func(c) >= 0:    #中点が次にどちらに移るかを判別
        a = c
    else:
        b = c

    ''' 以前の結果と今回の結果が error_abs 以下になればループを抜ける '''
    if np.abs(c - c_old) <= error_abs:
        break
    else:
        c_old = c

ans = c

print("f(x)=0  <=  x=",ans)
print("試行回数", i, "回")

