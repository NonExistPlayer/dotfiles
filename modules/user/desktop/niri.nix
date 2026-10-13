{ pkgs, ... }:

{
  xdg.configFile = {
    "niri/config.kdl".source = ../../../config/niri/config.kdl;
    "niri/animations.kdl".source = ../../../config/niri/animations.kdl;
    "niri/binds.kdl".source = ../../../config/niri/binds.kdl;
    "niri/input.kdl".source = ../../../config/niri/input.kdl;
    "niri/layout.kdl".source = ../../../config/niri/layout.kdl;
    "niri/vicinae.kdl".source = ../../../config/niri/vicinae.kdl;
    "niri/winrules.kdl".source = ../../../config/niri/winrules.kdl;
  };

  home.packages = with pkgs; [ xwayland-satellite ];

  home.pointerCursor = {
    enable = true;
    gtk.enable = true;
    x11.enable = true;

    package = pkgs.bibata-cursors;
    name = "Bibata-Modern-Ice";
    size = 32;
  };
}
