from datetime import datetime
from ignis import utils
from ignis.widgets import Label
from options import Options


class Clock(Label):
    __gtype_name__ = "Clock"

    def __init__(self):
        super().__init__(css_classes=["clock"])
        utils.Poll(1000, lambda x: self.update())

    def update(self):
        self.set_label(datetime.now().strftime(Options.Clock.format))
