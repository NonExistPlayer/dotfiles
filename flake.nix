{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

    home-manager = {
      url = "github:nix-community/home-manager";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    zen-browser = {
      url = "github:youwen5/zen-browser-flake";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    happ = {
      url = "github:NonExistPlayer/happ.nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };
  outputs = inputs@{ self, nixpkgs, ... }: {
    nixosConfigurations.laptop =
       nixpkgs.lib.nixosSystem {
         system = "x86_64-linux";
         specialArgs = { inherit inputs; };
         modules = [
	   ./hosts/laptop
	   ./modules/system
	   inputs.home-manager.nixosModules.home-manager
	   inputs.happ.nixosModules.default
         ];
       };
    nixosConfigurations.pc =
       nixpkgs.lib.nixosSystem {
         system = "x86_64-linux";
         specialArgs = { inherit inputs; };
         modules = [
	   ./hosts/pc
	   ./modules/system
	   inputs.home-manager.nixosModules.home-manager
	   inputs.happ.nixosModules.default
         ];
       };
  };
}
