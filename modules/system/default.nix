{ ... }:

{
  imports =
    [
      ./gvfs.nix
      ./packages.nix
      ./pipewire.nix
      ./polkit.nix
    ];

  services.libinput.enable = true;

  networking.networkmanager.enable = true;

  nix.settings.experimental-features = [ "nix-command" "flakes" ];
}
