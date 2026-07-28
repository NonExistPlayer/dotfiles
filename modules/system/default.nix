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

  services.gvfs.enable = true;

  security.polkit.enable = true;
  security.polkit.enablePkexecWrapper = true;

  nixpkgs.config.allowUnfree = true;
  services.happ.enable = true;

  virtualisation.docker.enable = true;

  services.libinput.enable = true;

  networking.networkmanager.enable = true;

  nix.settings.experimental-features = "nix-command flakes";
}
