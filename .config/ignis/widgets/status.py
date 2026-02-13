from ignis.options import options

from ignis.widgets import Box, Icon, Button
from ignis.window_manager import WindowManager
from ignis.services.network import NetworkService
from ignis.services.notifications import NotificationService


class StatusBar(Button):
    __gtype_name__ = "StatusBar"

    def __init__(self):
        netservice = NetworkService.get_default()
        winmanager = WindowManager.get_default()
        nservice = NotificationService.get_default()

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
