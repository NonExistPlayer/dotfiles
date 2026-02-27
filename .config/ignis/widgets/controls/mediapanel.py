from ignis.widgets import Box, Label, Picture, Calendar
from ignis.services.mpris import MprisService, MprisPlayer

from gi.repository import Gio, Adw


class MediaPanel(Box):
    __gtype_name__ = "MediaPanel"

    def __init__(self):
        stack = Adw.ViewStack()
        switcher = Adw.ViewSwitcher(stack=stack)

        stack.add_titled_with_icon(
            Calendar(), "cal", "Calendar", "view-grid-symbolic")
        #   Widget,      ID,     Title,    Icon
        stack.add_titled_with_icon(
            MediaView(), "mpris", "MPRIS", "audio-x-generic-symbolic"
        )

        super().__init__(
            child=[switcher, stack],
            spacing=10,
            vertical=True,
        )


class MediaView(Box):
    __gtype_name__ = "MediaView"

    def __init__(self):
        mprisserv = MprisService.get_default()
        stack = Adw.ViewStack()
        switcher = Adw.InlineViewSwitcher(
            stack=stack,
            valign="center",
            orientation="vertical",
            display_mode="icons",
        )

        stack.get_pages().connect(
            "items-changed",
            lambda *_: switcher.set_visible(
                stack.get_pages().get_n_items() > 1),
        )

        super().__init__(child=[switcher, stack], spacing=10)

        def add(p: MprisPlayer):
            desktop = Gio.DesktopAppInfo.new(p.desktop_entry + ".desktop")
            desktop_icon = desktop.get_icon()
            icon_name = (
                desktop_icon.get_names()[0]
                if desktop_icon
                else "multimedia-volume-control-symbolic"
            )
            player_widget = MediaView.Player(p, icon_name)
            stack.add_titled_with_icon(
                player_widget, None, p.identity, icon_name)

            p.connect("closed", lambda _: stack.remove(player_widget))

        mprisserv.connect(
            "player_added",
            lambda _, p: add(p),
        )

    class Player(Box):
        __gtype_name__ = "PlayerView"

        def __init__(self, player: MprisPlayer, icon):
            self.icon = None

            self.icon = Picture(
                content_fit="scale_down",
                image=player.bind("art_url", lambda x: x or icon),
                width=96,
                height=96,
            )

            title = Label(
                css_classes=["title"],
                label=player.bind("title"),
                ellipsize="end",
            )
            author = Label(
                css_classes=["author"],
                label=player.bind("artist"),
                ellipsize="middle",
            )

            box = Box(
                child=[title, author],
                valign="center",
                vertical=True,
            )

            super().__init__(
                child=[self.icon, box],
                spacing=20,
            )

            player.connect("closed", lambda _: self.set_visible(False))
