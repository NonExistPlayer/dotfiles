{ config, lib, pkgs, modulesPath, ... }:

{
  imports =
    [
    ];

  hardware.bluetooth.enable = false;

  hardware.graphics.enable = true;
  hardware.nvidia = {
    open = false;
    modesetting.enable = true;
    powerManagement.enable = false;
    package = pkgs.linuxPackages_latest.nvidiaPackages.legacy_580;
  };
  services.xserver.videoDrivers = [ "nvidia" ];

  nixpkgs.config.allowUnfreePredicate = pkg: builtins.elem (lib.getName pkg) [
    "nvidia-x11"
    "nvidia-settings"
    "nvidia-kernel-modules"
  ];

  networking.hostName = "nnixpc";

  boot = {
    kernelModules = [ ];
    extraModulePackages = [ ];

    initrd = {
      availableKernelModules = [ "xhci_pci" "ahci" "nvme" "usbhid" "usb_storage" "sd_mod" ];
      kernelModules = [ ];
    };

    loader = {
      grub = {
        enable = true;
        device = "nodev";
        efiSupport = true;
      };
      efi.canTouchEfiVariables = true;
    };
  };

  fileSystems."/" =
    {
      device = "/dev/disk/by-uuid/59523c6e-b0a8-4f88-9c36-01631ca561e8";
      fsType = "btrfs";
      options = [ "compress=zstd" "subvol=root" ];
    };

  fileSystems."/home" =
    {
      device = "/dev/disk/by-uuid/59523c6e-b0a8-4f88-9c36-01631ca561e8";
      fsType = "btrfs";
      options = [ "compress=zstd" "subvol=home" ];
    };

  fileSystems."/nix" =
    {
      device = "/dev/disk/by-uuid/59523c6e-b0a8-4f88-9c36-01631ca561e8";
      fsType = "btrfs";
      options = [ "compress=zstd" "noatime" "subvol=nix" ];
    };

  fileSystems."/boot" =
    {
      device = "/dev/disk/by-uuid/12CE-A600";
      fsType = "vfat";
      options = [ "fmask=0022" "dmask=0022" ];
    };

  swapDevices = [ ];

  nixpkgs.hostPlatform = lib.mkDefault "x86_64-linux";
  hardware.cpu.amd.updateMicrocode = lib.mkDefault config.hardware.enableRedistributableFirmware;
}
