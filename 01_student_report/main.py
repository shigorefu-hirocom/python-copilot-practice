from data import create_classroom
from report import build_report


def main() -> None:
    classroom = create_classroom()
    report = build_report(classroom)
    if report is None:
        print("レポートは未実装です。READMEを確認してください。")
    else:
        print(report)


if __name__ == "__main__":
    main()
