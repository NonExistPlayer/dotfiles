from ignis.widgets import Box, RevealerWindow, Revealer

from .actionbar import ActionBar
from .quicksettings import QuickSettings
from .notifications import Notifications

from options import Options


class ControlCenter(RevealerWindow):
    __gtype_name__ = "ControlCenter"

    def __init__(self):
        quicksettings = QuickSettings()
        notifications = Notifications()
        actionbar = ActionBar()

        revealer = Revealer(
            transition_type=Options.Animations.ControlCenter.type,
            transition_duration=Options.Animations.ControlCenter.duration,
            child=Box(
                css_classes=["control-center"],
                child=[quicksettings, notifications, actionbar],
                spacing=20,
                vertical=True,
            ),
        )

        super().__init__(
            namespace="shell-control-center",
            monitor=0,
            anchor=["top", "bottom", "right"],
            revealer=revealer,
            visible=False,
            popup=True,
            layer="top",
            child=Box(child=[revealer]),
        )

        # avoid importing in the module to avoid getting circular import
        from config import shell_bar

        self.connect(
            "show", lambda _: shell_bar.status.add_css_class(
                "suggested-action")
        )
        self.connect(
            "hide", lambda _: shell_bar.status.remove_css_class(
                "suggested-action")
        )
