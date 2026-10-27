from task import Task
from task_manager import TaskManager


def test_add_task_to_empty_manager():
    manager = TaskManager([])

    created = manager.add_task("復習する")

    assert created.task_id == 1
    assert created.title == "復習する"
    assert created.completed is False
    assert manager.tasks == [created]


def test_new_id_uses_largest_existing_id():
    original = Task(5, "コードを読む")
    manager = TaskManager([original, Task(2, "ノートを書く")])

    created = manager.add_task("テストを書く")

    assert created.task_id == 6
    assert len(manager.tasks) == 3
    assert manager.tasks[0] is original
    assert original.title == "コードを読む"


# TODO: 完了処理、対象外のタスク、存在しないID、再度の完了をテストする。
