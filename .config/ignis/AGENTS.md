# AI Instructions for Ignis Configuration

## Language Requirements
- **All code comments must be in English** - ensures consistency for future contributors
- **All UI text and user-facing strings must be in English** - improves accessibility and internationalization  
- **All public documentation must be in English** - follows GitHub and OSS conventions
- Internal developer notes can be in any language, but prefer English for clarity

**Why:** Mixed languages in code reduce maintainability and make it harder for international developers to contribute. English is the standard for open-source projects.

---

## Project Context
- **Framework:** Ignis (https://github.com/ignis-sh/ignis) - a GTK-based shell widget toolkit
- **GTK Python Bindings:** https://lazka.github.io/pgi-docs/
- **Language:** Python with GTK widgets
- **Purpose:** Custom shell/bar configuration with custom widgets
- **Location:** `.dotfiles/.config/ignis`

**Why:** Understanding the framework helps write idiomatic code and avoid anti-patterns specific to GTK/Ignis.

---

## Code Standards

### No hard code
- **Never** use the absolute path to a file (e.g.: `/home/user/.config/ignis/style.scss`).
  Use `os.path.expanduser("~/.config/ignis/style.scss")`
- You **can** use a "hardcode" for widgets and/or UI. (e.g.: `Label(label="hardcoded text")`)

**Why:** The hardcode is "tied to a specific machine, which prevents other users from using the shell.

### Add new settings
- It is recommended for some widgets options to add configurable settings to the `options.py`. Example:
```python
# widgets/clock.py
class Clock(Label):
    ...

    def update(self):
        self.set_label(datetime.now().strftime("%H:%S")) # hardcode

        self.set_label(datetime.now().strftime(Options.Clock.format)) # user can configure

# options.py
class Options(OptionsManager):
    ...
    class Clock(OptionsGroup):
        showseconds: bool = False
        format: str = "%H:%M" + (":%S" if showseconds else "")
```
- Add a new group for each widget or groups of widgets.

**Why:** Adding new settings will allow the user to customize the shell more.

### Widget Development
- It is preferable to use code (methods, classes, widgets) from Ignis. Ignis widgets inherit from their Gtk counterparts.
- Create widgets using classes and inheritance. Example: `class Bar(Window): ...`
- Keep widgets modular and reusable
- Use GTK CSS classes for styling (in `style.scss`) instead of inline styles
- Use lambda for: simple property updates, single expressions
- Use method for: multiple operations
- Always prefix methods with `_`: `self._callback` (indicates internal use)
- Always bind callbacks explicitly: `on_accept=self._callback` not lambda with side effects
- For each new widget, set `__gtype_name__` so that the widget has a readable name in the Gtk inspector.

**Why:** Maintains consistency with Ignis architecture.

### Error Handling
- Ignis doesn't crash on exceptions, but unhandled errors cause widget malfunction
- If the exception breaks the shell (for example: the window does not open, the shell does not start, the widget has incorrect behavior),
  then investigate the error, if it is an error in the code - fix it,
  if it is a situational error in the runtime (for example: incorrect user input) - add an exception handler.
- Always check your code for potential algorithmic errors, exceptions, and security issues. 

**Why:** Prevents crashes, unexpected behavior, safety problems.

---

## File Structure
```
/home/nonex/.dotfiles/.config/ignis/
├── config.py              # Configuration file, entry point
├── options.py             # Settings/options, constants
├── style.scss             # GTK CSS styling (variables and theme)
├── widgets/               # Custom widget modules
│   ├── controls/          # Control center widgets
│   │   └── quicksettings/ # Quick settings widgets
│   ├── launcher.py        # App launcher
│   ├── clock.py           # Time display widget
│   ├── status.py          # Status indicators
│   └── ...
└── README.ru.md           # README file about the project (in russian)
```

**Why:** Understanding structure helps place new code in correct locations and avoid circular imports.

---

## Common Patterns & Best Practices

### Async Operations
- Use `utils.Timeout()` for delayed callbacks (not `asyncio.call_later()`)
- Use `utils.exec_sh_async()` for shell commands that shouldn't block UI
- Store timeout handles to allow cancellation of previous operations

**Why:** Ignis provides higher-level abstractions better integrated with GTK event loop. Raw asyncio can cause issues.

### Timeout Handling
```python
# Correct pattern
self.timeout = None  # Store at instance level

def _show_message(self, text: str, time: int = 5000) -> None:
    if self.timeout:
        self.timeout.cancel()
    
    # ... update UI ...
    
    def on_timeout():
        # Cleanup logic
        self.timeout = None
    
    self.timeout = utils.Timeout(ms=time, target=on_timeout)
```

**Why:** Prevents multiple simultaneous timers and ensures proper cleanup.

---

## README Editing/Translating
- There are only two languages for translating the README: English `README.md` and Russian `README.ru.md` (original).
- After changing the README, **be sure to indicate at the end of the file** that the *file was modified/translated by AI and checked by the developer*.
- Add links to the file **if you mention it** using the relative path. (e.g. `[launcher.py](./widgets/launcher.py)`)
- Also add links if you mention the title in this file.
- Check that the links are valid.
- Check that the information is valid.
- You **can** add emojis to your titles or text.
- When changing one of the READMEs, remember to change/translate the other.

Use this list as a checklist to check if the README has been modified correctly.

---

## Checklist for Code Changes

Before submitting changes:
- [ ] All comments and strings are in English
- [ ] Code follows existing patterns in the directory
- [ ] No hardcoded values that should be configurable
- [ ] Timeout/async operations properly managed
- [ ] No new external dependencies added without good reason
- [ ] Check the README and edit if necessary.
