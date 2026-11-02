# 荷物管理システム — Copilot共同実習

小さな配送会社の荷物管理プログラムを、先生と一緒にGitHub Copilotで拡張します。追跡番号で荷物を識別し、受取人と配送状態を管理します。Visual Studio CodeとPyCharmのどちらを使っても構いません。Python 3.10以上とGitHub Copilotを使用します。

## 準備と起動

このREADMEがあるフォルダーをプロジェクトとして開き、Python環境を選択します。ターミナルの作業フォルダーも同じ場所にします。

```bash
python -m pip install -r requirements.txt
python main.py
python -m pytest -q
```

配布時は9件のテストが成功します。検索は未実装です。既存テストの成功は、実習の完成を意味しません。GUI、JSON保存、外部API、対話メニューは使用しません。データは起動するたびに作り直します。

## ファイルと読む順序

| 順序 | ファイル | 内容 |
| --- | --- | --- |
| 1 | main.py | 発送と配達のデモ |
| 2 | parcel.py | 追跡番号、受取人、状態と状態変更 |
| 3 | delivery_service.py | 番号による取得、発送、配達、検索の枠 |
| 4 | report.py | 一覧と検索結果の文字列 |
| 5 | data.py | 5件の初期データ |
| 6 | tests/ | 既存の動作を確認するテスト |

`Parcel`の属性は`tracking_number: str`、`recipient: str`、`status: str`です。初期状態は`受付済み`です。`dispatch()`で`配送中`、`deliver()`で`配達完了`になります。順序を飛ばした操作や繰り返しはValueErrorになり、状態は変わりません。

`DeliveryService.get_parcel()`は追跡番号が完全一致する元のParcelを返します。不明な番号は`ValueError("荷物が見つかりません")`です。追跡番号は重複しない文字列、受取人は文字列とします。
