# Only Hyprland support
from ignis.widgets import Box, Button
from ignis.services.hyprland import HyprlandService


class Workspaces(Box):
    __gtype_name__ = "HyprlandWorkspaces"

    def __init__(self):
        self.hyprland = HyprlandService.get_default()

        self.hyprland.connect(
            "notify::workspaces", lambda s, _: self.update(s.workspaces)
        )

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
