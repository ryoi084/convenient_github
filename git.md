###参考サイト
[サルでもわかるGit入門](https://backlog.com/ja/git-tutorial/intro/intro1_1.html)

#使い方の簡単な説明
1. ローカルレポジトリとして保存したいディレクトリを決める(今回はディレクトリ名をfooと名付けることにする)
2. そのなかにGitに保存したいファイル(フォルダ)を作成する(今回はファイル名をtest.txtと名付けることにする)
3. addすることで、Gitに保存したいファイルであることを認識させる
4. commitすることでGitに履歴と共に保存される
5. GitをGitHubやbitbucketと連携させることで、web上で管理することができるようになる

##インストール
`$ sudo apt-get install git`

##fooディレクトリをGitの管理下に置く
`.../foo$ git init `

##保存したい(履歴を残したい)ファイルを認識させる
`.../foo$ git add test.txt`

##gitにファイルを保存する
`.../foo$ git commit -m '<コメント>'`

