{ lib, pkgs, ... }:

{
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

  environment.systemPackages = with pkgs; [
    neovim
    wget
    git
  ];
}
