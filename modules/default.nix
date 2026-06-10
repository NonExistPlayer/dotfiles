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

  home-manager = {
    useGlobalPkgs = true;
    useUserPackages = true;

    users.nonex = import ../home/nonex.nix;
  };

  programs.neovim = {
    enable = true;
    defaultEditor = true;
  };

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
