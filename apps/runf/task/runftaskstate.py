from copy import deepcopy

from apps.core.task.coretaskstate import (TaskDefinition,
                                          TaskDefaults, Options)
from apps.runf.runfenvironment import RunFEnvironment


class RunFDefaults(TaskDefaults):
    def __init__(self):
        super().__init__()
        self.options = RunFOptions()


class RunFDefinition(TaskDefinition):
    def __init__(self, defaults=None):
        super().__init__()
        self.options = RunFOptions()
        self.task_type = "RUNF"
        self.args = []
        self.kwargs = {}
        self.function = b''

        if defaults:
            self.set_defaults(defaults)

    # TODO maybe move it to the CoreTask? Issue #2428
    def set_defaults(self, defaults: RunFDefaults):
        self.options = deepcopy(defaults.options)


class RunFOptions(Options):
    def __init__(self):
        super().__init__()
        self.environment = RunFEnvironment()
        self.args = []
        self.kwargs = {}
        self.function = b''