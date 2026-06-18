{ pkgs, ... }:

{
  xdg.configFile."niri".source = ../../config/niri;

  home.packages = with pkgs; [ xwayland-satellite ];
}
