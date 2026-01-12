# Only Hyprland support
from ignis.widgets import Widget
from ignis.services.hyprland import HyprlandService


class Workspaces(Widget.Box):
    def __init__(self):
        self.hyprland = HyprlandService.get_default()

        def connected(_, workspace):
            workspace.connect(
                "destroyed", lambda _: self.update())
            self.update()

        self.hyprland.connect("workspace_added", connected)

        super().__init__()

        self.update()

    def update(self) -> None:
        def makebutton(w):
            return Widget.Button(label=str(w.id),
                                 on_click=lambda x: w.switch_to())
        self.child = [makebutton(w) for w in self.hyprland.workspaces]
