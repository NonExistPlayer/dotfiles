{ pkgs, ... }:

{
  programs.niri.enable = true;

  environment.systemPackages = with pkgs;
  [
    wget
    git
    unzip
  ];

  fonts.packages = with pkgs.nerd-fonts; [ fira-code droid-sans-mono ];
}
