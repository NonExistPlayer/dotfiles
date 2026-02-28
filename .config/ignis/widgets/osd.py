from ignis import utils

from ignis.widgets import Box, Icon, Label, Window
from ignis.services.audio import AudioService

from options import Options


class OnScreenDisplay(Window):
    __gtype_name__ = "OnScreenDisplay"

    def __init__(self):
        audioservice = AudioService.get_default()

        self.timeout = None

        icon = Icon(image=audioservice.speaker.bind("icon_name"))
        label = Label(
            label=audioservice.speaker.bind(
                "volume", lambda x: f"Volume: {x}%"),
            width_request=100,
        )

        super().__init__(
            namespace="shell-osd",
            anchor=["bottom"],
            margin_bottom=50,
            layer="overlay",
            css_classes=["osd-window"],
            visible=False,
            child=Box(
                css_classes=["osd"],
                child=[icon, label],
                spacing=10,
            ),
        )

        def changed(*_):
            self.set_visible(True)

            if self.timeout:
                self.timeout.cancel()

            self.timeout = utils.Timeout(
                ms=Options.OnScreenDisplay.popuptimeout,
                target=lambda: self.set_visible(False),
            )

        audioservice.speaker.connect("notify::volume", changed)
        audioservice.speaker.connect("notify::is-muted", changed)
