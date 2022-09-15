# jupyter_k8s

## helm とは

Kubernetes 用のパッケージマネージャーです。

## config.yaml　とは

helm 起動時に必要な[Valuesファイル](https://helm.sh/docs/chart_template_guide/values_files/)
以下のようにyaml形式で書く。

```yml
proxy:
  secretToken: "8799038e67923a9368d1716fb648f9dc9c76810641abba3e9f2dc1651f6f3acd"
  https:
    enabled: false
```

なお、secretToken は `$(openssl rand -hex 32)` を実行して取得できるランダムな文字列

## helm で JupyterHubを使う準備

```bash
helm repo add jupyterhub https://jupyterhub.github.io/helm-chart/
```

## k8s で JupyterHub を起動

```bash
RELEASE=jhub
NAMESPACE=jhub
```

JupyterHubを起動してみる。

```bash
helm upgrade --cleanup-on-fail \
  --install $RELEASE jupyterhub/jupyterhub \
  --namespace $NAMESPACE \
  --create-namespace \
  --version=1.2 \
  --values config.yaml

```

## Pod を確認する

```bash
kubectl get pods -n jhub
```

## Pod を削除する

```bash
kubectl delete pods jupyterhub/k8s-hub:1.2.0
```

## その他

```bash
kubectl get pods --all-namespaces -o jsonpath='{range .items[*]}{"\n"}{.metadata.name}{":\t"}{range .spec.containers[*]}{.image}{", "}{end}{end}' |\
sort

```
