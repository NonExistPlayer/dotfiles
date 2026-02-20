<div align="center">

**English** | [Русский](./docs/ru/CONTRIBUTING.md)

</div>

# Contributor's Guide
Thank you for your interest in the project!

## Overview

| Software | Documentation                                      | Repository Link                   |
| -------- | -------------------------------------------------- | --------------------------------- |
| Hyprland | https://wiki.hypr.land                             | [link](`./config/hypr/hyprland.conf`) |
| Kitty    | https://sw.kovidgoyal.net/kitty/conf/              | [link](`./config/kitty/kitty.conf`)   |
| Ignis    | https://ignis-sh.github.io/ignis/latest/index.html | [link](`./config/ignis/`)             |

### Hyprland
The Hyprland config is divided into smaller configs for better structure and simplicity.

These files also use special styling. Headers are written as:
```conf
###
### Title
###

##
## Smaller title
##

# just comment
```

Similar to [callouts in GitHub Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#alerts),
the config has similar comments:

```conf
# -- Link -------------------------------------+
# https://wiki.hypr.land/Configuring/Keywords/ |
# ---------------------------------------------+

# (!) Note -------------+
# Please note something |
# ----------------------+
```

### Ignis

##### Structure
```
.config/ignis
├── config.py           # Main file
├── options.py          # Settings [TODO]
├── style.scss          # Styles
└── widgets             # Widgets
    ├── controls/       # Control Center
    ├── clock.py        # Clock widget
    ├── ...
    └── workspaces.py   # Workspaces widget
```

##### Basic Commands
- **Run `ignis init` directly from the console**, it's useful for viewing logs
- `ignis inspector` for the **Gtk inspector**

## Language Requirements
The following rules apply to all code/configuration:

- **All code/configuration must be in English**
- **All user-visible text must be in English**

## Documentation
Documentation refers to informational `.md` files in this repository.

- **Documentation is available in two languages: English (priority) and Russian**
- **When making changes, verify that the documentation remains accurate**
- **Translate to other languages**

## Contact
If you have questions or suggestions, please open an issue.

Thank you for contributing!
