{ ... }:

{
  programs.waybar = {
    enable = true;
    systemd.enable = true;

    settings.bar = {
      layer = "top";
      position = "bottom";

      modules-left = [ "niri/workspaces" ];
      modules-center = [ "niri/window" ];
      modules-right = [ "battery" "niri/language" "clock" ];
    };
  };
}
