{ ... }:

{
  imports =
    [
       ../modules/user
    ];

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

  home.stateVersion = "26.05";
}
