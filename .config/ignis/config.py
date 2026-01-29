import gi
import os
from ignis import utils
from ignis.css_manager import CssManager, CssInfoPath
from ignis.widgets import Window, Box, CenterBox, Stack

from widgets.clock import Clock
from widgets.workspaces import Workspaces
from widgets.launcher import Launcher
from widgets.tray import SystemTray
from widgets.status import StatusBar
from widgets.controls import ControlCenter

gi.require_version("Adw", "1")
from gi.repository import Adw  # noqa: E402
from gi.repository import Gtk, Gdk  # noqa: E402


# Setup Adwaita
Adw.init()

# Setup css styles
css_manager = CssManager.get_default()

css_manager.apply_css(
    CssInfoPath(
        name="main",
        path=os.path.expanduser("~/.config/ignis/style.scss"),
        compiler_function=lambda path: utils.sass_compile(path=path),
    )
)

# Setup key bindings
key_controller = Gtk.EventControllerKey()


def handle_key_press(
    event_controller_key: Gtk.EventControllerKey,
    keyval: int,
    keycode: int,
    state: Gdk.ModifierType,
) -> None:
    if shell_bar.center_widgets.visible_child_name == "launcher":
        if keyval == Gdk.KEY_Escape:
            shell_bar._toggle_launcher()
    else:
        char = chr(keyval)
        if char.isalpha():
            shell_bar._toggle_launcher()
            shell_bar.launcher.text += char
            shell_bar.launcher.set_position(1)


key_controller.connect("key-released", handle_key_press)


class Bar(Window):
    def __init__(self):
        self.clock = Clock()
        self.workspaces = Workspaces()
        self.launcher = Launcher()
        self.tray = SystemTray()
        self.status = StatusBar()

        self.left_widgets = Box(
            css_classes=["left-widgets"], child=[self.workspaces])
        self.center_widgets = Stack(css_classes=["center-widgets"])
        self.right_widgets = Box(
            css_classes=["right-widgets"],
            halign="end",
            spacing=15,
            child=[self.tray, self.status],
        )

        self.center_widgets.set_transition_type("SLIDE_UP")
        self.center_widgets.set_transition_duration(100)
        self.center_widgets.add_named(self.clock, "clock")
        self.center_widgets.add_named(self.launcher, "launcher")

        super().__init__(
            namespace="shell-bar",
            monitor=0,
            anchor=["left", "right", "bottom"],
            exclusivity="exclusive",
            kb_mode="on_demand",  # for launcher; do not set to 'exclusive'
            height_request=35,
            child=CenterBox(
                start_widget=self.left_widgets,
                center_widget=self.center_widgets,
                end_widget=self.right_widgets,
            ),
        )

        self.add_controller(key_controller)

    def _toggle_launcher(self):
        visible = self.center_widgets.visible_child_name
        next = "launcher" if visible == "clock" else "clock"
        self.center_widgets.set_visible_child_name(next)

        if next == "launcher":
            self.launcher.grab_focus()
        else:
            self.launcher.set_text("")


# Starting
shell_bar = Bar()
ControlCenter()
