{ pkgs, ... }:

{
  programs.niri.enable = true;

  environment.systemPackages = with pkgs;
  [
    wget
    git
    unzip
  ];
}
