from ignis import utils
from ignis.options import options
from ignis.widgets import Box, CenterBox, Button, ToggleButton

from .cbutton import ConfirmButton


class ActionBar(CenterBox):
    def __init__(self):
        settings_button = Button(  # placeholder
            css_classes=["circular"],
            icon_name="view-more-horizontal-symbolic",
            tooltip_text="Settings",
        )

        def dnd_toggled(active):
            options.notifications.dnd = active

        dnd_button = ToggleButton(
            css_classes=["circular"],
            icon_name="notifications-disabled-symbolic",
            active=options.notifications.bind("dnd"),
            on_toggled=lambda b, _: dnd_toggled(b.active),
            tooltip_text="Do Not Distrub",
        )
        clear_button = Button(  # placeholder
            css_classes=["circular"],
            icon_name="edit-clear-all-symbolic",
            tooltip_text="Clear Notifications",
        )

        tool_box = Box(
            css_classes=["toolbox"],
            spacing=5,
            child=[
                settings_button,
                dnd_button,
                clear_button,
            ],
        )

        power_button = ConfirmButton(
            css_classes=["shutdown", "circular"],
            icon_name="system-shutdown-symbolic",
            # on_confirmed=lambda: utils.exec_sh("shutdown now"),
            on_confirmed=lambda: utils.exec_sh(
                "hyprctl notify 3 1000 0 SHUTDOWN"),
            tooltip_text="Shutdown",
        )
        reboot_button = ConfirmButton(
            css_classes=["reboot", "circular"],
            icon_name="system-reboot-symbolic",
            # on_confirmed=lambda: utils.exec_sh("reboot"),
            on_confirmed=lambda: utils.exec_sh(
                "hyprctl notify 0 1000 0 REBOOT"),
            tooltip_text="Reboot",
        )
        power_box = Box(
            halign="end",
            spacing=5,
            child=[
                power_button,
                reboot_button,
            ],
        )

        super().__init__(
            css_classes=["action-bar"],
            start_widget=tool_box,
            end_widget=power_box,
        )
