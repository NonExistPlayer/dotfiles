{ pkgs, ... }:

{
  programs.niri.enable = true;

  environment.systemPackages = with pkgs;
  [
    zellij

    wget
    git
    unzip
  ];
}
