{ lib, pkgs, inputs, ... }:

{
  imports =
    [
      ./packages.nix
    ];

  services.pipewire = {
    enable = true;
    pulse.enable = true;
  };

  services.libinput.enable = true;

  networking.networkmanager.enable = true;

  nix.settings.experimental-features = "nix-command flakes";
}
