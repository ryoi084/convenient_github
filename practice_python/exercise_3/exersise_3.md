# Exercise 3

> 今回からサンプルプログラムを同じディレクトリ内に入れておくので, 

> 参考にしてみてください


## グラフを表示してみよう

今回は以前導入した2つのライブラリを活用してみようと思います.

Pythonでは, programの初めにどのライブラリを使うかを宣言しなければいけません.

では, program冒頭に次のように書いてみましょう.

> `import numpy`

> `import matplotlib.pyplot`

次に, 呪文のように次の文を打ちましょう.

> `x = numpy.linspace(-10, 10, 100)`

> `fig = matplotlib.pyplot.figure()`

後で詳しく解説しようと思います.

続いて

> `matplotlib.pyplot.plot(x, x**2)`

> `matplotlib.pyplot.show()`

と記述して実行してみましょう.

放物線の関数が表示されれば成功です!


## 簡単な説明

初めに

> `imoprt <...>`

と記述したところがありました.

この<...>の部分にライブラリの名前を入れることで以降のprogram内で使えるようになります.

programを見てもらえればわかると思うのですが, 

numpyやmatplotlibと書かれているところがいくつかあると思います.

ここで先ほど宣言したものが活きてくるわけですね.

 
続いて

> `x = numpy.linspace(-10, 10, 100)`

についてですが, これはNumPy内の`linspace`というモジュールによって

-10 から 10 までを 100等分した配列を生成します.

つまり

> `x = np.array([-10, -9.7979, ..., 9.7979, 10])`

というふうに自動で生成されます(コレ, 実は非常に便利です).

また

> `fig = matplotlib.pyplot.figure()`

という箇所がありますが, これは難しいので今回はこういうものであると受け入れてください.

(白状すると僕もちゃんとは把握しきれていません汗)

最後に

> `matplotlib.pyplot.plot(x, x**2)`

> `matplotlib.pyplot.show()`

についてですが,

上の式は見てわかる通り `x` に対して `x**2` のプロットをしています.

この部分の `x**2` を `x**3` とか `x**2 - 40.0` とかにすることで色々変えることができます.

そして, `.show()` で実際に表示をしています.

大体の流れは理解出来ましたでしょうか?

慣れてくるとそこまで難しくないので色々トライしてみてください.


## ライブラリの記法の省略方法

実際書いてみて感じたと思うのですが,

何度も `numpy` や `matplotlib.pyplot` と打つのは正直面倒くさいです...

そこで, はじめの宣言のところでモジュールに自分で名前をつけることで, 多少楽にすることができます.

例えば, `as` という指示を用いて

> import numpy as np`

とすれば, 以降 `numpy` の代わりに `np` のみで済むようになります.

更に

> `import matplotlib.pyplot as plt`

とすれば, あの長ったらしかった `matplotlib.pyplot` の記述が たったの `plt` の三文字で済むようになります!

どんどん活用してみましょう!

(ちなみに, 上で書いたように `numpy` は `np`, `matplotlib.pyplot` は `plt` と省略することが多い気がします)


## sin(x)を書いてみよう

最後に, `numpy` のモジュールである `np.sin(x)` を用いて正弦波をプロットしてみてください.

これはサンプルに載せていないので頑張ってみてくださいね.
