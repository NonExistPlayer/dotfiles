from ignis.widgets import Box, Icon, Button
from ignis.window_manager import WindowManager
from ignis.services.network import NetworkService


class StatusBar(Button):
    __gtype_name__ = "StatusBar"

    def __init__(self):
        self.netservice = NetworkService.get_default()
        self.winmanager = WindowManager.get_default()

        self.ethernet_icon = Icon(
            image=self.netservice.ethernet.bind("icon_name"),
            visible=self.netservice.ethernet.bind("is_connected"),
        )
        self.vpn_icon = Icon(
            image=self.netservice.vpn.bind("icon_name"),
            visible=self.netservice.vpn.bind("is_connected"),
        )

        box = Box(spacing=15)

        super().__init__(
            css_classes=["status-bar"],
            child=box,
            on_click=lambda _: self.winmanager.toggle_window(
                "shell-control-center"),
        )

        box.append(Icon(image=self.netservice.wifi.bind("icon_name")))
        box.append(self.ethernet_icon)
        box.append(self.vpn_icon)
