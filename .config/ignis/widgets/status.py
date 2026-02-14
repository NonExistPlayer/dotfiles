from ignis.options import options

from ignis.widgets import Box, Icon, Label, Button
from ignis.window_manager import WindowManager
from ignis.services.niri import NiriService
from ignis.services.network import NetworkService
from ignis.services.hyprland import HyprlandService
from ignis.services.notifications import NotificationService


class StatusBar(Button):
    __gtype_name__ = "StatusBar"

    def __init__(self):
        netservice = NetworkService.get_default()
        winmanager = WindowManager.get_default()
        nservice = NotificationService.get_default()
        hyprservice = HyprlandService.get_default()
        niriservice = NiriService.get_default()

        keylayout = Label()

        if hyprservice.is_available:
            keyboard = hyprservice.main_keyboard

            # if the keylayouts less than 2, then hide
            if len(keyboard.layout.split(",")) < 2:
                keylayout.set_visible(False)
            else:
                keylayout.set_label(keyboard.bind(
                    "active_keymap", lambda k: k[0:2]))
                keylayout.set_tooltip_text(keyboard.bind("active_keymap"))
        elif niriservice.is_available:
            keylayouts = niriservice.keyboard_layouts

            # if the keylayouts less than 2, then hide
            if len(keylayouts.names) < 2:
                keylayout.set_visible(False)
            else:
                keylayout.set_label(keylayouts.bind(
                    "current_name"), lambda k: k[0:2])
                keylayout.set_tooltip_text(keylayouts.bind("current_name"))
        else:
            keylayout.set_visible(False)

        ethernet_icon = Icon(
            image=netservice.ethernet.bind("icon_name"),
            visible=netservice.ethernet.bind("is_connected"),
        )
        vpn_icon = Icon(
            image=netservice.vpn.bind("icon_name"),
            visible=netservice.vpn.bind("is_connected"),
        )
        self.notification_icon = Icon(
            image="preferences-system-notifications-symbolic",
        )

        def dnd_changed():
            if options.notifications.dnd:
                self.notification_icon.add_css_class("dnd")
                self.notification_icon.remove_css_class("notified")
            else:
                self.notification_icon.remove_css_class("dnd")

        options.notifications.connect_option("dnd", dnd_changed)

        def notifications_changed(s, _):
            if len(s.popups) > 0 and not options.notifications.dnd:
                self.notification_icon.add_css_class("notified")
            else:
                self.notification_icon.remove_css_class("notified")

        nservice.connect("notify::notifications", notifications_changed)

        box = Box(
            spacing=15,
            child=[
                keylayout,
                Icon(image=netservice.wifi.bind("icon_name")),
                ethernet_icon,
                vpn_icon,
                self.notification_icon,
            ],
        )

        super().__init__(
            css_classes=["status-bar"],
            child=box,
            on_click=lambda _: winmanager.toggle_window(
                "shell-control-center"),
        )
