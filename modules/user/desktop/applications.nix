{ pkgs, ... }:

{
  programs.vicinae.enable = true;

  home.packages = with pkgs; [
    polkit_gnome

    adwaita-icon-theme
    nautilus
    gnome-calendar
    amberol
    baobab
    loupe
  ];
}
