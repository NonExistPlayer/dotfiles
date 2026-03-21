<div align="center">

**English** | [Русский](README.ru.md)

</div>

<div align="center">
  <h1>My Shell</h1>
  Magic happens here!
</div>

These are the files of my shell, written in [Ignis](https://github.com/ignis-sh/ignis).

Huge thanks to [linkfrg](https://github.com/linkfrg) for the [framework](https://github.com/ignis-sh/ignis) and the [reference](https://github.com/linkfrg/dotfiles) for the shell.

> [!IMPORTANT]
> The shell **does not depend** on other configurations in this repository.
> **Except:** `../hypr/hyprland/ignis.conf` (for Hyprland) and
> `../niri/ignis.kdl` (for niri; **optional**).<br>
> Those files is responsible for
> configuring compositor for Ignis (mainly hotkeys).

## Usage

**Requirements**:
- **Hyprland** / Niri (not tested)<br>
  > It's possible to run on any Wayland compositor
  > (with Layer Shell protocol support), but the
  > [workspace](./widgets/workspaces.py) widget depends on Hyprland / Niri.
  > In this case, widget will be hidden.
- **Ignis**<br>
  Currently Ignis is not releasing updates, which means
  for new features you **need** to use the `git` version.
  
  For more precise information, see
  [the official documentation](https://ignis-sh.github.io/ignis/latest/user/installation.html) from Ignis.
  ##### Arch Linux
  Regular installation via AUR.
  ```
  yay -S python-ignis-git
  ```
  Or if you use `paru`.
  ```
  paru -S python-ignis-git
  ```
  ##### Pip
  ```
  pip install git+https://github.com/ignis-sh/ignis.git
  ```
- **SASS Compiler**<br>
  Install `dart-sass` or `grass-sass`.
  Without it, Ignis will throw a `SassNotFoundError`.
- **`ignis-gvc`**<br>
  [`ignis-gvc`](https://github.com/ignis-sh/ignis-gvc) is used for audio handling in Ignis.
- `gnome-bluetooth-3.0` *(optional)*<br>
  Ignis uses this library for Bluetooth support.
  The shell will be able to start, but Bluetooth won't work.

## Installation
To install, simply place these files in `~/.config/ignis/` and install all dependencies.

To run the shell, type in the console (or in your Hyprland configuration) `ignis init`.

## Styling
All styles are located in the `style.scss` file. You can style it **however you like**.

To find out what CSS classes a widget has, open the GTK inspector with the command `ignis inspector`.

## FAQ / Troubleshooting

### Q: "Why Ignis specifically?"

The main reason for using Ignis is GTK 4 (for libadwaita).
For a more detailed comparison, see [this issue](https://github.com/ignis-sh/ignis/issues/58) from the Ignis repository.

### Q: "Why is AI being used?"

GitHub Copilot is used for the shell to: simplify tasks, assist in development/explanations,
code review, documentation translation (across the repository), etc.

**No vibe-coding whatsoever!**

### Q: "How to shutdown/reboot/suspend computer?"

Open control center in the shell, you will see three buttons.
To take action, press two times on a button, with the small delay.
This is done to protect against accidental clicks.

> Suspend button, depend on `systemctl`.
> If you are not using systemd, then edit
> the command in shell settings.

### I: "Ignis or the control center is not displayed"

Run Ignis from the console to view the log: `ignis init`,
after closing Ignis with the command `ignis quit` (even if it's not displayed).

Then check the output. An error should be displayed.
Report the error by opening an [issue](https://github.com/NonExistPlayer/dotfiles/issues/new/choose).
**Make sure the error is not related to your changes or environment.**

### I: "Ignis closed"

> Ignis does not exit on its own. If a Python error occurs, Ignis
> continues to run and automatically restarts when code changes.

Check the Ignis log as described above.

Based on my experience, it's most likely a `Segmentation fault`.
It occurs on the C side of libraries used by Ignis (Gtk, NM).

In this case, open an issue as shown above.

### I: "Bluetooth error: 'Library missing'"

Simply install the `gnome-bluetooth-3` library from the dependencies above.

### I: `SassNotFoundError`

Install one of the SASS compilers: `dart-sass` or `grass-sass`.
