from ignis.widgets import Box, Label, ToggleButton
from ignis.gobject import IgnisProperty

from gi.repository import Gtk


class QuickSettingsButton(ToggleButton):
    def __init__(self, title: str, **kwargs):
        self._subtitle = ""
        self._icon_name = ""

        self._subtitle_label = Label(
            css_classes=["subtitle"],
            label=self._subtitle,
            ellipsize="middle",
        )
        self._image = Gtk.Image.new_from_icon_name(self._icon_name)

        hbox = Box(spacing=16)

        vbox = Box(
            orientation="vertical",
            child=[
                Label(
                    css_classes=["title"],
                    label=title,
                ),
                self._subtitle_label,
            ],
            hexpand=True,
            spacing=8,
        )

        super().__init__(css_classes=["pill"], **kwargs)
        self.set_size_request(180, 40)

        hbox.append(self._image)
        hbox.append(vbox)

        self.set_child(hbox)

    @IgnisProperty
    def subtitle(self):
        return self._subtitle

    @subtitle.setter
    def subtitle(self, value):
        self._subtitle_label.set_label(value)
        self._subtitle = value

    @IgnisProperty
    def icon_name(self):
        return self._icon_name

    @icon_name.setter
    def icon_name(self, value):
        self._image.set_from_icon_name(value)
        self._icon_name = value
