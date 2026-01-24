import gi
import os
from ignis.app import IgnisApp
from ignis.widgets import Widget

from widgets.clock import Clock
from widgets.workspaces import Workspaces
from widgets.launcher import Launcher

gi.require_version("Adw", "1")
from gi.repository import Adw  # noqa: E402
from gi.repository import Gtk, Gdk  # noqa: E402


Adw.init()

app = IgnisApp.get_default()
app.apply_css(os.path.expanduser("~/.config/ignis/style.scss"))

key_controller = Gtk.EventControllerKey()


def handle_key_press(
    event_controller_key: Gtk.EventControllerKey,
    keyval: int,
    keycode: int,
    state: Gdk.ModifierType,
) -> None:
    if keyval == 65515:  # super key
        shell_bar._toggle_launcher()


key_controller.connect("key-released", handle_key_press)


class Bar(Widget.Window):
    def __init__(self):
        self.clock = Clock()
        self.workspaces = Workspaces()
        self.launcher = Launcher()

        self.left_widgets = Widget.Box(child=[self.workspaces])
        self.center_widgets = Widget.Box(halign="center", child=[self.clock])
        self.right_widgets = Widget.Box(halign="end", child=[])

        self._toggled = False

        super().__init__(
            namespace="shell-bar",
            monitor=0,
            anchor=["left", "right", "bottom"],
            exclusivity="exclusive",
            kb_mode="on_demand",  # for launcher; do not set to 'exclusive'
            height_request=35,
            child=Widget.CenterBox(
                start_widget=self.left_widgets,
                center_widget=self.center_widgets,
                end_widget=self.right_widgets,
            ),
        )

        self.add_controller(key_controller)

    def _toggle_launcher(self):
        if self._toggled:
            self.center_widgets.child = [self.clock]
        else:
            self.center_widgets.child = [self.launcher]
        self._toggled = not self._toggled


shell_bar = Bar()
