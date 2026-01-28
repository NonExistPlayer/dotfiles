import asyncio
from ignis.widgets import Box, Button
from ignis.services.system_tray import SystemTrayService
from gi.repository import Gtk, GdkPixbuf


class SystemTray(Box):
    def __init__(self):
        self.trayservice = SystemTrayService.get_default()
        self.trayservice.connect(
            "notify::items", lambda s, _: self._update_tray(s.items)
        )

        super().__init__(
            css_classes=["system-tray"],
            spacing=20,
        )

    def _update_tray(self, items):
        for item in items:
            button = Button(
                tooltip_text=item.tooltip,
                on_click=lambda _: asyncio.create_task(item.activate_async()),
                on_right_click=lambda _: asyncio.create_task(
                    item.secondary_activate_async()
                ),
            )
            if isinstance(item.icon, str):
                button.set_icon_name(item.bind("icon"))
            elif isinstance(item.icon, GdkPixbuf.Pixbuf):
                button.set_image(Gtk.Image.new_from_pixbuf(item.bind("icon")))
            else:
                continue

            self.append(button)
