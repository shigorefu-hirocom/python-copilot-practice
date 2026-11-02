from delivery_service import DeliveryService


def build_report(service: DeliveryService) -> str:
    lines = ["荷物一覧:"]
    for parcel in service.parcels:
        lines.append(f"{parcel.tracking_number}: {parcel.recipient} [{parcel.status}]")
    return "\n".join(lines)


def build_search_report(service: DeliveryService, keyword: str) -> str:
    # TODO: 実習1で検索結果の文字列を返す。
    pass
