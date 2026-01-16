import gi
import os
from ignis.app import IgnisApp
from ignis.widgets import Widget
from widgets.clock import Clock
from widgets.workspaces import Workspaces

gi.require_version("Adw", "1")
from gi.repository import Adw  # noqa: E402


Adw.init()

app = IgnisApp.get_default()
app.apply_css(os.path.expanduser("~/.config/ignis/style.scss"))


class Bar(Widget.Window):
    def __init__(self):
        clock = Clock()
        workspaces = Workspaces()

        left = Widget.Box(child=[workspaces])
        mid = Widget.Box(halign="center", child=[clock])
        right = Widget.Box(halign="end", child=[])

        super().__init__(
            namespace="shell-bar",
            monitor=0,
            anchor=["left", "right", "bottom"],
            exclusivity="exclusive",
            height_request=35,
            child=Widget.CenterBox(
                start_widget=left, center_widget=mid, end_widget=right
            ),
        )


Bar()
