# 価格コムクローラー

## 環境構築(Windows)

1. python3.9をインストール

サイトからダウンロードする場合

https://www.python.org/downloads/windows/

2. pipenvをインストール

pipの場合

```shell
pip install --upgrade pip
pip install pipenv
```

3. pipenvからライブラリをインストール

```shell
pipenv install
```

## 実行方法

```shell
pipenv run crawler
```

同じフォルダにCSVで出力される。