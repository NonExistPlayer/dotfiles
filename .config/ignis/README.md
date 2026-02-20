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
> **Except:** `../hypr/hyprland/ignis.conf`. This file is responsible for
> configuring Hyprland for Ignis (mainly hotkeys).

## Usage

**Requirements**:
- **Hyprland** / Niri (not tested)<br>
  > Technically it's possible to run on any Wayland compositor
  > (with Layer Shell protocol support), but the
  > [workspace](./widgets/workspaces.py) widget depends on Hyprland.
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
