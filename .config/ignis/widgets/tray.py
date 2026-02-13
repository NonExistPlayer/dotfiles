import asyncio
from ignis.widgets import Box, Icon, Button
from ignis.services.system_tray import SystemTrayService


class SystemTray(Box):
    __gtype_name__ = "SystemTray"

    def __init__(self):
        service = SystemTrayService()

        service.connect("added", lambda _, t: self.append(TrayItem(t)))

        super().__init__(
            css_classes=["system-tray"],
            spacing=10,
        )


class TrayItem(Button):
    __gtype_name__ = "SystemTrayItem"

    def __init__(self, item):
        super().__init__(
            css_classes=["system-tray-item", "flat"],
            tooltip_text=item.tooltip,
            on_click=lambda _: asyncio.create_task(item.activate_async()),
            on_right_click=lambda _: item.menu.popup() if item.menu else None,
            child=Box(
                child=[
                    Icon(image=item.bind("icon")),
                    item.menu,
                ]
            ),
        )

        def removed(_):
            self.unparent()
            self.set_visible(False)

        item.connect("removed", removed)
