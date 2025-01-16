# ベースイメージを指定（軽量のPythonイメージを使用）
FROM python:3.10-slim

# 作業ディレクトリを作成
WORKDIR /app

# 必要なファイルをコンテナにコピー
COPY requirements.txt requirements.txt
COPY . .

# 必要な依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリを実行
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
