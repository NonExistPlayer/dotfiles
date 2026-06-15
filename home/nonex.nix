{ pkgs, inputs, ... }:

{
  imports =
    [
       ../modules/user
    ];

  home.username = "nonex";
  home.homeDirectory = "/home/nonex";

  # My packages that I need but not belong to my dotfiles/ricing
  home.packages =
  let
    zen = inputs.zen-browser.packages.${pkgs.system}.default;
  in
  with pkgs; [
    zen
    vlc
    kdePackages.kdenlive
  ];

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
