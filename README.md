<div align="center">

**English** | [Русский](./docs/ru/README.md)

</div>

<div align="center">
  <h1><code>nnx's dotfiles</code></h1>
  <p>These are my dotfiles, containing my environment configuration.</p>
  <p>I hope you like it, I tried my best!</p>
</div>

# Requirements

## Included Software
This is a list of applications from the dotfiles themselves. **Not all of them are mandatory to install**, but
they are part of the shell. Recommended applications are highlighted in **bold**.

- **Hyprland**<br>
  Tiling Wayland compositor.
- **Ignis**<br>
  Framework for creating desktop shells.
  **Install GIT-version**
- Kitty<br>
  Cool terminal emulator.

## Required Software
This is a small list of software/libraries. Required programs are highlighted in **bold**.

- **Git**<br>
  Version control system. **Required for installation**.<br>
  *However, you can download the dotfiles directly from GitHub, although that would be pointless.*
- **GNU Stow**<br>
  Organizes all important (user) configuration in one directory (usually `~/.dotfiles`).<br>
  Automatically creates links from this directory to the home directory.
  **Required for installation**.<br>
  *As with Git, you can create symbolic links manually.*

It's also recommended to check out the [Ignis requirements](./.config/ignis/README.md#Usage)
(if you plan to use it).

# Installation
> [!WARNING]
> Installation is manual only; automatic installation is **not planned**!
> These dotfiles were created only for personal use
> and for those with experience configuring their Linux distribution.

1. Clone the git repository to `~/.dotfiles` (you can choose any name)
```
git clone https://github.com/nonexistplayer/dotfiles ~/.dotfiles
```

2. Navigate to `~/.dotfiles` and create links using `stow`
```
cd ~/.dotfiles
stow .
```
This will create symbolic links in `~/.config`.

3. Reboot your system or (re)start Hyprland.

4. Enjoy.

> [!TIP]
> See shell's [README](../../.config/ignis/README.ru.md).

# License

This project is licensed under the [MIT License](./LICENSE).

Copyright © 2026 Ilya Korobov
