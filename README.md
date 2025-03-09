# gRPC Python-Rust サンプルプロジェクト

Rust で書かれた gRPC サーバーと、Python および Go で書かれたクライアントの実装例です。

## プロジェクト構成

```
project/
├── proto/                 # Protocol Buffers 定義ファイル
│   └── test.proto
├── rust-server/           # Rust サーバー実装
│   ├── Cargo.toml
│   ├── build.rs
│   └── src/
│       └── main.rs
└── python-client/         # Python クライアント実装
    ├── client.py          # コマンドラインクライアント
    └── streamlit_app.py   # Streamlit UIクライアント
```

## 機能

- ユーザー情報（名前、メール、パスワード）をリクエストとして送信
- サーバーは受け取った情報にタイムスタンプを追加してレスポンスを返す
- 複数の言語（Python、Go）からのアクセスをサポート
- Streamlitによる簡易的なWeb UI

## 環境構築

### 1. Rust サーバー

```bash
cd rust-server
cargo build
```

### 2. Python クライアント

```bash
cd python-client
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 依存パッケージのインストール
pip install grpcio grpcio-tools
pip install streamlit  # Streamlit UIを使用する場合

# .proto ファイルからPythonコードを生成
python -m grpc_tools.protoc -I../proto --python_out=. --grpc_python_out=. ../proto/test.proto
```

## 実行方法

### 1. サーバーの起動

```bash
cd rust-server
cargo run
```

サーバーは `127.0.0.1:50051` でリッスンします。

### 2. Python コマンドラインクライアントの実行

```bash
cd python-client
python client.py
```

### 3. Streamlit UI クライアントの実行

```bash
cd python-client
streamlit run ui.py
```

ブラウザが自動的に開き、Streamlit アプリケーションが表示されます。

## 注意事項

- このサンプルでは、セキュリティのための TLS/SSL は実装していません。本番環境では暗号化された接続を使用してください。
- 実際のアプリケーションではパスワードをそのまま送受信すべきではありません。ハッシュ化などのセキュリティ対策を実装してください。
- IPv4 アドレス（127.0.0.1）を使用しています。IPv6 を使用する場合は、サーバーとクライアントの両方を対応するよう変更してください。

## トラブルシューティング

### 「Cannot invoke RPC on closed channel」エラー

クライアント側で以下のエラーが発生する場合：

```
ValueError: Cannot invoke RPC on closed channel!
```

以下の対処方法を試してください：

1. サーバーが実行されていることを確認
2. クライアントコードでIPv6（[::1]）ではなくIPv4（127.0.0.1）を使用
3. ファイアウォールの設定を確認
4. 接続前に少し待機時間を入れる（例：`time.sleep(1)`）
