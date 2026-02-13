from ignis.options import options

from ignis.widgets import Box, Icon, Button
from ignis.window_manager import WindowManager
from ignis.services.network import NetworkService
from ignis.services.notifications import NotificationService


class StatusBar(Button):
    __gtype_name__ = "StatusBar"

    def __init__(self):
        self.netservice = NetworkService.get_default()
        self.winmanager = WindowManager.get_default()
        self.nservice = NotificationService.get_default()

        self.ethernet_icon = Icon(
            image=self.netservice.ethernet.bind("icon_name"),
            visible=self.netservice.ethernet.bind("is_connected"),
        )
        self.vpn_icon = Icon(
            image=self.netservice.vpn.bind("icon_name"),
            visible=self.netservice.vpn.bind("is_connected"),
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

        self.nservice.connect("notify::notifications", notifications_changed)

        box = Box(
            spacing=15,
            child=[
                Icon(image=self.netservice.wifi.bind("icon_name")),
                self.ethernet_icon,
                self.vpn_icon,
                self.notification_icon,
            ],
        )

        super().__init__(
            css_classes=["status-bar"],
            child=box,
            on_click=lambda _: self.winmanager.toggle_window(
                "shell-control-center"),
        )
