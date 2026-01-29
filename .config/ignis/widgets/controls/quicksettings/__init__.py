from ignis.widgets import Grid

from .wifi import WifiButton
from .bluetooth import BluetoothButton


class QuickSettings(Grid):
    def __init__(self):
        wifi = WifiButton()

        bluetooth = BluetoothButton()

        super().__init__(
            css_classes=["quick-settings"],
            column_num=2,
            column_homogeneous=True,
            row_homogeneous=True,
            column_spacing=10,
            row_spacing=10,
            child=[wifi, bluetooth],
        )
