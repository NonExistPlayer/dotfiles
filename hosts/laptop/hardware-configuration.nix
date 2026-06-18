{ config, lib, pkgs, modulesPath, ... }:

{
  imports =
    [ (modulesPath + "/installer/scan/not-detected.nix")
    ];

  hardware.bluetooth.enable = true;

  boot.initrd.availableKernelModules = [ "xhci_pci" "nvme" "usb_storage" "sd_mod" ];
  boot.initrd.kernelModules = [ ];
  boot.kernelModules = [ "kvm-intel" ];
  boot.extraModulePackages = [ ];

  fileSystems."/" =
    { device = "/dev/mapper/root";
      fsType = "ext4";
    };

  boot.initrd.luks.devices."root".device = "/dev/disk/by-uuid/6066fa5b-0c27-4eda-a2f5-6a275a3940f8";

  fileSystems."/boot" =
    { device = "/dev/disk/by-uuid/E2CA-99F6";
      fsType = "vfat";
      options = [ "fmask=0022" "dmask=0022" ];
    };

  swapDevices = [ ];

  nixpkgs.hostPlatform = lib.mkDefault "x86_64-linux";
  hardware.cpu.intel.updateMicrocode = lib.mkDefault config.hardware.enableRedistributableFirmware;
  hardware.graphics.extraPackages = with pkgs; [ intel-media-driver ];

  environment.systemPackages = with pkgs; [ brightnessctl ];
}
