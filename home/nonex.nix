{ pkgs, inputs, ... }:

{
  imports =
    [
       ../modules/user
    ];

  home.username = "nonex";
  home.homeDirectory = "/home/nonex";

  nixpkgs.config.allowUnfree = true;

  services.syncthing.enable = true;

  # My packages that I need but not belong to my dotfiles/ricing
  home.packages =
  let
    zen = inputs.zen-browser.packages.${pkgs.system}.default;
  in
  with pkgs; [
    telegram-desktop
    zen
    vlc
    kdePackages.kdenlive
    steam
    srb2
  ];

  nixpkgs.overlays = [
    (final: prev: {
      steam = prev.steam.override {
        extraArgs = "-cef-disable-gpu-compositing";
      };
    })   
  ];
  

  programs.obsidian.enable = true;

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
