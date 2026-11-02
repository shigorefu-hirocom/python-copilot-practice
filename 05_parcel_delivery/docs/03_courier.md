# 実習3 配達員を割り当てる

実習2を完成させてから開始します。1人の配達員が複数の荷物を担当できるようにして、オブジェクト間の関係を表します。

## 完成条件

- courier.pyに`Courier(courier_id: str, name: str)`を作ります。
- Parcelに`courier_id: str | None`を追加し、初期値をNoneにします。
- `DeliveryService(parcels, couriers=None)`に拡張します。省略時は空の配達員一覧とし、既存の呼び出しも動くようにします。IDは重複しない文字列とします。
- `get_courier(courier_id) -> Courier`は元のオブジェクトを返します。不明なIDは`ValueError("配達員が見つかりません")`です。
- `assign_courier(tracking_number, courier_id) -> None`で担当IDを設定します。先に荷物、次に配達員を取得し、両方が存在してから割り当て可能か確認します。
- 配達完了前の荷物に割り当てます。完了済みなら`ValueError("配達完了の荷物には割り当てできません")`です。
- 同じ配達員への再割り当ては成功として扱います。完了前なら別の配達員への変更も可能です。
- 割り当ては配送状態と履歴を変更しません。エラー時には担当も変更しません。配達完了後も担当IDを保持します。
- `get_courier_parcels(courier_id) -> list[Parcel]`は担当荷物を元の順序・同じオブジェクトで返します。完了済みも含め、担当なしは`[]`。先に配達員の存在を確認します。
- couriersを省略した従来の発送・配達も動きます。担当者の有無を発送の追加条件にしません。

変更対象はcourier.py、parcel.py、delivery_service.py、data.py、main.py、tests/です。data.pyに`create_couriers()`を追加し、C01 田中とC02 佐藤を用意します。

mainでは最初にP002とP003をC01へ割り当て、従来のP001のデモは維持します。最後にC01の担当荷物の追跡番号を取得して表示します。

```text
担当荷物: C01
P002
P003
```

## 確認と依頼

1人に複数の荷物、別の配達員、再割り当て、不明なID、両IDが不明な場合のエラー優先順、完了済み、失敗時の状態・履歴・担当の保存をテストします。

```text
実習3を読んで、ParcelとCourierをIDで関連付ける計画を説明してください。
既存のDeliveryService(parcels)も動く設計にしてください。
今はファイルを変更しないでください。
```

計画確認後に実装し、既存テストも含めて検証します。
