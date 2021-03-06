# windowsにpython3.6.5をダウンロード

今回は数値計算でpythonを用いるために

最低限のライブラリとして

- NumPy
- SciPy
- Matplotlib

の3つを導入しようと思います.


## python3.6.5のインストール
公式サイトからPython 3.6.5のx86-64のものを探してダウンロードします.

[公式サイト](https://www.python.org/downloads/windows/)

(2018/4/9現在の最新は, 2018-03-28のもの)

インストールの画面になった際, もし欄が存在したらPATHを入れてもらうようにしましょう.

次にコマンドプロンプトを開いて次のように打ってみてください.

`> python -h`

もしこれでいろんな情報が出てきたらOKです.

例えば

`バッチファイルとして認識されていません。`

などと出てきた時はPATHが通っていないことが原因であることが多いので,

環境変数をいじってあげましょう.



## パッケージのインストール
### matplotlib
グラフを出力してくれるライブラリです.

pythonをインストールした時に勝手にインストールしてくれるpipというものを用いてコンピュータに導入します.

コマンドプロンプトで次のように入力してください.

`> pip install Matplotlib`

### NumPy
数値計算には必須のライブラリです.

こちらは[このサイト](https://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy)の中にあるpython3.6かつamd64であるものを選んでダウンロードをしてください.

その後, コマンドプロンプトでダウンロードしたところまで移動した後,

`> pip install <ダウンロードしてきたファイル名>`

と入力して, ダウンロードしてください.

### SciPy
フーリエ変換や数値積分などを簡単に行ってくれるライブラリです.

こちらもNumPyと同様の流れで外部のサイトから持ってきてダウンロードします.

[このサイト](https://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy)の中にあるpython3.6かつamd64であるものを選んでダウンロードしてください.

その後, コマンドプロンプトでダウンロードしたところまで移動した後,

`> pip install <ダウンロードしてきたファイル名>`

と入力して, ダウンロードしてください.


## 以上で使えるようになったと思います
ありがとうございました

これからもよろしくお願いします
