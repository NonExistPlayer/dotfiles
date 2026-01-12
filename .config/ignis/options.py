import os
from ignis.options_manager import OptionsManager, OptionsGroup


class Options(OptionsManager):
    def __init__(self):
        super().__init__(file=os.path.expanduser("~/.config/ignis/options"))

    class Clock(OptionsGroup):
        showseconds: bool = False
        format: str = "%H:%M" + (":%S" if showseconds else "")
