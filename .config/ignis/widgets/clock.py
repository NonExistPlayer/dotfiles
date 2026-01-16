from datetime import datetime
from ignis.utils import Utils
from ignis.widgets import Widget
from options import Options


class Clock(Widget.Label):
    def __init__(self):
        super().__init__(css_classes=["clock"])
        Utils.Poll(1000, lambda x: self.update())

    def update(self):
        self.set_label(datetime.now().strftime(Options.Clock.format))
