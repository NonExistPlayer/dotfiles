{ pkgs, ... }:

{
  xdg.configFile."niri".source = ../../config/niri;

  home.packages = with pkgs; [
    xwayland-satellite
    polkit_gnome

    adwaita-icon-theme
    nautilus
    gnome-calendar
    amberol
    baobab
    loupe
  ];

  programs.vicinae.enable = true;
  home.pointerCursor = {
    enable = true;
    gtk.enable = true;
    x11.enable = true;

    package = pkgs.bibata-cursors;
    name = "Bibata-Modern-Ice";
    size = 32;
  };
}
