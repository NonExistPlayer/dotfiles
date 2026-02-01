import asyncio
from ignis import utils
from ignis.widgets import Entry


class Launcher(Entry):
    def __init__(self):
        super().__init__(
            placeholder_text="Type something here...",
            width_chars=40,
            xalign=0.5,
            css_classes=["launcher"],
            on_accept=lambda e: asyncio.create_task(Launcher.__on_accept(e)),
        )

    async def __on_accept(e) -> None:
        text = e.text
        e.set_text("")
        await utils.exec_sh_async(text)
