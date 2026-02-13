# Only Hyprland support
from ignis.widgets import Box, Button
from ignis.services.hyprland import HyprlandService
from ignis.services.niri import NiriService


class Workspaces(Box):
    __gtype_name__ = "Workspaces"

    def __init__(self):
        _hyprserv = HyprlandService.get_default()
        _niriserv = NiriService.get_default()

        if _hyprserv.is_available:
            service = _hyprserv
        elif _niriserv.is_available:
            service = _niriserv
        else:
            return

        service.connect("notify::workspaces", lambda s,
                        _: self.update(s.workspaces))

        super().__init__(css_classes=["workspaces"], spacing=6)

    def update(self, workspaces) -> None:
        def makebutton(w):
            # noqa: START
            return Button(
                label=str(w.id),
                on_click=lambda x: w.switch_to(),
            )
            # noqa: END

        self.child = [makebutton(w) for w in workspaces]
