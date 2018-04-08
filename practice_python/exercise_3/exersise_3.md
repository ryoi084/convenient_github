# Exercise 3

## グラフを表示してみよう
今回は以前導入した2つのライブラリを活用してみようと思います.

Pythonでは, programの初めにどのライブラリを使うかを宣言しなければいけません.

では, program冒頭に次のように書いてみましょう.

`import numpy`

`import matplotlib.pyplot`

次に, 呪文のように次の文を打ちましょう.

`x = numpy.linspace(-10,10,100)`

`fig = matplotlib.pyplot.figure()`

後で詳しく解説しようと思います.

続いて

`matplotlib.pyplot.plot(x,x**2)`

`matplotlib.pyplot.show()`

と記述して実行してみましょう.

放物線の関数が表示されれば成功です!

## 簡単な説明

初めに

`imoprt <...>`

と記述したところがありました.

この<...>の部分にライブラリの名前を入れることで以降のprogram内で使えるようになります.


