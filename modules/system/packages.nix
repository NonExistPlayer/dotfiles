{ pkgs, inputs, ... }:

{
  programs.niri.enable = true;

  environment.systemPackages = with pkgs;
  let
    zen = inputs.zen-browser.packages.${stdenv.hostPlatform.system}.default;
  in [
    zellij

    wget
    git
    unzip

    zen
  ];
}
