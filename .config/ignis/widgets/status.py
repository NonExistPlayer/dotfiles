from ignis.widgets import Box, Button
from ignis.services.network import NetworkService


class StatusBar(Box):
    def __init__(self):
        self.netservice = NetworkService.get_default()

        super().__init__(css_classes=["status-bar"])

        self.append(Button(icon_name=self.netservice.wifi.bind("icon_name")))

        if self.netservice.ethernet.is_connected:
            self.append(
                Button(icon_name=self.netservice.ethernet.bind("icon_name")))
