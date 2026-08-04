{ config, lib, pkgs, modulesPath, ... }:

{
  imports =
    [
      ./btrfs.nix
    ];

  hardware.bluetooth.enable = true;

  hardware.enableAllFirmware = true;
  hardware.graphics.enable = true;
  hardware.graphics.enable32Bit = true; 
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

  fileSystems = {
    "/" =
      {
	device = "/dev/disk/by-uuid/59523c6e-b0a8-4f88-9c36-01631ca561e8";
	fsType = "btrfs";
	options = [ "compress=zstd" "subvol=root" ];
      };

    "/home" =
      {
	device = "/dev/disk/by-uuid/59523c6e-b0a8-4f88-9c36-01631ca561e8";
	fsType = "btrfs";
	options = [ "compress=zstd" "subvol=home" ];
      };

    "/nix" =
      {
	device = "/dev/disk/by-uuid/59523c6e-b0a8-4f88-9c36-01631ca561e8";
	fsType = "btrfs";
	options = [ "compress=zstd" "noatime" "subvol=nix" ];
      };

    "/boot" =
      {
	device = "/dev/disk/by-uuid/12CE-A600";
	fsType = "vfat";
	options = [ "fmask=0022" "dmask=0022" ];
      };

    "/data/archive" =
      {
	device = "/dev/disk/by-uuid/9c4d1979-e0cc-4aa0-a2a5-8646b5146ff9";
	fsType = "ext4";
	options = [ "nofail" "x-gvfs-show" ];
      };

    "/data/doomsday" =
      {
	device = "/dev/disk/by-uuid/a37fe54c-bbd9-42de-889e-378f032d2696";
	fsType = "ext4";
	options = [ "nofail" "x-gvfs-show" ];
      };

    "/data/ssd" =
      {
	device = "/dev/disk/by-uuid/2f055135-3139-4e90-8dc7-6936873d1650";
	fsType = "ext4";
	options = [ "nofail" "x-gvfs-show" ];
      };
  };

  swapDevices = [ ];

  nixpkgs.hostPlatform = lib.mkDefault "x86_64-linux";
  hardware.cpu.amd.updateMicrocode = lib.mkDefault config.hardware.enableRedistributableFirmware;
}
