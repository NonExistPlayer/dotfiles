<div align="center">

[English](README.md) | **Русский**

</div>

<div align="center">
  <h1>Моя оболочка</h1>
  Здесь творяться чудеса!
</div>

Это файлы моей оболочки, написанной на [Ignis](https://github.com/ignis-sh/ignis).

Огромное спасибо [linkfrg](https://github.com/linkfrg) за [фреймворк](https://github.com/ignis-sh/ignis) и за [референс](https://github.com/linkfrg/dotfiles) для оболочки.

> [!IMPORTANT]
> Оболочка **не зависит** от других конфигов в этом репозитории.
> **Кроме:** `../hypr/hyprland/ignis.conf`. Этот файл отвечает,
> за настройку Hyprland под Ignis (в основном горячие клавиши).

## Использование

**Требования**:
- **Hyprland** / Niri (не тестируется)<br>
  > Возможно запустить на любом Wayland-композиторе
  > (с поддержкой Layer Shell protocol), но виджет
  > [workspace](./widgets/workspaces.py) зависит от Hyprland / Niri.<br>
  > В таком случае, виджет не появиться.
- **Ignis**<br>
  На данный момент Ignis не выпускает обновлений, из-за чего
  для новых возможностей **нужно** использовать `git`-версию.
  
  Для более точной информации смотрите
  [на официальной документации](https://ignis-sh.github.io/ignis/latest/user/installation.html) от Ignis.
  ##### Arch Linux
  Обычная установка через AUR.
  ```
  yay -S python-ignis-git
  ```
  Или если используете `paru`.
  ```
  paru -S python-ignis-git
  ```
  ##### Pip
  ```
  pip install git+https://github.com/ignis-sh/ignis.git
  ```
- **Компилятор SASS**<br>
  Установите `dart-sass` или `grass-sass`.
  Без него, Ignis будет выдавать ошибку `SassNotFoundError`.
- **`ignis-gvc`**<br>
  [`ignis-gvc`](https://github.com/ignis-sh/ignis-gvc) используется для работы со звуком в Ignis.
- `gnome-bluetooth-3.0` *(опицонально)*<br>
  Для работы Bluetooth, Ignis использует эту библиотеку.
  Оболочка сможет запуститься, но Bluetooth не будет работать.

## Установка
Для установки достаточно поместить эти файлы в `~/.config/ignis/` и установить все зависимости.

Чтобы запустить оболочку, введите в консоль (или в конфигурацию Hyprland) `ignis init`.

## Стилизация
Все стили находятся в файле `style.scss`. Вы можете стилизовать **как вам угодно**.

Чтобы узнать какие у виджета CSS-классы, откройте GTK инспектор командой `ignis inspector`.
