from ignis.widgets import Box, Button
from ignis.services.hyprland import HyprlandService
from ignis.services.niri import NiriService


class Workspaces(Box):
    __gtype_name__ = "Workspaces"

    def __init__(self):
        if HyprlandService.is_available:
            service = HyprlandService.get_default()
        elif NiriService.is_available:
            service = NiriService.get_default()
        else:
            return

        # FIXME: Niri no workspaces
        service.connect("notify::workspaces", lambda s,
                        _: self.update(s.workspaces))

        super().__init__(css_classes=["workspaces"], spacing=6)

    def update(self, workspaces) -> None:
        def makebutton(w):
            return Button(
                label=str(w.id),
                on_click=lambda x: w.switch_to(),
            )

        self.child = [makebutton(w) for w in workspaces]
