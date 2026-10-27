class Task:
    def __init__(self, task_id: int, title: str, completed: bool = False):
        self.task_id = task_id
        self.title = title
        self.completed = completed

    def complete(self) -> None:
        # TODO: 完了状態に変更する。
        pass
