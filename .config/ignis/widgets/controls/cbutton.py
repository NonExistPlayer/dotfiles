from ignis import utils
from ignis.widgets import Button
from ignis.gobject import IgnisProperty


class ConfirmButton(Button):
    def _on_clicked(self, _):
        if self.get_await_confirm():
            self.set_await_confirm(False)

            self._on_confirmed()
        else:
            self.set_await_confirm(True)

            self.set_sensitive(False)
            utils.Timeout(ms=800, target=lambda: self.set_sensitive(True))

    def __init__(self, **kwargs):
        self._await_confirm = False
        self._on_confirmed = None
        self.timeout = None

        super().__init__(**kwargs)

        self.connect("clicked", self._on_clicked)

    @IgnisProperty
    def await_confirm(self):
        return self._await_confirm

    @await_confirm.setter
    def await_confirm(self, value):
        print(value)
        self._await_confirm = value
        if value:
            self.child.add_css_class("confirm")
            self.timeout = utils.Timeout(
                ms=5000, target=lambda: self.set_await_confirm(False)
            )
        else:
            self.child.remove_css_class("confirm")
            if self.timeout.ms > 0:
                self.timeout.cancel()

    @IgnisProperty
    def on_confirmed(self):
        return self._on_confirmed

    @on_confirmed.setter
    def on_confirmed(self, value):
        self._on_confirmed = value
