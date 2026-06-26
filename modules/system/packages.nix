{ pkgs, ... }:

{
  programs.niri.enable = true;

  environment.systemPackages = with pkgs;
  [
    zellij

    distrobox

    wget
    git
    unzip
  ];
}
