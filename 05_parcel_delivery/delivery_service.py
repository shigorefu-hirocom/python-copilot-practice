from parcel import Parcel


class DeliveryService:
    def __init__(self, parcels: list[Parcel]):
        self.parcels = list(parcels)

    def get_parcel(self, tracking_number: str) -> Parcel:
        for parcel in self.parcels:
            if parcel.tracking_number == tracking_number:
                return parcel
        raise ValueError("荷物が見つかりません")

    def dispatch_parcel(self, tracking_number: str) -> None:
        self.get_parcel(tracking_number).dispatch()

    def deliver_parcel(self, tracking_number: str) -> None:
        self.get_parcel(tracking_number).deliver()

    def search_parcels(self, keyword: str) -> list[Parcel]:
        # TODO: 実習1の仕様に従って検索する。
        pass
