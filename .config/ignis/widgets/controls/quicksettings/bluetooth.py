from ignis.services.bluetooth import BluetoothService
from ignis.exceptions import GnomeBluetoothNotFoundError

from .qsbutton import QuickSettingsButton

from gi.repository import GObject


class BluetoothButton(QuickSettingsButton):
    def __init__(self):
        try:
            blueservice = BluetoothService.get_default()
        except GnomeBluetoothNotFoundError:
            super().__init__(
                "Bluetooth",
                subtitle="Library missing",
                icon_name="bluetooth-hardware-disabled-symbolic",
            )
            return

        def icon_name(state):
            match state:
                case "absent":
                    return "bluetooth-hardware-disabled-symbolic"
                case "on":
                    return "bluetooth-symbolic"
                case "off":
                    return "bluetooth-disabled-symbolic"
                case "turning-on" | "turning-off":
                    return "bluetooth-acquiring-symbolic"

        super().__init__(
            "Bluetooth",
            icon_name=blueservice.bind("state", icon_name),
        )

        blueservice.bind_property(
            "powered",  # source property
            self,  # target
            "active",  # target property
            # flags; two-way binding
            GObject.BindingFlags.BIDIRECTIONAL,
            lambda _, value: value,  # transform to
            lambda _, value: bool(value),  # transform from
        )

        def new_device(s, _):
            length = len(s.connected_devices)
            if length < 1:
                self.subtitle = ""
                return

            if length > 1:
                self.subtitle = f"{length} devices"
            else:
                self.subtitle = s.connected_devices[0].bind("alias")

        blueservice.connect("notify::connected-devices", new_device)
