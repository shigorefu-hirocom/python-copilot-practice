from parcel import Parcel
from delivery_service import DeliveryService
from report import build_report


def test_report_returns_text_without_changing_status():
    parcel = Parcel("P001", "田中")
    parcel.dispatch()
    assert build_report(DeliveryService([parcel])) == "荷物一覧:\nP001: 田中 [配送中]"
    assert parcel.status == "配送中"


def test_report_for_empty_service():
    assert build_report(DeliveryService([])) == "荷物一覧:"
