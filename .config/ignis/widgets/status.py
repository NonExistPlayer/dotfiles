from ignis.widgets import Box, Icon, Button
from ignis.window_manager import WindowManager
from ignis.services.network import NetworkService


class StatusBar(Button):
    def __init__(self):
        self.netservice = NetworkService.get_default()
        self.winmanager = WindowManager.get_default()

        box = Box(spacing=15)

        super().__init__(
            css_classes=["status-bar"],
            child=box,
            on_click=lambda _: self.winmanager.toggle_window(
                "shell-control-center"),
        )

        box.append(Icon(image=self.netservice.wifi.bind("icon_name")))

        if self.netservice.ethernet.is_connected:
            box.append(
                Icon(
                    image=self.netservice.ethernet.bind("icon_name"),
                )
            )
