{ pkgs, inputs, ... }:

{
  environment.systemPackages = with pkgs;
  let
    zen = inputs.zen-browser.packages.${stdenv.hostPlatform.system}.default;
  in [
    zellij
    ranger

    wget
    git

    zen
  ];
}
