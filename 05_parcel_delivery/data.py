from parcel import Parcel


def create_parcels() -> list[Parcel]:
    return [
        Parcel("P001", "田中"),
        Parcel("P002", "Alice"),
        Parcel("P003", "ALICE Suzuki"),
        Parcel("P004", "佐藤"),
        Parcel("P005", "Bob"),
    ]
