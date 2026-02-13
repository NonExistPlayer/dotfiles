import os
from ignis.options_manager import OptionsManager, OptionsGroup


class Options(OptionsManager):
    def __init__(self):
        super().__init__(file=os.path.expanduser("~/.config/ignis/options"))

    class Animations(OptionsGroup):
        class Launcher(OptionsGroup):
            type: str = "SLIDE_UP"
            duration: int = 100

        class ControlCenter(OptionsGroup):
            type: str = "SLIDE_LEFT"
            duration: int = 100

    class Clock(OptionsGroup):
        showseconds: bool = False
        format: str = "%H:%M" + (":%S" if showseconds else "")
