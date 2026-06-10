{ ... }:

{
  programs.kitty = {
    enable = true;

    settings = {
      window_padding_width = 2.8;

      cursor_shape = "beam";
      cursor_trail = 1;

      confirm_os_window_close = 0;
    };
  };
}
