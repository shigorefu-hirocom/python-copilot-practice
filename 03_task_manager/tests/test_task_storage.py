import json

from task import Task
from task_storage import load_tasks, save_tasks


def test_save_and_load_unfinished_task(tmp_path):
    filename = str(tmp_path / "tasks.json")
    tasks = [Task(3, "日本語の課題を読む")]

    save_tasks(filename, tasks)
    restored = load_tasks(filename)

    assert len(restored) == 1
    assert restored[0].task_id == 3
    assert restored[0].title == "日本語の課題を読む"
    assert restored[0].completed is False
    assert restored[0] is not tasks[0]


def test_save_and_load_empty_list(tmp_path):
    filename = str(tmp_path / "tasks.json")

    save_tasks(filename, [])
    restored = load_tasks(filename)
    with open(filename, encoding="utf-8") as file:
        stored = json.load(file)

    assert stored == []
    assert restored == []


# TODO: 完了したタスクを保存し、読み直しても完了状態が残ることを確認する。
