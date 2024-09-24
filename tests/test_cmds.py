from pymembercli import cmds


class TestCmds:
    def test_add_tasks(self):
        tasks = []
        cmds.add_task(name="i am a test task", desc="it's true!", tasks=tasks)
        assert tasks[0].name == "i am a test task"
        assert tasks[0].desc == "it's true!"

    def test_del_tasks_id(self):
        tasks = []
        cmds.add_task(name="i am a test task", desc="it's true!", tasks=tasks)
        tasks = cmds.del_task_by_id(taskids=[0,], tasks=tasks)
        assert not tasks

    def test_del_tasks_grp(self):
        tasks = []
        cmds.add_task(name="i am a test task", desc="it's true!", tasks=tasks)
        tasks = cmds.del_task_by_grp(taskset='todo', tasks=tasks)
        assert len(tasks) == 0

    def test_set_task(self):
        tasks = []
        cmds.add_task(name="i am a test task", desc="it's true!", tasks=tasks)
        cmds.set_task(taskids=[0,], group='doing', tasks=tasks)
        assert tasks[0].status == 'doing'
