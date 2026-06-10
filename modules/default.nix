{ lib, pkgs, inputs, ... }:

{
  # You can disable specific modules here:
  imports =
    [
      ./niri
    ];

  services.pipewire = {
    enable = true;
    pulse.enable = true;
  };

  services.libinput.enable = true;

  networking.networkmanager.enable = true;

  users.users.nonex = {
    isNormalUser = true;
    extraGroups = [ "wheel" ]; # Enable ‘sudo’ for the user.
    packages = with pkgs; [];
  };

  environment.systemPackages = with pkgs;
  let
    zen = inputs.zen-browser.packages.${stdenv.hostPlatform.system}.default;
  in [
    neovim
    zellij
    ranger
    wget
    git

    zen
  ];
}
