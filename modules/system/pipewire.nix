{ pkgs, ... }:

{
  services.pipewire.enable = true;
  services.pipewire.pulse.enable = true;

  environment.systemPackages = with pkgs; [ pwvucontrol ];
}
