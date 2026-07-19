{ pkgs, ... }:

{
  xdg.configFile."niri".source = ../../config/niri;

  home.packages = with pkgs; [
    xwayland-satellite

    adwaita-icon-theme
    nautilus
    gnome-calendar
    amberol
    baobab
    loupe
  ];

  programs.vicinae.enable = true;
}
