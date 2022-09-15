
# JupyterHub をFargate で起動する

## JupyterHub のクラスターを作成

beta-jupyterhub-cluster

## notebook のクラスターを作成する

beta-jupyter-notebooks-cluster

## JupyterHub のイメージをpush

ECRのプライベートリポジトリ`jupyterhub` を構築する。

{account_id}.dkr.ecr.us-east-2.amazonaws.com/jupyterhub:1

## notebookのイメージをpush

ECRのプライベートリポジトリ`notebooks` を構築する。

{account_id}.dkr.ecr.us-east-2.amazonaws.com/notebooks:1

## JupyterHubのタスクロールを作成

JupyterHubRole

## JupyterHub のタスク定義を作成

jupyterhub

## notebookのタスク定義を作成

jupyterhub-notebook
