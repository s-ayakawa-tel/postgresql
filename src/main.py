import psycopg2


def main():

    # PostgreSQL接続情報（各自の環境に合わせて設定してください）
    conn_params = {
        "host": "10.146.11.69",  # PostgreSQLサーバのIPアドレス
        "port": 5432,
        "dbname": "wine_db",
        "user": "postgres",
        "password": "postgres",
    }

    try:
        # データベースに接続
        conn = psycopg2.connect(**conn_params)
        conn.set_client_encoding("UTF8")  # DBのエンコーディングに合わせてUTF8に設定
        cur = conn.cursor()

        # テーブルからデータを取得（例: 最初の5件）
        cur.execute("SELECT * FROM wine LIMIT 5;")
        rows = cur.fetchall()

        for row in rows:
            # 各カラムがbytes型の場合はデコード、そうでなければそのまま表示
            safe_row = []
            for col in row:
                if isinstance(col, bytes):
                    try:
                        safe_row.append(col.decode("utf-8", errors="replace"))
                    except Exception:
                        safe_row.append(str(col))
                else:
                    safe_row.append(col)
            print(safe_row)

        cur.close()
        conn.close()

    except Exception as e:
        print("接続またはクエリ実行でエラーが発生しました:", e)


if __name__ == "__main__":
    main()
