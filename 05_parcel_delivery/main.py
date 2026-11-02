from data import create_parcels
from delivery_service import DeliveryService
from report import build_report


def main() -> None:
    service = DeliveryService(create_parcels())
    service.dispatch_parcel("P001")
    print(build_report(service))
    service.deliver_parcel("P001")
    print("\n配達後:")
    print(build_report(service))
    # TODO: 実習1でaliceの検索結果を表示する。


if __name__ == "__main__":
    main()
