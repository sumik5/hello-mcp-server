# Hello MCP Server

シンプルなMCP (Model Context Protocol) サーバーの実装例です。

## 概要

このプロジェクトは、MCPサーバーの基本的な実装を示すサンプルです。`hello`ツールを提供し、名前を受け取って挨拶メッセージを返します。

## 必要条件

- Python 3.13以上
- mise (開発環境管理ツール)
- uv (Pythonパッケージマネージャー)

## セットアップ

```bash
# miseで開発環境をセットアップ
mise install

# 依存関係のインストール
mise run install
```

## 使用方法

### サーバーの起動

```bash
# miseタスクでサーバーを起動
mise run start

# または直接実行
uv run --no-dev python hello_server.py

# 環境変数でトランスポートを指定
MCP_TRANSPORT=stdio uv run --no-dev python hello_server.py
```

## miseタスク

利用可能なmiseタスク：

```bash
# 依存関係のインストール
mise run install

# サーバーの起動
mise run start

# Dockerイメージのビルド
mise run docker-build

# Dockerコンテナの実行
mise run docker-run

# プロジェクトのクリーンアップ
mise run clean

# 依存関係のロック
mise run lock
```

## Docker

Dockerコンテナとして実行する場合：

```bash
# miseタスクを使用
mise run docker-build
mise run docker-run

# または直接実行
docker build -t hello-mcp-server:latest .
docker run --rm -p 8000:8000 hello-mcp-server:latest
```
