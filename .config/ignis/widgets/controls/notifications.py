import os

from ignis.widgets import Box, Label, Scroll, Button
from ignis.services.notifications import Notification, NotificationService

from gi.repository import Gtk


class Notifications(Scroll):
    __gtype_name__ = "Notifications"

    def __init__(self):
        service = NotificationService.get_default()

        service.connect("notified", lambda _,
                        n: self.box.append(NotificationWidget(n)))

        self.box = Box(
            css_classes=["notifications"],
            orientation="vertical",
            spacing=10,
        )

        super().__init__(
            child=self.box,
            vexpand=True,
        )


class NotificationWidget(Box):
    __gtype_name__ = "Notification"

    def _closed(self, _):
        self.unparent()
        self.set_visible(False)

    def __init__(self, notification: Notification):
        notification = notification

        app_box = Box(css_classes=["app-box"], hexpand=True, spacing=8)

        icon = None
        name = Label(
            label=notification.app_name,
            hexpand=True,
            halign="start",
        )

        if notification.icon:
            if os.path.exists(notification.icon):
                icon = Gtk.Image.new_from_file(notification.icon)
            else:
                icon = Gtk.Image.new_from_icon_name(notification.icon)

            app_box.append(icon)

        app_box.append(name)

        title = Label(
            css_classes=["title"],
            label=notification.summary,
            halign="start",
        )
        body = Label(css_classes=["body"],
                     label=notification.body, halign="start")
        close = Button(
            css_classes=["close", "flat"],
            icon_name="window-close-symbolic",
            on_click=lambda _: notification.close(),
        )
        app_box.append(close)

        action_box = Box(hexpand=True, homogeneous=True, spacing=6)

        for action in notification.actions:
            action_box.append(
                Button(
                    css_classes=["action-button"],
                    label=action.label,
                    on_click=lambda _: action.invoke(),
                )
            )

        super().__init__(
            css_classes=["notification"],
            orientation="vertical",
            child=[
                app_box,
                title,
                body,
                action_box,
            ],
        )

        notification.connect("closed", self._closed)
