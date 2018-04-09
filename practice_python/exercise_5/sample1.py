import numpy as np
import sys


try_max = 10    #初期値入力の最大試行回数

error_abs = 1.E-12   #求めたい答えの精度


''' f(x) = x^2 - 2.0 '''
''' f(x) = 0 となるのは x = √2, -√2 '''
def func(x):
    return x**2 - 2.0


a_ini = int(input("aの初期値を入力してください => "))
b_ini = int(input("bの初期値を入力してください => "))
c_old = 0.

''' 外部入力により初期値を設定 '''
''' f(a)*f(b) < 0 となるまで試行 '''
for i in np.arange(0, 1000):
    if int(i) == try_max:
        print("もう一度プログラムを実行してください\n")
        sys.exit()

    elif func(a_ini)*func(b_ini) >= 0.:
        print("もう一度入力し直してください\n")
        a_ini = int(input("aの初期値を入力してください => "))
        b_ini = int(input("bの初期値を入力してください => "))
    
    elif func(a_ini)*func(b_ini) <= 0.:
        break

''' b > a となるように調整 '''
if b_ini-a_ini >= 0.:
    a = a_ini
    b = b_ini
elif b_ini-a_ini < 0.:
    b = a_ini
    a = b_ini


''' 二分法 '''
for j in np.arange(0, 1000):

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

print(ans)

