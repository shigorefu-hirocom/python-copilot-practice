import json

from task import Task


def load_tasks(filename: str) -> list[Task]:
    with open(filename, encoding="utf-8") as file:
        records = json.load(file)
    # TODO: 保存した完了状態も復元する。
    return [Task(row["id"], row["title"]) for row in records]


def save_tasks(filename: str, tasks: list[Task]) -> None:
    # TODO: 完了状態も保存する。
    records = [{"id": task.task_id, "title": task.title} for task in tasks]
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(records, file, ensure_ascii=False, indent=2)
