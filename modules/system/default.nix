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

  xdg.portal.enable = true;
  xdg.portal.extraPortals = [ pkgs.xdg-desktop-portal-gtk ];

  services.gnome.gnome-keyring.enable = true;

  security.polkit.enable = true;
  security.polkit.enablePkexecWrapper = true;

  nixpkgs.config.allowUnfree = true;
  services.happ.enable = true;

  virtualisation.docker.enable = true;

  services.libinput.enable = true;

  networking.networkmanager.enable = true;

  nix.settings.experimental-features = "nix-command flakes";
}
