{ ... }:

{
  home.username = "nonex";
  home.homeDirectory = "/home/nonex";

  programs.git = {
    enable = true;

    settings = {
      user.name = "NonExistPlayer";
      user.email = "nonexistplayer@gmail.com";

      alias = {
        s = "status";
        l = "log --oneline";
      };
    };
  };

  programs.kitty = {
    enable = true;

    settings = {
      window_padding_width = 2.8;

      cursor_shape = "beam";
      cursor_trail = 1;

      confirm_os_window_close = 0;
    };
  };

  home.stateVersion = "26.05";
}
