{ pkgs, ... }:

{
  programs.vicinae.enable = true;

  home.packages = with pkgs; [
    polkit_gnome

    adwaita-icon-theme
    nautilus
    file-roller
    gnome-calendar
    amberol
    baobab
    loupe
  ];
}
