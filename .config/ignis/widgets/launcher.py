import subprocess
from ignis.widgets import Entry


class Launcher(Entry):
    __gtype_name__ = "AppLauncher"

    def __init__(self):
        super().__init__(
            placeholder_text="Type something here...",
            width_chars=40,
            xalign=0.5,
            css_classes=["launcher"],
            on_accept=Launcher._on_accept,
        )

    def _on_accept(e) -> None:
        text = e.text
        from config import shell_bar

        shell_bar._toggle_launcher()
        subprocess.Popen(
            text,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
