import pytest
from parcel import Parcel


def test_dispatch_then_deliver_changes_status():
    parcel = Parcel("P001", "田中")
    assert parcel.status == "受付済み"
    parcel.dispatch()
    assert parcel.status == "配送中"
    parcel.deliver()
    assert parcel.status == "配達完了"


def test_delivery_before_dispatch_preserves_status():
    parcel = Parcel("P001", "田中")
    with pytest.raises(ValueError, match="^配達できない状態です$"):
        parcel.deliver()
    assert parcel.status == "受付済み"


def test_repeated_dispatch_preserves_status():
    parcel = Parcel("P001", "田中")
    parcel.dispatch()
    with pytest.raises(ValueError, match="^発送できない状態です$"):
        parcel.dispatch()
    assert parcel.status == "配送中"


def test_repeated_delivery_preserves_status():
    parcel = Parcel("P001", "田中")
    parcel.dispatch()
    parcel.deliver()
    with pytest.raises(ValueError, match="^配達できない状態です$"):
        parcel.deliver()
    assert parcel.status == "配達完了"
