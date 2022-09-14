# JupyterHubと格闘した一般男性の記録

## JupyterHub の解説

### JupyterHubのJupyterとは

Julia Python R の3つのプログラミング言語の名前からそれぞれ引用して作られた名前です。(諸説あり)
複数の言語をプロジェクト単位で同時に扱えるのが特徴です。

### ipynbファイルとは

JupyterNotebook の実行環境で作成できるファイルです。
スクリプトをセルという単位で複数管理できます。

### JupyterHubとは

JupyterNotebookの後継ソフトにあたるJupyterLabにマルチユーザアカウント機能(Hub)を導入したJupyter環境を提供するソフトウェアです。
デフォルトでは Linux の PAM認証を利用してユーザ認証を実行します。

設定は全て`jupyterhub_config.py`で管理します。

## jupyterhub_config.pyとは

JupyterHub の設定を管理するコンフィグファイルのことです。
なお、`jupyterhub_config.py`という名前はjupyterhub コマンドでコンフィグを作成した時にデフォルトで設定される名前です。

`jupyterhub_config.py`の書き方一つでいろんな設定をJupyterHubに設定できます。

## jupyterhub_config.py の設定項目集

設定はPythonで定義します。文法はインストールしたメインのインタプリタに依存します。

## c.JupyterHub

### c.JupyterHub.base_url

アクセス時のログインパスを設定できます。ドメインから後ろの文字列に相当する文字列を指定します。

書き方の例

```py
c.JupyterHub.base_url = '/'
```

### c.JupyterHub.authenticator_class

アクセス時の認証クラスをしています。`dummy`に設定すると登録されていないユーザ名およびパスワードでなくても
JupyterHubにログインできるようになります。

※専ら検証用の設定項目になるかと思います。

書き方の例

```py
c.JupyterHub.authenticator_class = "dummy"
```

### c.JupyterHub.spawner_class

JupyterHub で利用するスポナークラスを設定します。
JupyterHub で利用するスポナーとはnotebookサーバを起動する際のプログラムです。

書き方の例(JupyterHubコンテナでDockerSpawnerを使う場合)

```py
c.JupyterHub.spawner_class = "docker"
```

### c.JupyterHub.hub_ip

サーバをJupyterHubサーバとしてリッスンする時に設定する項目です。
リッスンする時のIPアドレスを設定します。

書き方の例

```py
c.JupyterHub.hub_ip = '*'
```

もしくは

```py
c.JupyterHub.hub_ip = '0.0.0.0'
```

### c.JupyterHub.port

サーバをJupyterHubサーバとしてリッスンする時に設定する項目です。
リッスンする時のポート番号を設定します。
なお、httpsで接続する場合は`443`で指定します。

書き方の例

```py
c.JupyterHub.port=443
```

### c.JupyterHub.tornado_settings

JupyterHubにアクセスする時のレスポンスヘッダを定義します。
tornadoはPythonのフレームワークのことであり、Webサーバのことでもあります。
JupyterHubにはこのtornadoを設定する項目が存在します。

書き方の例

インラインフレームにJupyterHubを組み込みたい時の設定です。

```py
c.JupyterHub.tornado_settings = {
  'headers': {
    'Content-Security-Policy': 'frame-ancestors * any' ,
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods':'*',
    'Access-Control-Allow-Headers':'*',
    'Access-Control-Allow-Credentials':'true'
  }
}
```

### c.JupyterHub.open_browser

```py
c.JupyterHub.open_browser = False
```

## c.Spawner

### c.Spawner.notebook_dir

Spawnerによって起動された`jupyter notebook`のディレクトリを設定するときの項目です。
notebookの起動URLを設定する項目、`c.Spawner.default_url`と同時に設定することが多いです。

書き方の例

```py
user_path = '/home/.{username}/notebooks'
c.Spawner.notebook_dir = user_path
c.Spawner.default_url = user_path
```

### c.Spawner.cpu_limit

起動されたnotebookサーバが使用するCPU使用率を制限します。
指定はfloat型の数値で設定します。

書き方の例

```py
## 10%に設定する
c.Spawner.cpu_limit=0.1
```

なお、2と設定した場合は2つのCPUを使用できます。

### c.Spawner.cpu_guarantee

一定のCPU使用率を保証する設定です。

書き方の例

```py
c.Spawner.cpu_guarantee=0.1
```

### c.Spawner.mem_limit

スポナーで起動したサーバで使用するメモリーサイズを制限します。

書き方の例

```py
c.Spawner.mem_limit="128M"
```

### c.Spawner.mem_guarantee

一定のメモリサイズを保証する設定です。

書き方の例

```py
c.Spawner.mem_guarantee="128M"
```

## c.Authenticator

### c.Authenticator.admin_users

JupyterHubの管理ユーザを`Authenticator`に設定します。

```py
c.Authenticator.admin_users = {'jupyter'}
```

## c.PAMAuthenticator

### c.PAMAuthenticator.admin_groups

JupyterHubの管理ユーザを`PAMAuthenticator`に設定します。

```py
c.PAMAuthenticator.admin_groups = {'wheel'}
```

## c.LocalAuthenticator

### c.LocalAuthenticator.create_system_users

```py
c.LocalAuthenticator.create_system_users=True
```

### c.LocalAuthenticator.add_user_cmd

```py
# ユーザ作成
c.LocalAuthenticator.add_user_cmd = ['./add_user.sh']
```

## AWSでJupyter環境を使う場合

AWSでJupyter環境を使う場合はEC2やECSで構築しても良いですが、AWSではフルマネージドで環境を提供してくれる `Sagemaker` というものがあります。
分析作業に集中したい場合は活用すると良いでしょう。

特に複数人でさらにAWSアカウントで組織管理できる場合は後述の`Sagemaker Studio`を活用すると良いです。

### Sagemaker Studio を使う

Sagemakerをマルチユーザで扱えるようにしたAWSの分析サービスの一つです。
AWS IAM Identity Center(AWS SSO)に接続することでログインユーザを管理できます。

## おわり
