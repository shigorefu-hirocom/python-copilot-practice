import pytest
from parcel import Parcel
from delivery_service import DeliveryService


def test_get_parcel_returns_same_object():
    parcel = Parcel("P001", "田中")
    assert DeliveryService([parcel]).get_parcel("P001") is parcel


def test_delivery_does_not_change_other_parcel():
    first, second = Parcel("P001", "田中"), Parcel("P002", "Alice")
    service = DeliveryService([first, second])
    service.dispatch_parcel("P001")
    service.deliver_parcel("P001")
    assert first.status == "配達完了"
    assert second.status == "受付済み"


def test_unknown_tracking_number_preserves_data():
    parcel = Parcel("P001", "田中")
    service = DeliveryService([parcel])
    with pytest.raises(ValueError, match="^荷物が見つかりません$"):
        service.dispatch_parcel("UNKNOWN")
    assert service.parcels == [parcel]
    assert parcel.status == "受付済み"
