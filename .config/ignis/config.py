from ignis.widgets import Widget
from widgets.clock import Clock
from widgets.workspaces import Workspaces


class Bar(Widget.Window):
    def __init__(self):
        clock = Clock()
        workspaces = Workspaces()

        left = Widget.Box(
            child=[workspaces]
        )
        mid = Widget.Box(
            halign="center",
            child=[clock]
        )
        right = Widget.Box(
            halign="end",
            child=[]
        )

        super().__init__(
            namespace="shell-bar",
            monitor=0,
            anchor=["left", "right", "bottom"],
            exclusivity="exclusive",
            height_request=35,
            child=Widget.CenterBox(
                start_widget=left,
                center_widget=mid,
                end_widget=right
            )
        )


Bar()
