from ignis.services.network import NetworkService

from .qsbutton import QuickSettingsButton
from gi.repository import GObject


class WifiButton(QuickSettingsButton):
    def __init__(self):
        netservice = NetworkService.get_default()
        netdevice = netservice.wifi.devices[0]

        def icon_name(state):
            match state:
                # Wi-Fi disabled
                case "unavailable":
                    return "network-wireless-disabled-symbolic"

                # enabled but not connected
                case "disconnected":
                    return "network-wireless-offline-symbolic"

                # connection avaliable
                case "activated":
                    return netdevice.ap.bind("icon_name")

                # auth needed
                case "need_auth":
                    return "network-wireless-no-route-symbolic"

                # something weird
                case "unknown" | "unmanaged" | "failed":
                    return "network-wireless-hardware-disabled-symbolic"

                # waiting...
                case "prepare" | "config" | "ip_config" | "ip_check" | "secondaries":
                    return "network-wireless-acquiring-symbolic"

        super().__init__(
            "Wi-Fi",
            subtitle=netdevice.ap.bind("ssid"),
            icon_name=netdevice.bind("state", icon_name),
            active=netservice.wifi.enabled,  # fix visual bug
        )

        netservice.wifi.bind_property(
            "enabled",  # source property
            self,  # target
            "active",  # target property
            # flags; two-way binding
            GObject.BindingFlags.BIDIRECTIONAL,
            lambda _, value: value,  # transform to
            lambda _, value: bool(value),  # transform from
        )
